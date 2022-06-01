import psycopg2
import psycopg2.extras

class ClientReport:
    def __init__(self, firstname, lastname, total_balance, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.total_balance = total_balance
        self.__id = id

    @property
    def id(self):
        return self.__id

    def get_full_name(self):
        return self.firstname + self.lastname

    def get_result(self):
        return f"{self.firstname} 3andou {self.total_balance}"

    @classmethod
    def get_client_by_id(cls, id):
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")
        
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""
                    SELECT c.id AS id,
                        c.firstname AS firstname,
                        c.lastname AS lastname,
                        SUM(a.balance) AS total_balance
                    FROM clients AS c
                    JOIN accounts AS a
                        ON c.id = a.client_id                     
                    WHERE c.id = %s
                    GROUP BY c.id, c.firstname, c.lastname;
                    """, (id,))

                    client = cur.fetchone()
                    return ClientReport(**client)
                except Exception as e:
                    print(f"matnjmch tjib fama mochkla arja3 ghodwa: {e}")

    def __repr__(self):
        return f"client {self.id} {self.firstname} {self.lastname} {self.total_balance}"

a = ClientReport.get_client_by_id(11)
print(a)

