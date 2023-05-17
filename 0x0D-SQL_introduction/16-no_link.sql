-- Lists all records of the table in descending order.
-- Doesn't list rows without a name value.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
