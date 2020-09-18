CREATE DATABASE ettic CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;;
CREATE TABLE ettic.students (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL
);

INSERT INTO ettic.students(firstname, lastname) VALUES ("Donatien ", "Hugues");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Florian ", "Melisande");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Barbe ", "Yves");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Winoc ", "Berthe");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Mathieu ", "Thomas");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Melina ", "Nicolas");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Benjamine ", "Martine");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Yannic ", "Adelaide");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Capucine ", "Bertrand");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Eustache ", "Marcellette");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Bertrand ", "Camelia");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Gigi ", "Laetitia");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Liliane ", "Maia");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Joseph ", "Dieudonnee");
INSERT INTO ettic.students(firstname, lastname) VALUES ("Emile ", "Gilberte");

CREATE TABLE ettic.a_table_name_you_wont_guess (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    this_might_be_a_flag VARCHAR(300) NOT NULL
);

INSERT INTO ettic.a_table_name_you_wont_guess(this_might_be_a_flag) VALUES ("FLAG-5d5d51067ebb90fb948e97f1824739cc");

CREATE USER 'ettic'@'localhost' IDENTIFIED BY 'ettic';
GRANT ALL PRIVILEGES ON ettic.* TO 'ettic'@'localhost';