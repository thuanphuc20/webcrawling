CREATE DATABASE local_db;
USE local_db;

CREATE TABLE mondo (
    id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    tensanpham VARCHAR(255) NOT NULL DEFAULT '',
    gia VARCHAR(55),
    chitiet VARCHAR(255),
    img VARCHAR(255)
    link VARCHAR(1000),
    PRIMARY KEY (id)
);
