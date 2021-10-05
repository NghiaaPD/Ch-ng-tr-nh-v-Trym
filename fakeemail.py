from faker import Faker
from random import*

for _ in range(50):
    
    first_name =Faker().first_name()
    last_name =Faker().last_name()

    #dot = ["",".",","]
    #random_dot = choice(dot)
    email_address = ["gmail.com","yahoo.com","hotmail.com","outlook.com"]
    random_email_address = choice(email_address)
    number = [i for i in range(0,100)]
    random_number = choice(number)
    number_1 = randint(0,10)

    email = first_name.lower() + str(number_1) + last_name.lower()+ str(random_number) + "@" + random_email_address


    print(email)