import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from collections import Counter
import seaborn as sns
from scipy.stats.stats import pearsonr

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('float_format', '{:f}'.format)

class Functions:

    def duomenu_kokybes_analize_tolydiniai(df):
        count = len(df)
        newdf = pd.DataFrame(columns=['Atributo pavadinimas', 'Kiekis',
                                    'Trūkstamo reikšmės, %', 'Kardinalumas',
                                    'Minimali reikšmė', 'Maksimali reikšmė',
                                    '1-asis kvartilis', '3-asis kvartilis',
                                    'Vidurkis', 'Mediana', 'Standartinis nuokrypis'])
        for col in df.columns:
            if df.dtypes[col] != 'object':
                # print("Stulpelio pavadinimas:", col)
                # print("Stulpelio duomenų tipas:", df.dtypes[col])
                # print("Bendras reikšmių skaičius:", df[col].count())
                # print("Trūkstamų reikšmių proc:", df[col].isnull().sum() * 100 / count, "%")
                # print("Kardinalumas:", df[col].nunique())
                # print("Minimali reikšmė", df[col].min())
                # print("Maksimali reikšmė", df[col].max())
                # print("Pirmas kvartilis:", df[col].quantile(0.25))
                # print("Trečias kvartilis:", df[col].quantile(0.75))
                # print("Vidurkis:", df[col].mean())
                # print("Mediana:", df[col].quantile(0.5))
                # print("Standartinis nuokrypis:", df[col].std())
                # print()
                newdf.loc[-1] = [col, df[col].count(), (df[col].isnull().sum() * 100 / count),
                               df[col].nunique(), df[col].min(), df[col].max(),
                               df[col].quantile(0.25), df[col].quantile(0.75),
                               df[col].mean(), df[col].quantile(0.5), df[col].std()]
                newdf.index = newdf.index + 1
                newdf = newdf.sort_index()
        # print(newdf)
        newdf.to_excel("tolydiniai.xlsx")

    def duomenu_kokybes_analize_kategoriniai(df):
        count = len(df)
        newdf = pd.DataFrame(columns=['Atributo pavadinimas', 'Kiekis',
                                    'Trūkstamo reikšmės, %', 'Kardinalumas',
                                    'Moda', 'Modos dažnumas', 'Moda, %',
                                    '2-oji Moda', '2-osios Modos dažnumas',
                                    '2-oji Moda, %'])

        for col1 in df.columns:
            if df.dtypes[col1] == 'object':
                # print("Stulpelio pavadinimas:", col1)
                # print("Stulpelio duomenų tipas:", df.dtypes[col1])
                # print("Bendras reikšmių skaičius:", df[col1].count())
                # print("Trūkstamų reikšmių proc:", df[col1].isnull().sum() * 100 / count, "%")
                # print("Kardinalumas:", df[col1].nunique())
                # print("Prima moda:")
                # print(df[col1].mode().values)
                # print("Dažnumo reikšmė:", df[col1].value_counts().max())
                # print("Procentinė reikšmė:", df[col1].value_counts(normalize=True).max() * 100, "%")
                af = df[col1].replace(df[col1].mode().values, np.nan)
                # print("Antroji moda:")
                # print(af.mode().values)
                # print("Dažnumo reikšmė:", af.value_counts().max())
                # print("Procentinė reikšmė:", af.value_counts().max() / df[col1].count() * 100, "%")
                # print()
                newdf.loc[-1] = [col1, df[col1].count(), (df[col1].isnull().sum() * 100 / count),
                               df[col1].nunique(), df[col1].mode().values, df[col1].value_counts().max(),
                               df[col1].value_counts(normalize=True).max() * 100, af.mode().values,
                               af.value_counts().max(), af.value_counts().max() / df[col1].count() * 100]
                newdf.index = newdf.index + 1
                newdf = newdf.sort_index()
        # print(newdf)
        newdf.to_excel("kategoriniai.xlsx")

    def histogramos_tolydiniai(df):
        for col in df.columns:
            if df.dtypes[col] != 'object':
                df[col].hist(bins=34, color='#37777D', ec='black')
                plt.title(col)
                plt.xlabel('Reikšmės')
                plt.ylabel('Kiekis')
                plt.show()

    def histogramos_kategoriniai(df):
        for col in df.columns:
                if df.dtypes[col] == 'object':
                    freqs = Counter(df[col])
                    xvals = range(len(freqs.values()))
                    plt.bar(xvals, freqs.values(), color='#37777D', ec='black')
                    plt.xticks(xvals, freqs.keys(), rotation='vertical')
                    plt.title(col)
                    plt.xlabel('Reikšmės')
                    plt.ylabel('Kiekis')
                    plt.show()

    def korealiacijos_zemelapis(df):
        for col in df.columns:
            if df.dtypes[col] == 'object':
                df[col] = df[col].factorize()[0]
        heat_map = sns.heatmap(df.corr().round(3),
                               annot=True,
                               annot_kws={'size': 8})
        plt.show()
        # print(df4.corr())

    def scatter_plot_tolydiniai(df, col1, col2, n1, n2):
        plt.scatter(df[col1], df[col2], s=20)
        plt.xlabel(n1)
        plt.ylabel(n2)
        plt.show()

    def scatter_plot_matrix(df):
        sns.pairplot(df)
        plt.show()

    def bar_plot_kategoriniai(df, col1, col2, filtercol1):
        filter = df[col1] == filtercol1
        sns.set(style="darkgrid")
        titanic = df.where(filter)
        ax = sns.countplot(x=col1, hue=col2, data=titanic)
        plt.show()

    def box_plot_bendri_tipai(df, col1, col2, n1, n2):
        sns.set_style("whitegrid")
        g = sns.boxplot(x=col1, y=col2, data=df).set(xlabel=n1, ylabel=n2)
        plt.xticks(rotation=90)
        plt.show()

    def cov_corr(df):
        print()
        print('Kovariacijos')
        print(df.cov())
        print()
        print('Koreliacijos')
        print(df.corr())

    def normalize(df):
        for col in df.columns:
            if df.dtypes[col] == 'object':
                df[col] = df[col].factorize()[0]
        normalized_df = (df - df.min()) / (df.max() - df.min())
        print(normalized_df)

    def factoralize(df):
        for col in df.columns:
            if df.dtypes[col] == 'object':
                df[col] = df[col].factorize()[0]
        print(df)




