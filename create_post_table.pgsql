CREATE TABLE IF NOT EXISTS dummyapi.post(
id            VARCHAR(100) PRIMARY KEY,
image         VARCHAR(255),
likes         INT,
tags          TEXT[],
text          TEXT,
publishDate   TIMESTAMP WITH TIME ZONE,
owner         VARCHAR(100),
FOREIGN KEY(owner) REFERENCES dummyapi.user
);