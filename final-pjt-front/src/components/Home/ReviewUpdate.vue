<template>
<body class="back">
  
	<h1>리뷰 수정</h1>
  
  <div id="form">

  <div class="fish" id="fish"></div>
  <div class="fish" id="fish2"></div>

  <form id="waterform" @submit.prevent="updateReview(information, $route.params.category, $route.params.id)">

  <div class="formgroup" id="name-form">
      <label for="title">제목</label>
      <input type="text" id="title" name="title" v-model.trim="information.title" />
  </div>

  <div class="formgroup" id="message-form">
      <label for="content">내용</label>
      <textarea id="content" name="content" v-model.trim="information.content"></textarea>
  </div>
    <input type="submit" value="제출" />
  </form>
		<input class="center-block" type="button" value="취소" @click="backToDetail($route.params.category, $route.params.category_id, $route.params.id)"/>
  </div>
</body>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  props: {
    review: {
      required: true,
    }
  },

  data: function () {
    return {
      information: {
        title: this.review.title,
        content: this.review.content,
      },
    }
  },

  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `Bearer ${token}`
      }
      return config
    },

    updateReview: function (information, category, id) {
        const headers = this.setToken()
        axios({
            url: `${SERVER_URL}/community/reviews/${category}/${id}/`,
            method: 'put',
            data: information,
            headers,
          })
        .then((res) => {
          this.$router.push({ name: 'ReviewDetail', params: { category: `${category}`, category_id: this.$route.params.id, id: `${res.data.pk}` }})
        })
        .catch((err) => {
            console.log(err)
        })
		},
		backToDetail: function (category, category_id, id) {
			this.$router.push({ name: 'ReviewDetail', params: { category, category_id, id }})
		}
  }
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Sniglet|Raleway:900);
.back {
		background: #0f3854;
		background: radial-gradient(ellipse at center,  #0a2e38  0%, #000000 160%);
		background-size: 100%;
}

body, html{
	height: 100%;
	padding: 0;
	margin: 0;
	font-family: 'Raleway', sans-serif;
}
h1{
	font-weight: normal;
	font-size: 3em;
	font-family: 'Raleway', sans-serif;
	margin: 0 auto;
	padding-top: 20px;
	width: 500px;
	color: white;
	text-align: center;

}

/* Animation webkit */
@-webkit-keyframes myfirst
{
	0% {margin-left: -235px}
	90% {margin-left: 100%;}
	100% {margin-left: 100%;}
}

/* Animation */
@keyframes myfirst
{
	0% {margin-left: -235px}
	70% {margin-left: 100%;}
	100% {margin-left: 100%;}
}

.fish{
	background-image: url('http://www.geertjanhendriks.nl/codepen/form/fish.png');
	width: 235px;
	height: 104px;
	margin-left: -235px;
	position: absolute;	
	animation: myfirst 24s;
	-webkit-animation: myfirst 24s;
	animation-iteration-count: infinite;
	-webkit-animation-iteration-count: infinite;
	animation-timing-function: linear;
	-webkit-animation-timing-function: linear;
}

#fish{
	top: 120px;
}

#fish2{
	top: 260px;
	animation-delay: 12s;
	-webkit-animation-delay: 12s;
}

form{
	margin: 0 auto;
	width: 600px;
	color: white;
	position: relative;
	
	
}
label, input, textarea{
	display: block;	
}
input, textarea{
  background-color: white;
	width: 600px;	
	border: none;
	border-radius: 20px;
	outline: none;
	padding: 10px;
	font-family: 'Raleway', sans-serif;
	font-size: 1em;
	color: #676767;
	transition: border 0.5s;
	-webkit-transition: border 0.5s;
	-moz-transition: border 0.5s;
	-o-transition: border 0.5s;
	border: solid 3px #78909C;	
	-webkit-box-sizing:border-box;
	-moz-box-sizing:border-box;
	box-sizing:border-box;
	
}
input:focus, textarea:focus{
	border: solid 3px #77bde0;	
}

textarea{
	height: 300px;	
	resize: none; 
	overflow: auto;
}
input[type="submit"]{
	background-color: #7CD0D5;
	color: white;
	height: 50px;
	cursor: pointer;
	margin-top: 30px;
	margin-bottom: 15px;
	font-size: 1.29em;
	font-family: 'Raleway', sans-serif;
	-webkit-transition: background-color 0.5s;
	-moz-transition: background-color 0.5s;
	-o-transition: background-color 0.5s;
	transition: background-color 0.5s;
}
input[type="submit"]:hover{
	background-color: #FF7043;
	
}
label{
	font-size: 1.5em;
	margin-top: 20px;
	padding-left: 20px;
}
.formgroup, .formgroup-active, .formgroup-error{
	background-repeat: no-repeat;
	background-position: right bottom;
	background-size: 10.5%;
	transition: background-image 0.7s;
	-webkit-transition: background-image 0.7s;
	-moz-transition: background-image 0.7s;
	-o-transition: background-image 0.7s;
	width: 566px;
	padding-top: 2px;
}

input[type="button"]{
	display: block;
  margin-right: auto;
  margin-left: auto;
	background-color: #7CD0D5;
	color: white;
	height: 50px;
	cursor: pointer;
	margin-bottom: 20px;
	font-size: 1.29em;
	font-family: 'Raleway', sans-serif;
	-webkit-transition: background-color 0.5s;
	-moz-transition: background-color 0.5s;
	-o-transition: background-color 0.5s;
	transition: background-color 0.5s;
}
input[type="button"]:hover{
	background-color: #EC407A;
	
}

</style>
