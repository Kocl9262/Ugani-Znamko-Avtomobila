class Car():
    def __init__(self, znamka, model):
        self.znamka = znamka
        self.model = model

car1 = Car(znamka="Fiat", model="Punto")
car2 = Car(znamka="Renault", model="Senic")
car3 = Car(znamka="Kia", model="Soul")

cars = [car1, car2, car3]