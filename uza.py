# -*- coding: utf-8 -*-
from random import randint


class Car():
    def __init__(self, znamka, model):
        self.znamka = znamka
        self.model = model

car1 = Car(znamka="Fiat", model="Punto")
car2 = Car(znamka="Renault", model="Senic")

cars = [car1, car2]

rnd = randint(0, 1)
print rnd

print(cars[rnd].model)
