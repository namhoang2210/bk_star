DROP TABLE IF EXISTS category CASCADE;
CREATE TABLE category
(
  id bigserial NOT NULL,
  name text,
  description text,
  image text,
  active boolean DEFAULT TRUE,
  CONSTRAINT pkey_category PRIMARY KEY (id)
);

DROP TABLE IF EXISTS post CASCADE;
CREATE TABLE post
(
  id bigserial NOT NULL,
  category_id bigint,
  title text,
  content text,
  image text,
  active boolean DEFAULT TRUE,
  CONSTRAINT pkey_post PRIMARY KEY (id)
);