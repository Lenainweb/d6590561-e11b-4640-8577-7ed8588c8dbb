INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO file_base (original_name, user_id, permission_of_file, file_path, count_download)
VALUES ('HELLO', 1, 'pablic', 'fgfh', 5);
INSERT INTO file_base (original_name, user_id, permission_of_file, file_path, count_download)
VALUES ('qqerer', 1, 'pablic', 'fgfh', 3);
INSERT INTO file_base (original_name, user_id, permission_of_file, file_path, count_download)
VALUES ('dfr', 1, 'pablic', 'fgfh', 1);

INSERT INTO user_links(user_id,fileid_id)
VALUES (1,1);
INSERT INTO user_links(user_id,fileid_id)
VALUES (1,2);
INSERT INTO user_links(user_id,fileid_id)
VALUES (1,3);
INSERT INTO user_links(user_id,fileid_id)
VALUES (3,2);