SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = 'slovene' ORDER BY percentage DESC;


SELECT countries.name, COUNT(cities.id) AS totalcitys
FROM countries
JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name ORDER BY totalcitys DESC; 


SELECT cities.name, cities.population
FROM countries 
JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'mexico' 
AND cities.population > 500000 ORDER BY population DESC;


SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89 ORDER BY percentage DESC;

SELECT countries.name, countries.surface_area, countries.population
FROM countries 
WHERE countries.surface_area < 501
AND countries.population > 100000;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'constitutional monarchy'
AND countries.capital > 200
AND countries.life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population 
FROM countries
JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "argentina"
AND cities.district = "buenos aires"
AND cities.population > 500000;



SELECT countries.region, COUNT(countries.name) AS howmany
FROM countries
GROUP BY countries.region ORDER BY howmany DESC; 



SELECT cities.district
FROM cities;






