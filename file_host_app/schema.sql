DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS file_base;
DROP TABLE IF EXISTS user_links;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE file_base (
  file_id INTEGER PRIMARY KEY AUTOINCREMENT,
  original_name	VARCHAR(50),
  user_id INTEGER NOT NULL,
  permission_of_file VARCHAR(20) NOT NULL default 'private',	
  file_path VARCHAR(100),
  count_download	INTEGER	,
  FOREIGN KEY (user_id ) REFERENCES user
);

CREATE TABLE user_links( 
    user_id INTEGER NOT NULL,
    fileid_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, fileid_id),
    FOREIGN KEY (user_id ) REFERENCES user,
    FOREIGN KEY (fileid_id ) REFERENCES file_base
);

INSERT INTO user (username, password)
VALUES ('admin', 'pbkdf2:sha256:260000$9p7uOiDRCBpC9ydf$66120f235003a0fe4c6e05384cd991b766ebe5bfc0a61bf5b3cbe59a38e02f7f');

INSERT INTO file_base (original_name, user_id, permission_of_file)
VALUES ('HELLO', 1, 'pablic');
INSERT INTO file_base (original_name, user_id)
VALUES ('qqerer', 1);
INSERT INTO file_base (original_name, user_id)
VALUES ('dfr', 1);

INSERT INTO user_links(user_id,fileid_id)
VALUES (1,1);
INSERT INTO user_links(user_id,fileid_id)
VALUES (1,2);
INSERT INTO user_links(user_id,fileid_id)
VALUES (1,3);



