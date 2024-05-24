#!/usr/bin/env python3

class Person:
    '''creates persons with names'''

    def __init__(self, name):
        '''initialize attributes'''
        self.name = name


    
person_1 = Person("Ibra")

print(person_1.name)
