import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from collections import Counter
import seaborn as sns
from scipy.stats.stats import pearsonr
from functions import Functions

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('float_format', '{:f}'.format)

df = pd.read_csv('master.csv')
dfzem = pd.read_csv('master.csv')
dfnorm = pd.read_csv('master.csv')

'''         NR.2
Atlikti duomenų rinkinio kokybės analizę (žr. 2 pav.).
Kiekvienam tolydinio tipo atributui paskaičiuoti:
 bendrą reikšmių skaičių,   trūkstamų reikšmių procentą,
 kardinalumą,   minimalią (min) ir maksimalią (max) reikšmes,
 1-ąją ir 3- ją kvartilius,   vidurkį,   medianą,
 standartinį nuokrypį.
'''
# Functions.duomenu_kokybes_analize_tolydiniai(df)

'''         NR.3
Kiekvienam kategorinio tipo atributui paskaičiuoti:
 bendrą reikšmių skaičių,   trūkstamų reikšmių procentą,
 kardinalumą,   modą,  modos dažnumo reikšmę
 modos procentinę reikšmę  2-ąją modą,
 2-osios modos dažnumo reikšmę,
 2-osios modos procentinę reikšmę. 
'''
# Functions.duomenu_kokybes_analize_kategoriniai(df)

'''         NR.4
Nupaišyti atributų histogramas
(rekomenduotinas stulpelių skaičius randamas formule:
1 + 3.22 ∙ 𝑙𝑜𝑔𝑒 𝑛 = 34, kur n imties dydis).
Ataskaitoje pateikti aprašymus, koks tai pasiskirstymas
(pvz., normalusis, vien(a)modalis, eksponentinis ir t.t.)
ir kokias išvadas pagal tai galima formuluoti. 
'''
# Functions.histogramos_tolydiniai(df)
# Functions.histogramos_kategoriniai(df)


'''         NR.6.1
Tolydinio tipo atributams: naudojant „scatter plot“
tipo diagramą pateikti kelis (2-3) pavyzdžius su
stipria tiesine atributų priklausomybe
(tiesioginė arba atvirkštinė koreliacija)
bei kelis pavyzdžius su tarpusavyje nekoreliuojančiais
(silpnai koreliuojančiais) atributais. Pakomentuoti rezultatus. 
'''
# Functions.scatter_plot_tolydiniai(df, 'population', 'suicides_no', 'Gyventojų kiekis', 'Savižudžių kiekis')
# Functions.scatter_plot_tolydiniai(df, 'population', 'gdp_for_year', 'Gyventojų kiekis', 'Metinis BPV')
# Functions.scatter_plot_tolydiniai(df, 'HDI for year', 'gdp_per_capita', 'Metinis žmogaus socialinės raidos indeksas', 'BPV žmogui')
# Functions.scatter_plot_tolydiniai(df, 'suicides/100k pop', 'gdp_per_capita', 'Savižudžių procentas', 'BPV gyventojui')
# Functions.scatter_plot_tolydiniai(df, 'suicides_no', 'year', 'Savižudžių kiekis', 'Metai')

'''         NR.6.2
Pateikti SPLOM diagramą  (Scatter Plot Matrix). 
'''
# Functions.scatter_plot_matrix(df)

'''         NR.6.3
Kategorinio tipo atributams:
naudojant „bar plot“ tipo diagramą pateikti keletą (2-3)
atributų priklausomybės pavyzdžių ir pakomentuoti rezultatus.
'''
# Functions.bar_plot_kategoriniai(df, 'age', 'sex', '15-24 years')
# Functions.bar_plot_kategoriniai(df, 'age', 'sex', '35-54 years')
# Functions.bar_plot_kategoriniai(df, 'age', 'generation', '15-24 years')
# Functions.bar_plot_kategoriniai(df, 'age', 'generation', '35-54 years')
'''         NR.6.4
Pateikti keletą (2-3) histogramų ir „box plot“
diagramų pavyzdžių, vaizduojančių sąryšius tarp
kategorinio (pavyzdys pateiktas pav.3) ir tolydinio tipo kintamųjų
'''
# Functions.box_plot_bendri_tipai(df, 'year', 'gdp_per_capita', 'Metai', 'Metinis BVP')
# Functions.box_plot_bendri_tipai(df, 'year', 'generation', 'Metai', 'Karta')
# Functions.box_plot_bendri_tipai(df, 'year', 'HDI for year', 'Metai', 'Metinis žmogaus socialinės raidos indeksas')

'''         NR.7
Paskaičiuoti kovariacijos ir koreliacijos reikšmes
tarp tolydinio tipo atributų ir grafiškai atvaizduoti
koreliacijos matricą. Rezultatus pakomentuoti. 
'''
# Functions.cov_corr(df)
# Functions.korealiacijos_zemelapis(dfzem)

'''         NR.8
Atlikti duomenų normalizaciją ( režiai [0;1] arba [-1;1]). 
'''
# Functions.normalize(dfzem)

'''         NR.9
Kategorinio tipo kintamuosius paversti į tolydinio tipo kintamuosius2
'''
Functions.factoralize(df)
