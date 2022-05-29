from http import client
import psycopg2
import psycopg2.extras
from client import Client
#heritage, inheritence
class ClientReport(Client):
    def __init__(self, firstname, lastname, total_balance, id):
        super().__init__(firstname, lastname, id)
        self.total_balance = total_balance
    
    @staticmethod
    def __connect():
        return psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")

    @classmethod                
    def get_client_by_id(cls, id):
        
        conn = cls.connect()
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""SELECT c.id AS id,
                        c.firstname AS firstname,
                        c.lastname AS lastName,
                        SUM(a.balance) AS total_balance
                    FROM clients AS c
                    JOIN accounts AS a
                        ON c.id = a.client_id
                    WHERE c.id = %s
                    GROUP BY c.id, c.firstname, c.lastname;                   
                    """, (id,))
                    client = cur.fetchone()
                    if not client:
                        return None
                    return ClientReport(**client)
                except Exception as e:
                    print(f"matnjmch tjib fama mochkla arja3 ghodwa: {e}")
                    #khabi e fin mat7eb
    def __repr__(self) -> str:
        return super().__repr__() + " **** " + (str)(self.total_balance)

    def ab(self):
        print('aslema')

#create instance of class Client

a = ClientReport("raouf", "ghrissi", 5, 6)
print(a)
print(a.__connect())

"""client = ClientReport.get_client_by_id(11)
print(client.id)
print(client)"""

#encapsultation : getter w setter

#abstraction


