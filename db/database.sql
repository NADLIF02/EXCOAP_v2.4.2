-- Création de la base de données si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS user_auth;
USE user_auth;

-- Création de la table des utilisateurs
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

-- Insertion des utilisateurs dans la table utilisateurs
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');
INSERT INTO utilisateurs (type, mot_de_passe) VALUES ('fer5rfr', 'password123');

-- Création de la table des événements
CREATE TABLE IF NOT EXISTS evenements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    description TEXT,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    couleur VARCHAR(255) DEFAULT '#ff9f89'
);
