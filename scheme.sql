USE mysql;
UPDATE user SET Grant_priv='Y' WHERE user='root';
CREATE DATABASE games;
USE games;
CREATE TABLE users_scores (ID int PRIMARY KEY,score int);
INSERT INTO games.users_scores (ID, score) VALUES (1, 0);