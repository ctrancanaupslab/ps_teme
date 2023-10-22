# setam frecventa de esantionare
frecventa_esantionare = 2000  # în Hz

# a) calculul intervalului de timp dintre doua esantiaone
interval_de_timp = 1 / frecventa_esantionare
print("Intervalul de timp între două eșantioane este de", interval_de_timp, "secunde")

# b) calculul cator bytes vor ocupa datele pentru o ora de achizitie
numar_esantioane_pe_ora = 3600 * frecventa_esantionare 
biti_pe_esantion = 4
bytes_pe_ora = (numar_esantioane_pe_ora * biti_pe_esantion) / 8  # Conversie din biti în bytes
print("Numarul de bytes necesari pentru o ora de achizitie este de", bytes_pe_ora, "bytes")
