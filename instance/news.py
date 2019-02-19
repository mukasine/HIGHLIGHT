class News:
    '''
    News class to define News Objects
    '''
def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

        {% extends 'base.html'%}
<!-- Content block -->
{% block content %}
<div class="container">

    <!-- Poster background -->
    <div class="row">
        <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 posterPath" style="background: url({{news.poster}}) no-repeat center center">
        </div>

        <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 news-details">
            <h3>{{ news.title }}</h3>

            <p class="overview"> {{ news.overview }}</p>
            <p class="ratings"> <b> {{ news.vote_average }}</b> - <i>{{ news.vote_count}} votes </i> </p>


        </div>
    </div>

</div>
{% endblock %}