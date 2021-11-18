import requests, json


class TmdbAPI:
    base_url = 'https://api.themoviedb.org/3'
    poster_url = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2'

    def __init__(self, api_key):
        self.key = api_key
    

    def get_url(self, category, feature, **kwargs):
        url = f'{self.base_url}/{category}/{feature}?api_key={self.key}'

        for key, value in kwargs.items():
            url += f'&{key}={value}'
        return url
    
    
    def get_genre(self):
        url = self.get_url('genre', 'movie/list', language='ko')
        response = requests.get(url)
        datas = response.json()

        genres = []
        for data in datas['genres']:
            genre = {}
            genre['model'] = "movies.genre"
            genre['pk'] = data['id']
            genre['fields'] = {}
            genre['fields']['name'] = data['name']
            genres.append(genre)
        return genres


    def get_actor_detail(self, actor_id):
        url = self.get_url('person', f'{actor_id}', region='KR', language='ko')
        response = requests.get(url)
        data = response.json()
        return data['birthday'], data['place_of_birth']


    def get_actor(self, movie_id, actors, actor_vst):
        url = self.get_url('movie', f'{movie_id}/credits', region='KR', language='ko')
        response = requests.get(url)
        datas = response.json()

        actor_list = []
        for data in datas['cast']:
            if data['id'] in actor_vst: continue
            actor = {}
            actor['model'] = "movies.actor"
            actor['pk'] = data['id']
            actor['fields'] = {}
            actor['fields']['name'] = data['name']
            actor['fields']['gender'] = data['gender']
            actor['fields']['birth_date'], actor['fields']['birth_place'] = self.get_actor_detail(data['id'])
            actor['fields']['profile_path'] = data['profile_path']
            actors.append(actor)
            actor_vst.add(data['id'])
            actor_list.append(data['id'])
        return actor_list


    def get_data(self):
        movies = []
        actors = []
        actor_vst = set()
        for page in range(1, 101):
            url = self.get_url('movie', 'popular', region='KR', language='ko', page=page)
            response = requests.get(url)
            datas = response.json()

            for data in datas['results']:
                movie = {}
                movie['model'] = "movies.movie"
                movie['pk'] = data['id']
                movie['fields'] = {}
                movie['fields']['genres'] = data['genre_ids']
                movie['fields']['actors'] = self.get_actor(data['id'], actors, actor_vst)
                movie['fields']['title'] = data['title']
                movie['fields']['overview'] = data['overview']
                movie['fields']['release_date'] = data['release_date']
                movie['fields']['vote_average'] = data['vote_average']
                movie['fields']['vote_count'] = data['vote_count']
                movie['fields']['poster_path'] = data['poster_path']
                movies.append(movie)
            print(f'현재 페이지={page} || 진행률={page}%')

        genres = self.get_genre()
        print(genres)
        with open('./final-pjt-back/movies/fixtures/genres.json', 'w', encoding="utf-8") as make_file:
            json.dump(genres, make_file, ensure_ascii=False, indent="\t")
        with open('./final-pjt-back/movies/fixtures/actors.json', 'w', encoding="utf-8") as make_file:
            json.dump(actors, make_file, ensure_ascii=False, indent="\t")
        with open('./final-pjt-back/movies/fixtures/movies.json', 'w', encoding="utf-8") as make_file:
            json.dump(genres+actors+movies, make_file, ensure_ascii=False, indent="\t")
        return 'Finish'


helper = TmdbAPI('233360b926375559342a878b1b52e833')
helper.get_data()

# from server.settings import env
# helper = TmdbAPI(env('TMDB_KEY'))
# from pprint import pprint
