import psycopg2
import psycopg2.extras

from client import Client

# Client class manesta3mlouha ken bech njibou mel base 
#add tsir b class okhra ok 

class ClientOut(Client):
    def __init__(self, firstname, lastname, id = None):
        super().__init__(firstname, lastname)
        self.id = id
    
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
                    if not client:
                        return None
                    return ClientOut(**client)
                except Exception as e:
                    print(f"matnjmch tjib fama mochkla arja3 ghodwa: {e}")
                    #khabi e fin mat7eb

    def __repr__(self) -> str:
        return super().__repr__() + "  id = " + (str)(self.id)
