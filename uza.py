# -*- coding: utf-8 -*-
from random import randint
from avtomobili import cars

vprasanje = "da"

while vprasanje != "ne":
    vprasanje = raw_input("Želiš preveriti kako dobro poznaš avtomobile? (da/ne): ")

    if vprasanje == "da":
        rnd = randint(0, len(cars) - 1)

        print("Znamka avtomobila " + cars[rnd].model + " je: ")
        odgovor = raw_input(">: ")

        if odgovor == cars[rnd].znamka:
            print("Pravilen odgovor!")

        else:
            print("Napačen odgovor")
            print("Pravilen odgovor je " + cars[rnd].znamka)

    else:
        print("----------------------------------------------------")
        print("Odločil si se, da ne želiš več igrati")
        break
