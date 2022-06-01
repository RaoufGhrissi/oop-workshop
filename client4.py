import psycopg2
import psycopg2.extras

class Client:
    def __init__(self, firstname, lastname, id=None):
        self.firstname = firstname
        self.lastname = lastname
        #set readonly property
        self.__id = id
        
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")
        
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO clients (firstname, lastname) VALUES(%s, %s)", (self.firstname, self.lastname))
                    print(f"mar7ba {self.get_full_name()} added fil base")
                except Exception as e:
                    print(f"matnjmch tzid fama mochkla arja3 ghodwa: {e}")
                    #khabi e fin mat7eb
    @property
    def id(self):
        #return self.id
        return self.__id

    def get_full_name(self):
        return self.firstname + self.lastname

    @classmethod
    #mahich related l instance b sifa khasa mel bel class lkol
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
                    #khabi e fin mat7eb

    def __repr__(self):
        return f"client {self.id} {self.firstname} {self.lastname}"

#client1 = Client("coding", "betounsi")
#print(client1.firstName, client1.lastName)

a = Client.get_client_by_id(11)
print(a)
print(a.id)
print(type(a))
print(a)
print(type(a))
#a.id = 5
print(a.id)
#print(a.__id)
print(type(a))
#encapsulation, enek thot des restrictions
#getter w setter