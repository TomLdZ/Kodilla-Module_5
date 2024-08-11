from faker import Faker
fake = Faker('en_US')

class BaseContact:
    def __init__(self, name, phone) ->str:
        self.name = name
        self.phone = phone
        self.email = name.replace(' ', '')  + '@gmail.com'

    def __str__(self):
        return f"Name: {self.name}, Phone no.: {self.phone}, Address e'mail: {self.email}"
    
    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.name}"
    
    @property
    def label_length(self):
        return len(self.name)

class BusinessContact(BaseContact):
    def __init__(self, name, phone, company, position) -> str:
        super().__init__(name, phone)
        self.company = company
        self.position = position 
        self.email = name.replace(' ', '')  + '@' +  self.company.lower().replace(' ', '') + '.com'

    def __str__(self):
        return f"Name: {self.name}, Phone no.: {self.phone}, Address e'mail: {self.email}, Company name: {self.company}, Position: {self.position}"




def create_contact(type: str, quantity: int):
    contact_list = []
    if isinstance(quantity, int):
        if type == "Base":
            for i in range(quantity):
                contact = BaseContact(fake.name(), fake.phone_number())
                contact_list.append(contact)  
        elif type == "Business":
            for i in range(quantity):
                contact = BusinessContact(fake.name(), fake.phone_number(), fake.company(), fake.job())
                contact_list.append(contact)
        else:
            print("Only types 'Base' and 'Business' are allowed")
        return contact_list
    else:
        print("Quantity must be an integer")

contact_list = create_contact("Business", 3)

for c in contact_list:
    print(c)










