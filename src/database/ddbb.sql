CREATE DATABASE simpleapi_example;

USE simpleapi_example;
CREATE TABLE users(
    id          int(255) AUTO_INCREMENT NOT NULL,
    username    varchar(20) NOT NULL,
    fullname    varchar(40) NOT NULL,
    email       varchar(40) NOT NULL,
    disabled    tinyint(1) NOT NULL,
    password    varchar(255) NOT NULL,

    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_users UNIQUE(username, email)
);

INSERT INTO users (
    username,
    fullname,
    email, 
    disabled,
    password
) 
VALUES (
    'test',
    'Test Tester',
    'test@test.com',
    0,
    'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae'
);