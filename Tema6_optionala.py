# Exercitiul 1:

from tabulate import tabulate
from datetime import date

class Factura():
    seria = "PYT"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_schimbata):
        self.cantitate = cantitate_schimbata

    def schimba_pretul(self, pret_schimbat):
        self.pret_buc = pret_schimbat

    def schimba_nume_produs(self, nume_produs_schimbat):
        self.nume_produs = nume_produs_schimbat

    def genereaza_factura(self):
        print(f"Factura seria {self.seria} numar {self.numar}")
        today = date.today()
        print("Data facturii este: ", today)
        date_factura = [["Produs", "Cantitate", "Pret_bucata", "Total"], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc]]
        print(tabulate(date_factura, headers='firstrow'))

Produs1 = Factura(111, "Ciocolata_Milka", 10, 6)
Produs2 = Factura(111, "Ciocolata_Kandia", 15, 8)
Produs1.schimba_cantitatea(13)
Produs1.schimba_pretul(7)
Produs1.schimba_nume_produs("Ciocolata_Milka_cu_lapte")
Produs1.genereaza_factura()

print("-----------------------")

# Exercitiul 2:

class Masina():
    marca = "Audi"
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = "Gri"
    culori_disponibile = {"alba", "rosie", "neagra", "galbena", "verde", "albastra"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie_masina(self):
        print(f"Masina este marca: {self.marca}", "\n"
              f"Modelul masinii este: {self.model}", "\n"
              f"Viteza maxima a masinii este: {self.viteza_maxima}", "\n"
              f"Viteza actuala a masinii este: {self.viteza_actuala}", "\n"
              f"Masina are culoarea: {self.culoare}", "\n"
              f"Masina este inmatriculata: {self.inmatriculata}")

    def inmatriculare_masina(self):
        self.inmatriculata = True

    def vopseste_masina(self, culoare):
        self.culoare = culoare
        if culoare in self.culori_disponibile:
            print(f"Masina se va vopsi in culoarea {culoare}")
        else:
            print("Culoarea nu este disponibila")

    def accelereaza_masina(self, viteza):
        if viteza < 0:
            print("Eroare viteza")
        elif viteza > self.viteza_maxima:
            print("Stop...ai depasit viteza maxima!!!")

    def franeaza_masina(self):
        while self.viteza_maxima > 0:
            print("Masina este in miscare")
            self.viteza_maxima = self.viteza_maxima - 20
            if self.viteza_maxima == 0:
                print("Masina s-a oprit. Are viteza zero")

Masina1 = Masina("A4", 220)
Masina1.descrie_masina()
Masina1.inmatriculare_masina()
print(Masina1.inmatriculata)
Masina1.vopseste_masina("albastra")
Masina1.accelereaza_masina(230)
Masina1.franeaza_masina()

# Exercitiul 3:

class TodoList():
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        del self.todo[nume]

    def afiseaza_todo_list(self):
        print(self.todo.keys())


    # def afiseaza_detalii_suplimentare(self, nume_task):





