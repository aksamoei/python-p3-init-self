#!/usr/bin/env python3

class Dog:
    '''creates dog class'''
    def __init__(self, name, breed="Mutt"):
        '''initializing attributes'''
        self.name = name
        self.breed = breed



your_dog = Dog("Casey")
my_dog = Dog("Stoner", "Bosco")

print(f"{your_dog.name} belongs to the breed {your_dog.breed}")
print(f"{my_dog.name} belongs to the breed {my_dog.breed}")