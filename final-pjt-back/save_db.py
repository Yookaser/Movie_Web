from movies.utils.tmdb_api import helper
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()
from movies.models import Genre

def genre():
    datas = helper.get_genre()
    print(datas)
    # Genre.objects.bulk_create(datas['genres'])

genre()
