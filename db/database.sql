-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS user_auth;
USE user_auth;

-- Create a 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optionally, insert a test user (password should be hashed in a real scenario)
INSERT INTO users (username, password_hash, email) VALUES ('testuser', 'testhash', 'test@example.com');
