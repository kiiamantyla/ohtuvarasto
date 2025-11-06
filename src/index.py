
from varasto import Varasto


def tulosta_varastotilanteet(mehua, olutta, otsikko):
    print(otsikko)
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def tulosta_olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testaa_oluen_toiminnot(olutta):
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def testaa_olutvarasto(olutta):
    tulosta_olut_getterit(olutta)
    testaa_oluen_toiminnot(olutta)

def testaa_mehun_lisays(mehua):
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")

def testaa_mehun_otto(mehua):
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testaa_mehun_virhetilanteet(mehua):
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def testaa_mehuvarasto(mehua):
    print("Mehu setterit:")
    testaa_mehun_lisays(mehua)
    testaa_mehun_otto(mehua)
    testaa_mehun_virhetilanteet(mehua)

def testaa_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0)")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_varastotilanteet(mehua, olutta, "Luonnin jälkeen:")
    testaa_olutvarasto(olutta)
    testaa_mehuvarasto(mehua)
    testaa_virhetilanteet()


if __name__ == "__main__":
    main()
