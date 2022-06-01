class Client:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        print(f"mar7ba {self.get_full_name()}")   

    def get_full_name(self):
        return self.firstName + " " + self.lastName

client1 = Client("raouf", "ghrissi")
print(client1.get_full_name())

print(client1)
print(type(client1))
#<class '__main__.Client'>

a = int('1111',2)
b = int(15)
print(a)
print(type(a))
print(b)
print(type(b))

c = str("raouf")
print(type(c))
print(c.upper())

#f12 on str and upper
#tekhou haja esmha self ama ena ma3aditelha chay 
#c instance heya tet3ada wa7adha comme premier param
#self convention ysamiw beha les devs lkol tnajem tbadalha ama famech aleh 
#argument hedha obligatoire w les fcts west class yetsawem methode
#donc 3ana attributes w methods

