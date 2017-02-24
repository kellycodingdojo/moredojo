What query would you run to get all the customers inside city_id = 312? 
Your query should return customer first name, last name, email, and address.

SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM city
JOIN address
ON city.city_id = address.city_id
JOIN customer
on address.address_id = customer.address_id
WHERE city.city_id = 312;


 


What query would you run to get all comedy films? Your query should return film title, 
description, release year, rating, special features, and genre (category).


SELECT film.film_id, film.title, film.description, film.release_year, film.special_features, category.name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE category.name = 'comedy';



WHY ARENT THERE FORIEN KEYS????
What query would you run to get all the films joined by actor_id=5?
 Your query should return the film title, description, and release year.
 
SELECT film.film_id, film.title, film.description, film.release_year
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

this is pats
Select actor.actor_id, actor.first_name, actor.last_name, film.film_id, film.title, film.description, film.release_year
FROM film_actor
JOIN actor 
ON film_actor.actor_id = actor.actor_id
JOIN film 
ON film_actor.film_id = film.film_id
WHERE film_actor.actor_id = 5;


What query would you run to get all the customers in store_id = 1 and inside these cities
(1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.


SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, address.address
FROM customer
JOIN address
ON customer.address_id = address.address_id
JOIN city
ON address.city_id = city.city_id
JOIN store
ON customer.store_id = store.store_id
WHERE store.store_id = 1 AND city.city_id IN(1,42,312,459);

What query would you run to get all the films with a "rating = G"
 and "special feature = behind the scenes", joined by actor_id = 15? 
 Your query should return the film title, description, release year, rating, 
 and special feature. Hint: You may use LIKE function in getting the 'behind the scenes' part.

SELECT  film.special_features AS behind_the_scenes, film.title, film.description, film.release_year, film.rating, actor.actor_id
FROM film 
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15 
AND film.rating = "g";

What query would you run to get all the actors that joined in the film_id = 369?
 Your query should return the film_id, title, actor_id, and actor_name.

SELECT  film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

What query would you run to get all drama films with a rental rate of 2.99? 
Your query should return film title, description, release year,
 rating, special features, and genre (category).
 
SELECT film.film_id, film.rental_rate, film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
WHERE film.rental_rate = '2.99'
AND category.name = "drama";


What query would you run to get all the action films which are joined by SANDRA KILMER?
Your query should return film title, description, release year, rating, special features, 
genre (category), and actors first name and last name.

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
from film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE category.name = "action"
AND actor.first_name = "sandra"
AND actor.last_name = "kilmer";



