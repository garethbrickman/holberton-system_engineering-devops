-- Creates new database, table, inserts dummy values, gives SELECT permission
CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (id INT, name VARCHAR(256));
INSERT INTO tyrell_corp.nexus6 (id, name) VALUES (1, "Leon")
USE tyrell_corp;
GRANT SELECT ON nexus6 TO 'holberton_user'@'localhost';
