import pandas as pd
import openpyxl
from plotnine import *

df_na = pd.read_csv(r'D:\HP_interview\laptops_selection.csv')
df = df_na.dropna()
df.insert(3, 'brand', df['name'].str.split().str[0])
df.insert(5, r'price(NTD)', round(df['price(in Rs.)'] * 0.39))
brand = df.iloc[:, 3].unique()
brand_count = df.iloc[:, 3].value_counts()
df_na.insert(3, 'brand', df_na['name'].str.split().str[0])
na_count = df_na.iloc[:, 3].value_counts()
brand_list = brand_count[brand_count > 20].index.tolist()
df7 = df[df['brand'].isin(brand_list)]


def check():
    print(df.head(8))
    print(brand)
    print('brand_count=\n', brand_count)
    print('na_count=\n', na_count)
    print(brand_list)
    print('df7:', df7.shape)
    print('df:', df.shape)


def plot():
    ta_plot = (ggplot(df7, aes(x='price(NTD)', color='brand')) + geom_density())
    print(ta_plot)


def xl_output():
    df_excel_filename = r'D:\HP_interview\laptops_selection_py.xlsx'
    df.to_excel(df_excel_filename)
    df7_excel_filename = r'D:\HP_interview\laptops_7_selection_py.xlsx'
    df7.to_excel(df7_excel_filename)


def main():
    check()
    xl_output()
    plot()


if __name__ == '__main__':
    main()
