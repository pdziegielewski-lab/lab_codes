import matplotlib.pyplot as plt
import math
import numpy as np
"""
Code calculates Linderman paremeter based on the comparison of
two MD simulations frames. 
Important! Atoms in xyz/dump file have to be sorted - they have
to be in the same order in all simulation frames.
"""

def czytaj_pozycje_xyz(sciezka_do_pliku):
    pozycje = []
    try:
        with open(sciezka_do_pliku, 'r') as plik:
            # Pomijamy pierwszą linię, która zawiera liczbę atomów
            plik.readline()
            for linia in plik:
                # Rozdzielamy linie na listę tokenów
                tokens = linia.split() 
                # Parsujemy współrzędne x, y, z
                x = float(tokens[0])
                y = float(tokens[1])
                z = float(tokens[2])
                # Dodajemy pozycję do listy
                pozycje.append((x, y, z))
    except FileNotFoundError:
        print(f"Plik {sciezka_do_pliku} nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd podczas czytania pliku: {e}")
    return pozycje

def porownaj_pozycje(plik1, plik2):

    pozycje1 = czytaj_pozycje_xyz(plik1)
    pozycje2 = czytaj_pozycje_xyz(plik2)

    roznica = []

    if len(pozycje1) != len(pozycje2):
        print("Liczba atomów w plikach różni się. Nie można porównać pozycji.")
        return roznica

    for i in range(len(pozycje1)):
        roznica_x = pozycje1[i][0] - pozycje2[i][0]
        roznica_y = pozycje1[i][1] - pozycje2[i][1]
        roznica_z = pozycje1[i][2] - pozycje2[i][2]
        roznica_xyz = math.sqrt(roznica_x**2+roznica_y**2+roznica_z**2)
        roznica.append(roznica_xyz)

    return roznica

# Przykład użycia
for i in range(0, 2510, 10):
    j = i + 10
    filename = '%d.dat' %j
    #sciezka_do_pliku_xyz1 = '%d.xyz' %i
    sciezka_do_pliku_xyz1 = '0.xyz'
    sciezka_do_pliku_xyz2 = '%d.xyz' %j

    roznica_pozycji = porownaj_pozycje(sciezka_do_pliku_xyz1, sciezka_do_pliku_xyz2)
    tablica_pozycji = np.array(roznica_pozycji)
    # Zapisz tablicę do pliku z jedną kolumną
    sciezka_do_pliku = filename
    np.savetxt(sciezka_do_pliku, tablica_pozycji, fmt='%1.4f', delimiter='\t')

    print(f"Tablica została zapisana do pliku: {sciezka_do_pliku}")
