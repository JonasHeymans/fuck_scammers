from faker import Faker
fake = Faker(['nl_BE'])
import random

tussenzetsels = ['.','_','-','']

def generate_voornaam():
    return fake.first_name()

def generate_achternaam():
    return fake.last_name()

def generate_email(voornaam,achternaam):
    tussenzetsels = ['.', '_', '-', '']
    return voornaam + random.choice(tussenzetsels) + achternaam + "@" + fake.free_email_domain()

def generate_phone():
    return '04' + str(random.randrange(0, 99999999, 8))

def generate_password():
    passwords = [fake.first_name(), fake.last_name(),fake.password(length=8), fake.catch_phrase(), fake.company()]
    return random.choice(passwords)

def generate_origin_id():
    return str(1664) + str(random.randint(99,999))

def genereate_id():
    return str(612) + str(random.randint(99,999))

