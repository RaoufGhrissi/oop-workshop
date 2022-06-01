class Client:
    bank = "bank A"
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        print(f"mar7ba {self.get_full_name()}")   

    def get_full_name(self):
        return self.firstName + " " + self.lastName

    def __repr__(self):
        return f"client {self.firstName} {self.lastName}"

client1 = Client("raouf", "ghrissi")

print(client1)
#print(client1.firstName, client1.lastName)


