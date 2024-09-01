# Napišite funkciju koja provjerava da li je
# rijec (text) palindrom.
# Palindrom je rijec koja se cita isto s lijeva na desno,
# i s desna na lijevo (npr. "kisik").

# Funkcija se mora zvati ⁠ palindrom ⁠.
# Funkcija prima rijec kao argument koji mora biti tipa string (str).
# Funkcija vraća True ili False (bool).
# Ako je rijec palindrom funkcija vraca True, inace False.
# Ako ulazni parametar nije tipa str, funkcija mora vratiti False.
# Glavna funkcija (main) ispituje ispravnost rada funkcije,
# taj dio programskog koda ne treba mijenjati.


def palindrom(rijec):
    if not isinstance(rijec, str):
        return False
    return rijec == rijec[::-1]

def main():
    # Unos riječi od strane korisnika
    rijec = input("Unesite riječ: ")
    
    if palindrom(rijec):
        print(f"Riječ '{rijec}' je palindrom.")
    else:
        print(f"Riječ '{rijec}' nije palindrom.")
    
    assert palindrom('kisik')
    assert palindrom('a')
    assert palindrom('')
    assert palindrom('anavolimilovana')
    assert palindrom(5) is False
    assert palindrom('aa')
    assert palindrom('ovo nije palindrom') is False
    print("Implementacija je tocna!")

if __name__ == '__main__':
    main()