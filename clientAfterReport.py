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

    #no relation with the class
    # ken je 3ana wakt nasn3ou class connect w nhezouha l bara
    # 9lil fn trawhom yesta3mlouha
    @staticmethod
    def __connect():
        return psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")

    @classmethod
    #matekhouch instance ama teb3a l class
    def get_client_by_id(cls, id):
        conn = cls.connect()
        
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

b = Client.get_client_by_id(11)
#Abstration
# we can call it inside the class but not outside
print(b.__connect())
