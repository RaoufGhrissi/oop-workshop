import psycopg2
import psycopg2.extras

# Client class manesta3mlouha ken bech njibou mel base 
#add tsir b class okhra ok
class Client: #Client / ClientInDb / BaseClient
    def __init__(self, firstname, lastname):
        assert firstname, "first name lezem ykoun mch none"
        assert isinstance(lastname, str), "first name lezem ykoun int"
        self.firstname = firstname
        self.lastname = lastname

    def add_user_in_db(self):
        conn = psycopg2.connect(dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost")

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO clients (firstName, lastName) VALUES(%s, %s)", (self.firstname, self.lastname))
                except Exception as e:
                    print("fama mochkla jareb ba3ed")
                    print(e)
    
    def get_full_name(self):
        return self.firstname + "/" + self.lastname

    def __repr__(self) -> str:
        return self.firstname + " - " + self.lastname
