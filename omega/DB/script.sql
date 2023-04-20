create database omega;

use omega;

SET SQL_SAFE_UPDATES = 0;


create table autor (
id INT NOT NULL PRIMARY KEY auto_increment,
jmeno_autor VARCHAR(50) NOT NULL,
prijmeni_autor VARCHAR(50) NOT NULL,
email_autor VARCHAR(50) NOT NULL,
prezdivka_autor VARCHAR(50) NOT NULL,
heslo_autor VARCHAR(25) NOT NULL,
ban BOOL NOT NULL
);

create table komentar (
id INT NOT NULL PRIMARY KEY auto_increment,
autor_id INT NOT NULL,
FOREIGN KEY (autor_id) REFERENCES autor(id),
clanek_id INT,
FOREIGN KEY (clanek_id) REFERENCES clanek(id),
text_komenatre VARCHAR(200) NOT NULL,
datum_komentare DATE NOT NULL
);

create table clanek (
id INT NOT NULL PRIMARY KEY auto_increment,
autor_id INT NOT NULL,
FOREIGN KEY (autor_id) REFERENCES autor(id),
text_clanku VARCHAR(500) NOT NULL,
datum_clanku DATE NOT NULL
);

create table admin1 (
id INT NOT NULL PRIMARY KEY auto_increment,
jmeno_admin VARCHAR(50) NOT NULL,
prijmeni_admin VARCHAR(50) NOT NULL,
prezdivka_admin VARCHAR(50) NOT NULL,
heslo_admin VARCHAR(25) NOT NULL
);

create table zabanovany_slova(
id INT NOT NULL PRIMARY KEY auto_increment,
slovo VARCHAR (50)
);

CREATE USER 'omega_admin'@'localhost' IDENTIFIED BY '123';

GRANT ALL PRIVILEGES ON *.* TO 'omega_admin'@'localhost';

FLUSH PRIVILEGES;

select * from admin1;

select * from autor;

select * from clanek;

select * from komentar;

select * from zabanovany_slova;

SELECT id FROM komentar WHERE clanek_id = '1';

SELECT id FROM autor WHERE prezdivka_autor = 'bartusek2';

SELECT ban FROM autor WHERE prezdivka_autor = 'bartusek2';

UPDATE autor SET ban = '1' WHERE prezdivka_autor = 'mirda';

SELECT ban FROM autor;

SELECT prezdivka_autor FROM autor WHERE ban = 1;

