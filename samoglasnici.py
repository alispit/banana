def broji_samoglasnike(text):
    text = str(text)
    samoglasnici = "aeiouAEIOU"
    broj_samoglasnika = sum(1 for char in text if char in samoglasnici)
    
    return broj_samoglasnika

def main():
    tekst = input("Unesite tekst: ")
    broj = broji_samoglasnike(tekst)
    print(f"Broj samoglasnika u unesenom tekstu je: {broj}")
if __name__ == '__main__':
    main()