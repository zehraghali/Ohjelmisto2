import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara
def luo_autot():
    autot = []
    for i in range(1, 11):
        rekisteritunnus = "ABC-" + str(i)
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))
    return autot
def tulosta_autot(autot):
    print("{:<10} {:<15} {:<15} {:<15}".format("Rek. tun.", "Huippunopeus", "Nopeus", "Kuljettu matka"))
    for auto in autot:
        print("{:<10} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka))
def kilpailu():
    autot = luo_autot()
    while True:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
        for auto in autot:
            auto.kulje(1)
        voittaja = None
        for auto in autot:
            if auto.kuljettu_matka >= 10000:
                voittaja = auto
                break
          if voittaja:
              break
    tulosta_autot(autot)
    # Pääohjelma
uusi_auto = Auto("ABC-123", 142)
print("{:<15} {:<15} {:<15} {:<15}".format("Rek. tun.", "Huippunopeus", "Nopeus", "Kuljettu matka"))
print("{:<15} {:<15} {:<15} {:<15}".format(uusi_auto.rekisteritunnus, uusi_auto.huippunopeus, uusi_auto.nopeus, uusi_auto.kuljettu_matka))
uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)
print("Nopeus: {}".format(uusi_auto.nopeus))
uusi_auto.kiihdyta(-200)
print("Nopeus hätäjarrutuksen jälkeen: {}".format(uusi_auto.nopeus))
