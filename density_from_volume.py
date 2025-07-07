# -*- coding: utf-8 -*-

def oblicz_gestosc_ukladu_Zr_Cu():
    """
    Oblicza gęstość układu zawierającego atomy cyrkonu (Zr) i miedzi (Cu)
    na podstawie podanej objętości komórki.

    Code calculates the density of the system using atomic masses and the number of atoms. 
    Here, using the example of the Zr-Cu system. You have to know the volume of your system in A^3.
    """

    # Stałe fizykochemiczne/masses of atoms
    MASA_MOLOWA_ZR = 91.224  # g/mol
    MASA_MOLOWA_CU = 63.546  # g/mol
    LICZBA_AVOGADRO = 6.02214076e23  # 1/mol Avogadro constant

    # Number of atoms in the system
    liczba_atomow_Zr = 84
    liczba_atomow_Cu = 44

    print("Program caluclates density of the system.")
    print(f"Number of Zr atoms in the system: {liczba_atomow_Zr}")
    print(f"Number of Cu atoms in the system: {liczba_atomow_Cu}")
    print("-" * 30)

    while True:
        try:
            objetosc_A3_str = input("Write volume of the system (Å³): ")
            objetosc_A3 = float(objetosc_A3_str)
            if objetosc_A3 <= 0:
                print("Volume must be positive value - try once again.")
                continue
            break
        except ValueError:
            print("Wrong value, give a number")

    # 1. main part of code
    masa_Zr_gramy = (liczba_atomow_Zr * MASA_MOLOWA_ZR) / LICZBA_AVOGADRO
    masa_Cu_gramy = (liczba_atomow_Cu * MASA_MOLOWA_CU) / LICZBA_AVOGADRO
    masa_calkowita_gramy = masa_Zr_gramy + masa_Cu_gramy

    # 2. Przeliczenie objętości z Å³ na cm³
    # 1 Å = 1e-8 cm
    # 1 Å³ = (1e-8 cm)³ = 1e-24 cm³
    objetosc_cm3 = objetosc_A3 * 1e-24

    # 3. Obliczenie gęstości
    gestosc_g_cm3 = masa_calkowita_gramy / objetosc_cm3

    print("-" * 30)
    print(f"Mass of the system: {masa_calkowita_gramy:.4e} g")
    print(f"Volume of the system: {objetosc_A3:.2f} Å³ = {objetosc_cm3:.4e} cm³")
    print("-" * 30)
    print(f"Calculated density: {gestosc_g_cm3:.4f} g/cm³")

if __name__ == "__main__":
    oblicz_gestosc_ukladu_Zr_Cu()
