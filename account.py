import psycopg2
import psycopg2.extras
from client import Client

class Account:
    def __init__(self, client_id: int, balance: float, id: int = None):
        assert isinstance(client_id, int), 'client_id should be int'
        assert isinstance(balance, float), 'balance should be float'
        client = Client.get_client_by_id(client_id)
        assert client, 'client_id is not present in table "clients"'

        self.client_id = client_id
        self.__balance = balance
        self.id = id

        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO accounts (client_id, balance) VALUES(%s, %s)", (self.client_id, self.balance))
                except Exception as e:
                    print(f"matnjmch tzid fama mochkla arja3 ghodwa: {e}")

    #getter
    @property
    def balance(self):
        return self.__balance
    
    #setter
    @balance.setter
    def balance(self, value):
        self.__balance = value

    #encapsulation

a = Account(11, 25.00)
print(a.balance)
a.balance = 80
print(a.balance)