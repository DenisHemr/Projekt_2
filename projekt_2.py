"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Denis Hemr
email: dennis.hemmr@gmail.com
discord: Denis H.#3249
"""


pozdrav = """
Vítejte v piškvorkách
========================================
Pravidla hry:
-------------
Každý hráč může na hrací plochu 3x3
umístit jeden znak(kámen)na každý svůj tah.
VÍTĚZEM je ten, kdo dokáže umístit tři znaky(kameny)
v řadě:
-------------
* horizontalní
* vertikální
* diagonální
========================================
Začněme hru!

"""


plocha = [" " for x in range(9)]

print(pozdrav)


def print_plocha() -> None:
    """
    Funkce:
    -------
    Funkce vypíše hrací plochu 3x3,
    kde každý prvek na ploše je reprezentován jako
    buď prázdný řetězec (" "), nebo znak "X" nebo znak "O".

    Parametry:
    -----------
    Žádné parametry.

    """
    rada1 = "| {} | {} | {} |".format(plocha[0], plocha[1], plocha[2])
    rada2 = "| {} | {} | {} |".format(plocha[3], plocha[4], plocha[5])
    rada3 = "| {} | {} | {} |".format(plocha[6], plocha[7], plocha[8])

    print()
    print(rada1)
    print(rada2)
    print(rada3)
    print()


def pohyb_hrace(znak) -> None:
    """
    Funkce:
    -------
    Pohyb hráče na hrací ploše 3x3

    Parametry:
    ----------
    znak : str
    Označení hráče ("X" nebo "O")

    """
    if znak == "X":
        cislo = 1
    elif znak == "O":
        cislo = 2

    print("Na tahu je hráč {}".format(cislo))

    while True:
        volba = input("Zadej pohyb (1-9): ").strip()
        if volba.isdigit() and int(volba) in range(1, 10):
            volba = int(volba)
            if plocha[volba - 1] == " ":
                plocha[volba - 1] = znak
                break
            else:
                print("Toto pole je obsazené!")
        else:
            print("Neplatný vstup, zadej číslo od 1 do 9!")


def vyhra(znak) -> bool:
    """
    Funkce:
    -------
    Kontroluje, zda hráč se zadaným symbolem zvítězil na hrací ploše 3x3.

    Parametry:
    ----------
    znak : str
    Symbol hráče ("X" nebo "O")

    Návratová hodnota:
    -------------------
    bool
    True, pokud hráč zvítězil, jinak False.

    """
    if (
        (plocha[0] == znak and plocha[1] == znak and plocha[2] == znak)
        or (plocha[3] == znak and plocha[4] == znak and plocha[5] == znak)
        or (plocha[6] == znak and plocha[7] == znak and plocha[8] == znak)
        or (plocha[0] == znak and plocha[3] == znak and plocha[6] == znak)
        or (plocha[1] == znak and plocha[4] == znak and plocha[7] == znak)
        or (plocha[2] == znak and plocha[5] == znak and plocha[8] == znak)
        or (plocha[0] == znak and plocha[4] == znak and plocha[8] == znak)
        or (plocha[2] == znak and plocha[4] == znak and plocha[6] == znak)
    ):
        return True
    else:
        return False


def remiza() -> bool:
    """
    Funkce:
    -------
    Kontrola, zda je na hrací ploše 3x3 remíza.

    Vrací:
    ------
    bool
    True, pokud je na hrací ploše 3x3 remíza, jinak False.

    """
    if " " not in plocha:
        return True
    else:
        return False


while True:
    print_plocha()
    pohyb_hrace("X")
    print_plocha()
    if vyhra("X"):
        print("X Vyhrává! Gratuluji!")
        break
    elif remiza():
        print("Remíza!")
        break
    pohyb_hrace("O")
    if vyhra("O"):
        print_plocha()
        print("O Vyhrává! Gratuluji!")
        break
    elif remiza():
        print("Remíza!")
        break
