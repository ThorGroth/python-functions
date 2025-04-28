class Buch:
    def __init__(self, titel, autor, seiten):
        self.titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesene_seiten = 0

    def info(self):
        print(f"{self.titel} von {self.autor} - {self.seiten} Seiten")

    def lesezeit_schaetzen(self, seiten_pro_stunde):
        if seiten_pro_stunde > 0:
            stunden = self.seiten / seiten_pro_stunde
            return round(stunden, 1)
        else:
            print("Seiten pro Stunde muss größer als 0 sein.")
            return None

    def lesen(self, seiten):
        if seiten <= 0:
            print("Du musst erst mal ein paar seiten lesen!")
        elif self.gelesene_seiten + seiten > self.seiten:
            print("Du hast über das buch hinaus gelesen!.")
        else:
            self.gelesene_seiten += seiten
            print(f"Du hast {seiten} Seiten gelesen. Insgesamt gelesen: {self.gelesene_seiten}/{self.seiten} Seiten.")

origin = Buch("Origin", "Dan Brown", 672)
origin.info()
print(f"Geschätzte Lesezeit bei 60 Seiten/Stunde: {origin.lesezeit_schaetzen(60)} Stunden")
origin.lesen(100)
origin.lesen(600)