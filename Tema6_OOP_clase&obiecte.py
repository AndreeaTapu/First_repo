# Exercitiul 1:

class Cerc():
    raza = None
    culoare = None

    def __init__(self, raza, culoare,):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Culoarea cercului este {self.culoare} iar raza cercului este: {self.raza} cm")

    def aria_cerc(self):
        self.aria = self.raza ** 2 * 3.14
        return self.aria

    def diametru_cerc(self):
        self.diametru_cerc = 2 * self.raza

    def circumferinta_cerc(self):
        self.circumferinta_cerc = 3.14 * self.diametru_cerc


Cerc1 = Cerc(12, "rosu")
Cerc2 = Cerc(7, "roz")
Cerc1.descrie_cerc()
Cerc2.descrie_cerc()
print(f"Cercul1 are culoarea {Cerc1.culoare}")
print(f"Cercul1 are raza: {Cerc1.raza} cm")
print(f"Cercul1 are aria: {Cerc1.aria_cerc()}")
print(f"Cercul2 are culoarea {Cerc2.culoare}")
print(f"Cercul2 are raza: {Cerc2.raza} cm")
print(f"Cercul2 are aria: {Cerc2.aria_cerc()}")

# Exercitiul 2:

class Dreptunghi():
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare,):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are o lungime de {self.lungime} cm, latime de {self.latime} cm si culoarea {self.culoare}")

    def aria_dreptunghi(self):
        self.aria = self.lungime * self.latime

    def perimetrul_dreptunghi(self):
        self.perimetrul = 2 * (self.lungime + self.latime)

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


Dreptunghi1 = Dreptunghi(9, 5, "alb")
Dreptunghi1.descrie_dreptunghi()
Dreptunghi1.schimba_culoare('albastru')
Dreptunghi1.descrie_dreptunghi()

# Exercitiul 3:

class Angajat():
    nume: None
    prenume: None
    salariu: None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f"Numele de familie al angajatului este {self.nume}. ", "\n"
              f"Prenumele angajatului este {self.prenume}. ", "\n"
              f"Angajatul are un salar de {self.salariu} lei"),

    def nume_complet(self):
        self.nume_complet = self.nume + " " + self.prenume

    def salariu_lunar(self):
        self.salariu_lunar = self.salariu

    def salariu_anual(self):
        self.salariu_anual = self.salariu * 12

    def marire_salariu(self):
        self.salariu = (5 * self.salariu)/100 + self.salariu
        print(f"Salariul actualizat este {self.salariu} lei")


Angajat1 = Angajat("Tapu", "Andreea", 5000)
Angajat1.descrie_angajat()
Angajat1.marire_salariu()

# Exercitiul 4:

class Cont():
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold += suma

    def creditare_cont(self, suma):
        self.sold -= suma


Cont1 = Cont("RO72xxxxaaaajjjjxxxx0000", "Tapu Andreea", 2000)
Cont1.afisare_sold()
Cont1.debitare_cont(3000)
Cont1.creditare_cont(1500)
Cont1.afisare_sold()
