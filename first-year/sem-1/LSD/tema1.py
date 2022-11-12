'''
Exercițiul 9: Cerc
Implementați o funcție în Python care primește ca parametru raza unui cerc
și returnează atât lungimea discului cât și aria acestuia.
'''

def cerc(raza):
    aria = 3.14 * raza * raza
    disc = 2 * 3.14 * raza
    x = "Lungimea discului este {} \nAria cercului este {}"
    return x.format(disc, aria)

'''
Exercițiul 10: Numărul de zile
Implementați o funcție în Python care primește ca parametri doi ani 
(numere întregi) și returnează numărul de zile dintre aceștia 
(Puteți utiliza funcția implementată la exercițiul 4).
Nota: Nu este permisa utilizarea modulului datetime sau a oricărui alt 
modul similar.
'''

def an_bisect(an):
    if an % 4 == 0:
        if an % 100 == 0:
            if an % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def zile(an1, an2):
    normali = an2 - an1 + 1
    if an_bisect(an1) != True:
        an1 = an1 + 4 - an1 % 4
    if an_bisect(an2) != True:
        an2 = an2 - an2 % 4
    bisecti =  (an2 - an1) / 4 + 1
    normali = normali - bisecti
    nr = bisecti * 366 + normali * 365
    nr = int(nr)
    x = "Intre cei doi ani sunt {} zile"
    return x.format(nr)

# MAIN

if __name__ == "__main__":

    #apel functie exercitiul 9

    raza = input('Introduceti valoarea razei cercului: ')
    raza = float(raza)
    print (cerc(raza))

    # apel functie exercitiul 10

    an1 = input('Introduceti primul an: ')
    an2 = input('Introduceti al doilea an: ')
    an1 = int(an1)
    an2 = int(an2)
    print (zile(an1, an2))
