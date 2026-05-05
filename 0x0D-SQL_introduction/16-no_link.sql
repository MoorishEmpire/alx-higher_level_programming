-- List all records of the database "second_table"
-- of the database "hbtn_0c_0" in MySQL server.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL and name != ""
ORDER BY score DESC;