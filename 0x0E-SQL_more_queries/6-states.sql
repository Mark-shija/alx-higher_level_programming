-- creates the database hbtn_0d_usa and the table states
-- in the database hbtn_0d_usa) on your MySQL serve
-- id INT unique, auto generated, can’t be null and is a primary key
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
