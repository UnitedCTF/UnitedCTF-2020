USE $MYSQL_DATABASE;

DROP TABLE IF EXISTS challenge0;
CREATE TABLE challenge0 (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(256) NOT NULL,
	password VARCHAR(256) NOT NULL
);

DROP USER IF EXISTS '$CHALLENGE0_USER';
CREATE USER '$CHALLENGE0_USER'@'%' IDENTIFIED BY '$CHALLENGE0_USER_PASS';

GRANT USAGE,SELECT ON ${MYSQL_DATABASE}.challenge0 TO ${CHALLENGE0_USER};

INSERT INTO challenge0 (username,password) VALUES
	("test", "PleaseDon'tStorePasswordInCleartextLikeThis"),
	("admin", "SeriouslyNeverDoThis,It'sBad"),
	("united", "HashPasswordsWithAProperCryptographicHashAndASalt"),
	("You won't be able to guess my name BSh8dn_fdHs", "The flag: FLAG-One_SELECT_to_bring_them_all_YbHKhnADUbc");
