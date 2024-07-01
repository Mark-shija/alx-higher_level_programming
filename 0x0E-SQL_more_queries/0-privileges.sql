-- Script to list all privileges of user_0d_1 and user_0d_2

-- Check and create users if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Granting privileges to the users if they are newly created
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- List all privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List all privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
