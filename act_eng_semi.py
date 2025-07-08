import numpy as np
import matplotlib.pyplot as plt
"""
Program generuje dane o żądanej energii aktywacji
w półprzewodniku. Można problem odwrócić do szukania
energii aktywacji z rzeczywistych danych"""
# Stałe
Eg = 2.5 # przerwa energetyczna w eV
k = 8.617e-5  # stała Boltzmanna w eV/K
sigma_0 = 1.0  # przewodnictwo w temperaturze T=0 K

# Zakres temperatur
#T = np.linspace(1, 300, 500)  # od 1 K do 1000 K
T = np.random.uniform(300,500,100)
# Obliczenia
ln_sigma = -Eg / (2 * k) * (1 / T) + np.log(sigma_0)
sigma = np.exp(-Eg/(2*k*T))*sigma_0
R=1/sigma
wynik = 8703*2*k
print(wynik)
#np.savetxt('dane_indeks_10.txt', np.column_stack((T,R)), header='T [K], R[Ohm]')
# Wykres
plt.scatter(1/T,ln_sigma, label=r'$\ln(\sigma)$')
plt.title(r'Zależność $\ln(\sigma)$ od odwrotności temperatury')
plt.xlabel(r'$\frac{1}{T}$ (1/K)')
plt.ylabel(r'$\ln(\sigma)$')
plt.legend()
plt.grid(True)
plt.show()
