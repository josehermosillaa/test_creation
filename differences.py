import pandas as pd

# Leer solo las cabeceras para ver las columnas
cols1 = pd.read_csv('BR_REGULATION_250506_1902.csv', nrows=0, sep=';').columns.tolist()
cols2 = pd.read_csv('BR_REGULATION_SP_250624_2246.csv', nrows=0, sep=';').columns.tolist()

# Normalizar nombres de columnas (mayúsculas y sin espacios)
def normalizar(cols):
    return [str(col).strip().upper() for col in cols]

cols1_norm = normalizar(cols1)
cols2_norm = normalizar(cols2)

print('Columnas archivo 1:', cols1_norm)
print('Columnas archivo 2:', cols2_norm)

# Encontrar columnas en común normalizadas
common_cols_norm = [col for col in cols1_norm if col in cols2_norm]
no_common_cols_norm = [col for col in cols2_norm if col not in cols1_norm]

print('Columnas en común:', common_cols_norm)
print('Columnas no en común:', no_common_cols_norm)

if not common_cols_norm:
    print('No hay columnas en común para comparar.')
    exit(1)

# Crear un mapeo de nombre original a normalizado para ambos archivos
map1 = {str(col).strip().upper(): str(col) for col in cols1}
map2 = {str(col).strip().upper(): str(col) for col in cols2}

# Leer los dataframes usando solo las columnas en común
usecols1_set = set([map1[col] for col in common_cols_norm])
usecols2_set = set([map2[col] for col in common_cols_norm])

df1 = pd.read_csv('BR_REGULATION_250506_1902.csv', sep=';', usecols=lambda x: x in usecols1_set)
df2 = pd.read_csv('BR_REGULATION_SP_250624_2246.csv', sep=';', usecols=lambda x: x in usecols2_set)

print('Filas archivo 1:', len(df1))
print('Filas archivo 2:', len(df2))
print('Filas archivo SP: 2525233 ')

breakpoint()
# Renombrar columnas a la versión normalizada para comparar
rename_dict1 = {map1[col]: col for col in common_cols_norm}
rename_dict2 = {map2[col]: col for col in common_cols_norm}
df1 = df1.rename(columns=rename_dict1)
df2 = df2.rename(columns=rename_dict2)

# Eliminar duplicados
original_len_df2 = len(df2)
df2 = df2.drop_duplicates()
print(f'Filas archivo 2 después de eliminar duplicados: {len(df2)} (eliminadas {original_len_df2 - len(df2)})')
breakpoint()
