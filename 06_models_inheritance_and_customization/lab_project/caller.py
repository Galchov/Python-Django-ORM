import os
import django
from datetime import date, timedelta

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Animal, Mammal, Bird, Reptile, ZooKeeper, Veterinarian, ZooDisplayAnimal


##### Exercise 1 #####

# Animal.objects.create(name="Nemo", species="Clownfish", birth_date="2019-04-10", sound="Bubbles")
# Mammal.objects.create(name="Fluffy", species="Orangutan", birth_date="2018-02-10", sound="Chomps", fur_color="Reddish-brown")
# Bird.objects.create(name="Robby", species="American Robin", birth_date="2021-03-20", sound="Chirp", wing_span=28.50)
# Reptile.objects.create(name="Python", species="Ball Python", birth_date="2019-07-01", sound="Hiss", scale_type="Smooth")

# animals = Animal.objects.all()
# for a in animals:
#     print(f"{a.name}: {a.species}.")


##### Exercise 2 #####

# zookeeper = ZooKeeper.objects.create(first_name="Peter", last_name="Johnson", phone_number="0899524265", specialty="Mammals")
# mammal = Mammal.objects.get(name="Fluffy")
# zookeeper.managed_animals.add(mammal)
# veterinarian = Veterinarian.objects.create(first_name="Dr. Michael", last_name="Smith", phone_number="9876543210", license_number="VET12345")

# zookeeper_from_db = ZooKeeper.objects.first()
# print(f"{zookeeper_from_db.first_name} {zookeeper_from_db.last_name} is a ZooKeeper.")

# veterinarian_from_db = Veterinarian.objects.first()
# print(f"{veterinarian_from_db.first_name} {veterinarian_from_db.last_name} is a Veterinarian.")


##### Exercise 3 #####

# is_proxy = ZooDisplayAnimal._meta.proxy

# if is_proxy:
#     print("ZooDisplayAnimal is a proxy model.")
# else:
#     print("ZooDisplayAnimal is not a proxy model.")


##### Exercise 4 #####

# zookeeper = ZooKeeper(first_name="John", last_name="Doe", phone_number="0123456789", specialty="Fishes")
# zookeeper.full_clean()
# zookeeper.save()


##### Exercsie 5 #####

# all_animals_info = ZooDisplayAnimal.objects.all()
# for a in all_animals_info:
#     print(a.display_info())
#     print(a.is_endangered())


##### Exercise 6 #####

# lion_birth_date = date.today() - timedelta(days=731)
# lion = Mammal.objects.create(name="Simba", species="Lion", birth_date=lion_birth_date, sound="Roar", fur_color="Golden")
# print(f"The lion's age is {lion.age}.")

# snake_birth_date = date.today() - timedelta(days=30)
# snake = Reptile.objects.create(name="Kaa", species="Python", birth_date=snake_birth_date, sound="Hiss", scale_type="Scales")
# print(f"The snake's age is {snake.age}.")


##### Exercise 7 #####

# v1 = Veterinarian.objects.create(first_name="John", last_name="Doe", phone_number="0896625120", license_number="VET123", availability=False)
# print(v1.availability)
# v2 = Veterinarian.objects.create(first_name="Alice", last_name="Johnson", phone_number="0896529728", license_number="VET789")
# print(v2.availability)
