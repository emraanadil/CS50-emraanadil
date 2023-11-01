-- write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
select title from movies join stars on stars.movie_id = movies.id join people on people.id = stars.person_id where people.name = "Johnny Depp"
INTERSECT
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter";