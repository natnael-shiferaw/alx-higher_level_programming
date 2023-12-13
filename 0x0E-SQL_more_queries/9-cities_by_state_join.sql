-- List all cities from the 'hbtn_0d_usa' database with their corresponding states
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id;
