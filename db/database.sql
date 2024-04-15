-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS user_auth;
USE user_auth;

CREATE TABLE utilisateurs (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');

