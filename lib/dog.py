#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = "Fido", breed = "Mastiff"):
        if isinstance(name, str) and 1 <= len(name) <= 25 and breed in APPROVED_BREEDS:
            self._name = name
            self._breed = breed
        elif name == "" or isinstance(name, str) == False or len(name) < 1 or len(name) >25: 
            print("Name must be string between 1 and 25 characters.")   
        else:
            print("Breed must be in list of approved breeds.")   

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)  

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)                       
            

dog = Dog("puppy")  
dog2 = Dog("")
dog3 = Dog("tdwhlfhlewruugrghltiho5yjklrnvk4tbojthkmnblkpgkgm") 


