-- 1. Limpeza (Opcional: Garante que comece do zero se rodar de novo)
DROP TABLE IF EXISTS movie_actors;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS series;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS genres;

-- 2. Criação das Tabelas (Baseado nos seus 4 Blueprints)
CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE actors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    year INTEGER,
    genre_id INTEGER REFERENCES genres(id)
);

CREATE TABLE series (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    seasons INTEGER,
    genre_id INTEGER REFERENCES genres(id)
);

-- 3. Inserção de Dados (O "Seed" propriamente dito)
INSERT INTO genres (name) VALUES ('Ação'), ('Ficção Científica'), ('Drama'), ('Terror');

INSERT INTO actors (name, country) VALUES 
('Keanu Reeves', 'Líbano'),
('Cillian Murphy', 'Irlanda'),
('Millie Bobby Brown', 'Reino Unido');

INSERT INTO movies (title, year, genre_id) VALUES 
('The Matrix', 1999, 2),
('John Wick', 2014, 1),
('Oppenheimer', 2023, 3);

INSERT INTO series (title, seasons, genre_id) VALUES 
('Stranger Things', 4, 2),
('The Boys', 3, 1),
('Peaky Blinders', 6, 3);