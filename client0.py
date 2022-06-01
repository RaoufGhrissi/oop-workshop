class Client:
    # a function inside a class is called method
    def get_full_name0(fn, ln):
        return fn + " " + ln

    def get_full_name(self):
        return self.firstName + self.lstnam

#Create instance of class client
client = Client()

#Assign attributes
client.id = 1
client.firstName = 'raouf'
client.lstnam = 'ghrissi'

print(client)

print(client.get_full_name())

#Create instance of class client
client2 = Client()

#Assign attributes
client2.id = 1
client2.name = 'raouf'
client2.lstnam = 'ghrissi'

print(client2)
print(client2.get_full_name())

#don't hard code !!!!!!