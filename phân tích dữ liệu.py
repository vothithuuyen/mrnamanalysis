import pandas as pd
import matplotlib as plt
#tải dữ liệu lên
df = pd.read_csv('F:\dulieuxettuyendaihoc.csv', header=0, delimiter=',')
#câu 3
#in 10 dòng đầu
print (df.head(10))
#in 10 dòng cuối 
print (df.tail(10))
#câu 4
#hiển thị số dòng trống 
print (df['DT'].isna().sum())
#điền dữ liệu thiếu 
df['DT'].fillna(0, inplace = True)
print (df['DT'])
#câu 5
print (df['T1'])
#thống kế dữ liệu thiếu T1
print (df['T1'].isna().sum())
#hiệu chỉnh 
df['T1'].fillna(df['T1'].mean(), inplace = True)
#câu 6
print (df['DH1'].isna().sum())
df['DH1'].fillna(df['DH1'].mean(), inplace = True)
#câu 7
df['TBM1'] = (2 * df['T1'] + df['L1'] + df['H1'] + df['S1'] + df['V1'] * 2 + df['X1'] + df['D1'] + df['N1']) / 10
print(df['TBM1'])
df['TBM2'] = (2 * df['T2'] + df['L2'] + df['H2'] + df['S2'] + df['V2'] * 2 + df['X2'] + df['D2'] + df['N2']) / 10
print(df['TBM2'])
df['TBM3'] = (2 * df['T3'] + df['L3'] + df['H3'] + df['S3'] + df['V3'] * 2 + df['X3'] + df['D3'] + df['N3']) / 10
print(df['TBM3'])
#câu 8
#TBM1
df.loc[df['TBM1'] < 5.0, 'XL1'] = 'Y'
print(df['XL1'])
df.loc[(df['TBM1'] >= 5.0) & (df['TBM1'] < 6.5), 'XL2'] = 'TB'
print(df['XL2'])
df.loc[(df['TBM1'] >= 6.5) & (df['TBM1'] < 8.0), 'XL3'] = 'K'
print(df['XL3'])
df.loc[(df['TBM1'] >= 8.0) & (df['TBM1'] < 9.0), 'XL4'] = 'G'
print(df['XL4'])
df.loc[df['TBM1'] > 9.0, 'XL5'] = 'XS'
print(df['XL5'])
#TBM2
df.loc[df['TBM2'] < 5.0, 'XL1'] = 'Y'
print(df['XL1'])
df.loc[(df['TBM2'] >= 5.0) & (df['TBM2'] < 6.5), 'XL2'] = 'TB'
print(df['XL2'])
df.loc[(df['TBM2'] >= 6.5) & (df['TBM2'] < 8.0), 'XL3'] = 'K'
print(df['XL3'])
df.loc[(df['TBM2'] >= 8.0) & (df['TBM2'] < 9.0), 'XL4'] = 'G'
print(df['XL4'])
df.loc[df['TBM2'] > 9.0, 'XL5'] = 'XS'
print(df['XL5'])
#TBM3
df.loc[df['TBM3'] < 5.0, 'XL1'] = 'Y'
print(df['XL1'])
df.loc[(df['TBM3'] >= 5.0) & (df['TBM3'] < 6.5), 'XL2'] = 'TB'
print(df['XL2'])
df.loc[(df['TBM3'] >= 6.5) & (df['TBM3'] < 8.0), 'XL3'] = 'K'
print(df['XL3'])
df.loc[(df['TBM3'] >= 8.0) & (df['TBM3'] < 9.0), 'XL4'] = 'G'
print(df['XL4'])
df.loc[df['TBM3'] > 9.0, 'XL5'] = 'XS'
print(df['XL5'])
#câu 9

#câu 10
df.loc[(df['KT'] == 'A') & ((df['DH1'] + df['DH2']) / 2 >= 5), 'KQXT'] = 1
