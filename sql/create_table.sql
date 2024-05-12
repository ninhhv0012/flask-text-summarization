CREATE TABLE summarization (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  text TEXT,
  summarization TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

INSERT INTO summarization (text, summarization)
VALUES ('This is some text to be summarized.', 'This is a concise summary.');
