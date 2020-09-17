USE $MYSQL_DATABASE;

DROP TABLE IF EXISTS challenge1;
CREATE TABLE challenge1 (
	id INT AUTO_INCREMENT PRIMARY KEY,
	author VARCHAR(256) NOT NULL,
	content VARCHAR(256),
	post_date DATETIME NOT NULL
);

DROP TABLE IF EXISTS secret_table_XaFqEhxVY3U;
CREATE TABLE secret_table_XaFqEhxVY3U (
	id INT AUTO_INCREMENT PRIMARY KEY,
	filler VARCHAR(256) NOT NULL,
	junk VARCHAR(256) NOT NULL,
	flag VARCHAR(256) NOT NULL

);

DROP USER IF EXISTS '$CHALLENGE1_USER';
CREATE USER '$CHALLENGE1_USER'@'%' IDENTIFIED BY '$CHALLENGE1_USER_PASS';

GRANT USAGE,SELECT ON ${MYSQL_DATABASE}.challenge1 TO ${CHALLENGE1_USER};
GRANT USAGE,SELECT ON ${MYSQL_DATABASE}.secret_table_XaFqEhxVY3U TO ${CHALLENGE1_USER};

INSERT INTO challenge1 (author, content, post_date) VALUES
	("test", "However, an abundance of appropriations concerning cultural precapitalist theory exist. Debord promotes the use of postcultural textual theory to analyse and modify society.", '1977-02-15 14:57:18'),
	("admin", "Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative approaches to corporate strategy foster collaborative thinking to further the overall value proposition.", '1981-10-06 07:53:02'),
	("united", "A Corona Extra conquers a lager. When an Ellis Island IPA is feline, the Hops Alligator Ale has a change of heart about a muddy Heineken.", '2008-08-04 21:51:15'),
	("admin", "Run it up the flag pole do i have consent to record this meeting minimize backwards overflow big boy pants but what's our go to market strategy? It's not hard guys i also believe it's important for every member to be involved and invested in our company.", '2018-05-14 08:43:21'),
	("admin", "Scrum project infographic accelerator infrastructure social media validation. Gen-z MVP agile development. Rockstar churn rate crowdfunding ownership. Network effects partner network monetization non-disclosure agreement investor traction social proof.", '1972-07-22 10:13:22'),
	("test", "But the subject is interpolated into a postmaterialist nationalism that includes language as a paradox. Many narratives concerning the role of the participant as poet may be discovered.", '1995-04-16 09:00:47'),
	("united", "The Citra Ninja caricatures some grizzly beer. Furthermore, a dude beams with joy, and a dude sells a Mango Beer related to a Busch to a grizzly beer over a burglar ale.", '1994-04-20 20:33:13');

INSERT INTO secret_table_XaFqEhxVY3U (filler, junk, flag) VALUES
	("FLAGgflagGLAFFLagFLGA", "DRAPEAUDdraapeueDreapeuuDRapuae", "FLAG-And_in_the_db_UNION_them_l88VnAUrYEI"),
	("FANionFnaionFanionFnAIOnFAnion", "EtendARdEtaentdardEtandftar", "Presque!!");
