import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Muat data
data_startup = pd.read_csv('50_Startups.csv')

# 1. Isi nilai yang hilang dengan rata-rata
imputer = SimpleImputer(strategy='mean')
data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']] = imputer.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']])

# 2. Lakukan one-hot encoding pada kolom 'State'
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
data_startup_encoded = pd.DataFrame(ct.fit_transform(data_startup))
data_startup_encoded = data_startup_encoded.rename(columns={0: 'State_1', 1: 'State_2', 2: 'State_3'})

# 3. Buat kolom baru 'Tax'
data_startup['Tax'] = (data_startup['Profit'] + data_startup['Marketing Spend'] + data_startup['Administration']) * 0.05

# 4. Standarisasi kolom-kolom tersebut
scaler = StandardScaler()
data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']] = scaler.fit_transform(data_startup[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit', 'Tax']])

# Tampilkan data yang telah diproses
print(data_startup.head())