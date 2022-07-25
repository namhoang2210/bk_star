DROP TABLE IF EXISTS category CASCADE;
CREATE TABLE category
(
  id bigserial NOT NULL,
  name text,
  active boolean DEFAULT TRUE,
  CONSTRAINT pkey_category PRIMARY KEY (id)
);