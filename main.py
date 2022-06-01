import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname="bankapp", 
    user="bankappuser",
    password="1234",
    host="localhost")

with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""CREATE TABLE clients (id SERIAL PRIMARY KEY,
            firstName VARCHAR NOT NULL,
            lastName VARCHAR NOT NULL
            );
            """
            )
        cur.execute("""CREATE TABLE accounts (id SERIAL PRIMARY KEY,
            client_id INT NOT NULL,
            balance FLOAT NOT NULL,
            FOREIGN KEY (client_id)
                REFERENCES clients (id)
            );
            """
            )

