from client4 import Client
import psycopg2
import psycopg2.extras

class Account:
    def __init__(self, client_id: int, balance: int, id: int = None):
        assert isinstance(client_id, int), 'client_id should be int'

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

    @property
    def balance(self):
        return self.__balance

#encapsulation again
    #setter
    @balance.setter
    def balance(self, value):
        self.__balance = value
#a = Account(11, 80)
#a = Account(11, 130)
a = Account(8, 130)
print(a.balance)
a.balance = 40
print(a.balance)