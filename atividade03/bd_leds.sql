CREATE DATABASE db_leds;

USE db_leds;

CREATE TABLE tbl_leds (
	id INT UNSIGNED AUTO_INCREMENT,
    _led VARCHAR(13),
    date_time DATETIME DEFAULT NOW(),
    CONSTRAINT tbl_leds_id_pk PRIMARY KEY (id)
);

SELECT * FROM tbl_leds;