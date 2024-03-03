$(function() {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
        var moviesList = data.results.map(function(movie) {
            return `<li>${movie.title}</li>`;
        }).join('');
        $('ul#list_movies').append(moviesList);
    });
});

