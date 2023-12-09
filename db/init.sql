-- DROP TABLE game_child, game_master, block_list, friend_list, friend_request, tournament_match,
-- 			tournament_players, tournaments_master, user_settings, email_users, intra_users;
CREATE TABLE primary_users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    user_type VARCHAR(50) NOT NULL --type is intra or user
);

CREATE TABLE intra_users (
    user_id INT PRIMARY KEY REFERENCES primary_users(id),
    intra_name VARCHAR(255) NOT NULL
);

CREATE TABLE email_users (
    user_id INT PRIMARY KEY REFERENCES primary_users(id),
    email_id VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE user_settings (
    user_id INT PRIMARY KEY REFERENCES primary_users(id),
    nickname VARCHAR(255) NOT NULL,
    avatar VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    is_logged BOOLEAN NOT NULL
);

CREATE TABLE tournaments_master (
    tournament_id SERIAL PRIMARY KEY,
    owner_id INT NOT NULL REFERENCES primary_users(id),
    name VARCHAR(255) NOT NULL,
    players INT NOT NULL,
    end_date TIMESTAMP NOT NULL,
    start_date TIMESTAMP NOT NULL
);

CREATE TABLE tournament_players (
    tournament_id INT NOT NULL REFERENCES tournaments_master(tournament_id),
    player_id INT NOT NULL REFERENCES primary_users(id),
    player_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (tournament_id, player_id)
);

CREATE TABLE tournament_match (
    tournament_id INT NOT NULL REFERENCES tournaments_master(tournament_id),
    match_id SERIAL PRIMARY KEY,
    player1_id INT NOT NULL REFERENCES primary_users(id),
    player2_id INT NOT NULL REFERENCES primary_users(id),
    player1_score INT NOT NULL,
    player2_score INT NOT NULL,
    round INT NOT NULL,
    match_date TIMESTAMP NOT NULL,
    is_played BOOLEAN NOT NULL
);

CREATE TABLE friend_request (
    request_id SERIAL PRIMARY KEY,
    sender_id INT NOT NULL REFERENCES primary_users(id),
    receiver_id INT NOT NULL REFERENCES primary_users(id),
    status VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE friend_list (
    friend_id SERIAL PRIMARY KEY,
    user_id_1 INT NOT NULL REFERENCES primary_users(id),
    user_id_2 INT NOT NULL REFERENCES primary_users(id)
);

CREATE TABLE block_list (
    user_id INT NOT NULL REFERENCES primary_users(id),
    block_id INT NOT NULL REFERENCES primary_users(id),
    PRIMARY KEY (user_id, block_id)
);

CREATE TABLE game_master (
    game_id SERIAL PRIMARY KEY,
    date_time TIMESTAMP NOT NULL,
    game_map VARCHAR(255) NOT NULL,
    game_mode VARCHAR(50) NOT NULL,
    player_1 INT NOT NULL REFERENCES primary_users(id),
    player_2 INT NOT NULL REFERENCES primary_users(id)
);

CREATE TABLE game_child (
    game_id INT NOT NULL REFERENCES game_master(game_id),
    score_p1 INT NOT NULL,
    score_p2 INT NOT NULL,
    winner INT NOT NULL REFERENCES primary_users(id),
    loser INT NOT NULL REFERENCES primary_users(id),
    points_won INT NOT NULL,
    points_lost INT NOT NULL,
    PRIMARY KEY (game_id)
);

