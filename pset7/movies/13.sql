--, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starre
select distinct(name) from people
join stars on stars.person_id = people.id
join movies on movies.id = stars.movie_id
where movies.title IN(SELECT distinct(movies.title) FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Kevin Bacon" AND people.birth = 1958) AND people.name != "Kevin Bacon";