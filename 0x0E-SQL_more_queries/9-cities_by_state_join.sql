-- Lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = state.id
ORDER BY cities.id ASC;
