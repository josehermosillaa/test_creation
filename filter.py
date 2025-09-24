import pandas as pd

SG = pd.read_csv('FAR_REGULATION_250430_1807.csv', sep=';')
SG = SG[SG['BBL'] == 1004930041]
breakpoint()
# filtro = (SG['SP'] != 'empty') & (SG['SP'] != '') & (SG['SP'].notna())
# SG_filtrado = SG[filtro]

# SG_filtrado.to_csv('SG_filtrado.csv', index=False)