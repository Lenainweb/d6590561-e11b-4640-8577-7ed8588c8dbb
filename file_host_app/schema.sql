DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS FILE_base;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE file_base (
  file_id INTEGER PRIMARY KEY AUTOINCREMENT,
  original_name	VARCHAR(50),
  permission_of_file VARCHAR(20) NOT NULL default 'private',	
  file_path VARCHAR(100),
  count_download	INTEGER	,
  file_by_link INTEGER 
);





