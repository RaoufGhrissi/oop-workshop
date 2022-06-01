import psycopg2
import psycopg2.extras

class Client:
    def __init__(self, firstname, lastname, id=None):
        self.firstname = firstname
        self.lastname = lastname
        #set readonly property
        self.id = id

    def get_full_name(self):
        return self.firstname + self.lastname

    @classmethod
    def get_client_by_id(cls, id):
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")
        
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("SELECT * FROM clients WHERE id = %s;", (id,))
                    client = cur.fetchone()
                    return Client(**client)
                except Exception as e:
                    print(f"matnjmch tjib fama mochkla arja3 ghodwa: {e}")

    def __repr__(self):
        return f"client {self.id} {self.firstname} {self.lastname}"


