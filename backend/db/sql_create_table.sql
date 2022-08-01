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

CREATE TABLE post
(
  id bigserial NOT NULL,
  category_id integer,
  title text,
  content text,
  image text,
  active boolean DEFAULT TRUE,
  CONSTRAINT pkey_category PRIMARY KEY (id)
);