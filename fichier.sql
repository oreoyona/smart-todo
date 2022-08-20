CREATE TABLE subscriptions(
    num BIGINT PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL
);

CREATE TABLE carabin(
    id serial PRIMARY KEY,
    nom varchar(120) NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    subscrption_num BIGINT REFERENCES subscriptions(num),
    UNIQUE(subscrption_num)

);


INSERT INTO carabin (nom, email) VALUES ('Jilembi kabu', 'uuadpe@gmail.com');
INSERT INTO carabin (nom, email) VALUES ('Opius rhabu', 'opiusrhabe@gmail.com');
INSERT INTO carabin (nom, email) VALUES ('Numio Osami', 'osami@gmail.com');
INSERT INTO carabin (nom, email) VALUES ('Nathan kabu', 'kabunathan@gmail.com');
INSERT INTO carabin (id, nom, email) VALUES (77854,'Gloire Chabu', 'gloirechabu@gmail.com');

INSERT INTO subscriptions (num, start_time, end_time) VALUES (77854, '1999-01-08 04:05:06', '2009-01-08 04:05:06');
INSERT INTO subscriptions (num, start_time, end_time) VALUES (8898,'2009-01-08 04:05:06', '2010-01-08 04:05:06');