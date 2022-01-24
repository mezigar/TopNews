<template>
    <div class="buddy">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/cerulean/bootstrap.min.css" integrity="sha384-3fdgwJw17Bi87e1QQ4fsLn4rUFqWw//KU0g8TvV6quvahISRewev6/EocKNuJmEw" crossorigin="anonymous">    
        <div class="container">
            <div class="sort">
                
            </div>

            <table>
                <tr>
                    <th>
                        <button  v-on:click="show_yandex=!show_yandex">
                            <h4>Яндекс</h4> 
                        </button>
                           
                    </th>

                    <th>
                        <button  v-on:click="show_ria=!show_ria">
                            <h4>Риа</h4>
                        </button>

                    </th>

                     <th>
                        <button  v-on:click="show_lenta=!show_lenta">
                            <h4>Лента</h4>
                        </button>

                    </th>

                    <th>
                       <button  v-on:click="show_all=!show_all">
                            <h4>Все новости</h4>
                        </button>

                    </th>
                </tr>
            </table>

            <ul id="list_news" v-if="show_yandex">
                <h5>Яндекс новости:</h5>
                <li class="li-style" v-for="(item, idx) in news[1]" v-bind:key="idx">
                    <a v-bind:href=item[2]>
                        <p>{{ item[0]+1 }}: {{ item[1] }}</p>
                    </a>
                </li>
            </ul>
            
            <ul id="list_news" v-if="show_ria">
                <h5>Риа новости:</h5>
                <li class="li-style" v-for="(item, idx) in news[3]" v-bind:key="idx">
                    <a v-bind:href=item[2]>
                        <p>{{ item[0]+1 }}: {{ item[1] }}</p>
                    </a>
                </li>
            </ul>

            <ul id="list_news" v-if="show_lenta">
                <h5>Лента новости</h5>
                <li class="li-style" v-for="(item, idx) in news[5]" v-bind:key="idx">
                    <a v-bind:href=item[2]>
                        <p>{{ item[0]+1 }}: {{ item[1] }}</p>
                    </a>
                </li>
            </ul>

            <ul id="list_news" v-if="show_all">
                <div v-for='(bunch_of_news, idx) in news' v-bind:key="idx">
                    <div v-if="idx % 2 == 1" v-bind:key="idx">
                        <li class="li-style"  v-for="item in bunch_of_news" v-bind:key="item">
                            <a v-bind:href="item[2]">
                                <p>{{ item[0]+1 }}: {{ item[1] }}</p>
                            </a>
                        </li>
                    </div>
                    <div v-else>
                        <h5>{{ news[idx] }}</h5>
                    </div>
                </div>
            </ul>            
                        
                    <div id="footer" class="page-footer font-medium blue">
                        <div class="footer-copyright text-center py-3">© 2022 Copyright:
                        <a href="https://mdbootstrap.com/"> My CV</a>
                    </div>
                </div>
            </div>
        </div>



</template>

<script>
import axios from 'axios';
export default {
  data: function() {
      return {
        news: [],
        show_yandex: false,
        show_ria: false,
        show_lenta: false,
        show_all: false

      };
    },
    methods: {
        getNews() {
            const path = "http://127.0.0.1:5000/news"
            axios.get(path)
            .then((res) => {
                this.news = res.data.news
                console.log(this.news)

            })
            .catch((err) => {
                console.log(err)
            });
        },

    },
    created() {
        this.getNews();
    }
}
</script>

<style scoped>
li {
    position: relative;
    margin-bottom: 1.5em;
    border: 3px solid #4e4929;
    padding: 0.6em;
    border-radius: 10px;
    background: #378683;
    color: #231F20;
    font-family: "Trebuchet MS", "Lucida Sans";
    list-style-type: none; /* Убираем маркеры */
}

button {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    padding: 0.6em;
    top: 10;
    background:#05386b;
}

h4 {
    color:#EDF5E1;
}

h5{
    color: #05386b;
}

a {
    /* color:#1a068f; */
    color: white;
}
a:visited {
    color:#2803fa;
}
a:active {
    color:#231F20;
}
table {
    width: auto;
    border: 1px solid green;
    margin: auto;
}
/* th {
    position:center; 
    margin-left: 50%; 
    margin-right: 50%;
} */
.buddy {
    background-color:#5CDB95;
    min-height: 100vh;
}

#footer {
    position: absolute;
    bottom: 0;
  
}
</style>
