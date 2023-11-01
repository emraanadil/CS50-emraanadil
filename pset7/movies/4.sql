-- no of movies rating of 10
select count(title) from movies join ratings on movies.id = ratings.movie_id where rating = "10.0";