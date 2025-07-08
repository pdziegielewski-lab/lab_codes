"""program oblicza i generuje plik xyz zawierający x2,y2,z2,lindperatom,vwyp1(predkosc),dr(roznica wektorow r), drl (to samo ale ze skladowcyh) pliki wejsciowe
 musza miec posortowane atomy po ID, plik bez naglowka, tylko kolumny x y z
 Program can generate xyz files for visulasization of lindemann paremeter per atom using e.g. Ovito.
"""
import math
#czas=[0,0.048,0.096,0.144,0.192,0.24,0.288,0.336,0.384,0.43199,0.47999,0.52799,0.57599,0.62399,0.67199,0.71999,0.76799,0.81599,0.86399,0.91199,0.95999,1.00799,1.05599,1.10399,1.15199,1.19998,1.24798,1.29598,1.34398,1.39198,1.43998,1.48798,1.53598,1.58398,1.63198,1.67998,1.72798,1.77598,1.82398,1.87198,1.91998,1.96797,2.01597,2.06397,2.11197,2.15997,2.20797,2.25597,2.30397,2.35197,2.39997,2.44797,2.49597,2.54397,2.59197,2.63997,2.68797,2.73596,2.78396,2.83196,2.87996,2.92796,2.97596,3.02396,3.07196,3.11996,3.16796,3.21596,3.26396,3.31196,3.35996,3.40796,3.45596,3.50395,3.55195,3.59995,3.64795,3.69595,3.74395,3.79195,3.83995,3.88795,3.93595,3.98395,4.03195,4.07995,4.12795,4.17595,4.22395,4.27194,4.31994,4.36794,4.41594,4.46394,4.51194,4.55994,4.60794,4.65594,4.70394,4.75194,4.79994,4.84794,4.89594,4.94394,4.99194,5.03994,5.08793,5.13593,5.18393]
# czas to dt50fs a czas3 dla dt=0.5ps
czas3=[0,0.47999,0.95999,1.43998,1.91998,2.39997,2.87996,3.35996,3.83995,4.31994,4.79994,5.27993,5.75993,6.23992,6.71991,7.19991,7.6799,8.15989,8.63989,9.11988,9.59988,10.07987,10.55986,11.03986,11.51985,11.99985,12.47984,12.95983,13.43983,13.91982,14.39982,14.87981,15.3598,15.8398,16.31979,16.79978,17.27978,17.75977,18.23976,18.71976,19.19975,19.67975,20.15974,20.63973,21.11973,21.59972,22.07972,22.55971,23.0397,23.5197,23.99969,24.47969,24.95968,25.43967,25.91967,26.39966,26.87965,27.35965,27.83964,28.31964] 
suma = 0.0
srednia_czas = 0.0
for j in range(0,60):
    filename = '0.xyz'
    with open(filename) as plik:
        tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]
    filename4 = '%d.xyz' % j
    with open(filename4) as plik1:
        tab1 = [list(map(float, wiersz1.split(' '))) for wiersz1 in plik1]
    plus1 = j+1
    filename2 = '%d.xyz' % plus1
    with open(filename2) as plik2:
        tab2 = [list(map(float, wiersz2.split(' '))) for wiersz2 in plik2]
    filename5 = 'centro%d.dat' % j
    with open(filename5) as plik5:
        tab5 = [list(map(float, wiersz5.split(' '))) for wiersz5 in plik5]
    krokczasu = czas3[plus1]-czas3[j]
    filename3 = 'xyz_lind_v_centro_dr_drl%d.xyz' % plus1
    roznica2 = open(filename3,"w")
    print("931063", file=roznica2)
    print('"Lattice="0 0 0" Origin="200 200 200" Properties=pos:R:4', file=roznica2)
    for i in range(0,931063):
    #for i in range(0,5):
        dr = 0.0
        dx=dy=dz=0.0
        x = tab[i][0]
        y = tab[i][1]
        z = tab[i][2] #wspolrzedne pliku 0
        x1 = tab1[i][0] #wspolrzedne z pliku j
        y1 = tab1[i][1]
        z1 = tab1[i][2]
        x2 = tab2[i][0] # wspolrzedne z pliku j+1
        y2 = tab2[i][1]
        z2 = tab2[i][2]
        centro = tab5[i][3]
        dx=(x2-x1)
        dy=(y2-y1)
        dz=(z2-z1)
        #r1=math.sqrt(x**2+y**2+z**2)
        #r2=math.sqrt(x2**2+y2**2+z2**2)
        r1=math.sqrt(y**2+z**2)
        r2=math.sqrt(y2**2+z2**2)
        drl=math.sqrt((y2-y)**2+(z2-z)**2) #przemieszczenie ze wspolrzednych
        drr = math.sqrt((r2 - r1)**2)
        dr = r2-r1 #roznica wektorow polozen
        drt = dr/czas3[plus1]
        roznica = math.sqrt((dr-drt)**2)
        vy=(dy/krokczasu)
        vz=(dz/krokczasu)
        vwyp1=math.sqrt(vy*vy+vz*vz) #v[A/ps]
        lindperatom = drl/2.72
        print(x2,y2,z2,lindperatom,vwyp1,centro, dr, drl,file=roznica2)
        suma = suma + roznica
    srednia = suma/czas3[plus1]
    licznik = math.sqrt(srednia)
    lind = (licznik/2.72)/1000
    print(lind)
    srednia = 0.0
    licznik = 0.0  
      
msd = 0
licznik = 0.0
lind = 0.0
roznica2.close()
