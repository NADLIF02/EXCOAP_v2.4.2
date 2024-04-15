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

CREATE TABLE evenements (
    id SERIAL PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    description TEXT,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    couleur VARCHAR(255) DEFAULT '#ff9f89'
);

