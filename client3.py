import psycopg2
import psycopg2.extras

class Client:
    def __init__(self, firstName, lastName):
        assert firstName, "first name is required"
        assert isinstance(firstName, str), "first name should be a string"
        assert lastName, "last name is required"

        self.firstName = firstName
        self.lastName = lastName
        
        #rod belek 9a3da tzid fih martin kif tzid w kif tgety 
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")
        
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO clients (firstName, lastName) VALUES(%s, %s)", (self.firstName, self.lastName))
                    print(f"mar7ba {self.get_full_name()} added fil base")
                except Exception as e:
                    print(f"matnjmch tzid fama mochkla arja3 ghodwa: {e}")

    def get_full_name(self):
        return self.firstName + self.lastName

    def __repr__(self):
        return f"client {self.firstName} {self.lastName}"

client1 = Client(30, 10)
#client1 = Client("raouf", "ghrissi")
print(client1.firstName, client1.lastName)

