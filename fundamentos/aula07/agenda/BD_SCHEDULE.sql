CREATE DATABASE bd_schedule;

USE bd_schedule;

# DROP DATABASE bd_schedule;

CREATE TABLE tbl_schedules (
	_id INT UNSIGNED NOT NULL,
	_type VARCHAR(13),
    _name VARCHAR(150),
    _email VARCHAR(150),
    _tel VARCHAR(11),
    CONSTRAINT tbl_schedules_id_pk PRIMARY KEY (_id)
);

SELECT * FROM tbl_schedules;