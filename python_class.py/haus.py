## Komposition
# Hasu besteht aus vielen räumen 
# räume können ohne haus nicht existieren
class Raum:
    def __init__(self, groesse):
        self.groesse = groesse

    def __str__(self):
        return f"Raum mit {self.groesse} Quadratmeter"

# Klasse Haus (one-site)
class Haus:
    def __init__(self, farbe, hoehe, flaeche, adresse, raeume):
        self.farbe = farbe
        self.hoehe = hoehe
        self.flaeche = flaeche
        self.adresse = adresse
        self.raeume = [Raum(20), Raum(40)]# koomposition

    def __str__(self):
        raeume_string = ", ".join(str(raum) for raum in self.raeume)
        return f"Haus an der {self.adresse} mit nit den Räumen {raeume_string}"

## Verwendung
# raeume = [Raum(20), Raum(40)]
haus = Haus("gelb", 12, 200, "Neue Strasse 1",) 
print(haus)