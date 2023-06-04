#https://faker.readthedocs.io/en/master/index.html

from faker import Faker



fake = Faker(locale="fr_FR")



for _ in range(10) :
    print(fake.job())