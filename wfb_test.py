import pytest
import pandas as pd
from zd_uses import permited_uses
from wf_groups import clasificar
from test_br import is_br
uses = ['R','CF', 'C','M']

use_not_r = ['CF', 'C','M']

columnas = ['R_BH_MIN', 'BR_R_BH_MAX', 'QAH_R_BH_MAX', 'BR_R_HEIGHT', 'QAH_R_HEIGHT']
for use in uses:
    # columnas.append(rf'{use}_BH_MIN')
    columnas.append(rf'BR_{use}_BH_MAX')
    columnas.append(rf'BR_{use}_HEIGHT')

@pytest.fixture(scope="module")
def df():
    df = pd.read_csv("BR_REGULATION_C_SP.csv", sep=';', low_memory=False)
    df = df[df['SA'] == 'WFB'].copy()
    df['ZD_WF'] = df['ZONEDIST'].apply(clasificar)
    df['permited_uses'] = df['ZONEDIST'].apply(permited_uses)
    df['is_br'] = df['ZONEDIST'].apply(is_br)
    df = df.replace({'true': True, 'false': False, 'True': True, 'False': False})
    # df = df.infer_objects(copy=False)
    
    return df

def safe_convert(val):
    try:
        return pd.to_numeric(val)
    except Exception:
        return val
    
def test_ZD1_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD1']
    
    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)
    # breakpoint()
    assert not df1.empty, "No hay datos para ZD1"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 35)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 35)
                    assert pd.isna(row['QAH_R_HEIGHT'])
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        # assert pd.isna(row[f'{use}_BH_MIN'])
                        assert (row[f'BR_{use}_BH_MAX'] == 35)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 35)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 35)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 35)
                    assert pd.isna(row['QAH_R_HEIGHT'])
        
            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    # assert pd.isna(row[f'{item}_BH_MIN'])
                    assert (row[f'BR_{item}_BH_MAX'] == 35)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 35), rf'Error en {item} fila {idx}'    
        

        # breakpoint()
        
def test_ZD2_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD2']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)
    # breakpoint()
    assert not df1.empty, "No hay datos para ZD2"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 35)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 45)
                    assert pd.isna(row['QAH_R_HEIGHT'])
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        # assert pd.isna(row[f'{use}_BH_MIN'])
                        assert (row[f'BR_{use}_BH_MAX'] == 35)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 45)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 35)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 45)
                    assert pd.isna(row['QAH_R_HEIGHT'])
        
            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    # assert pd.isna(row[f'{item}_BH_MIN'])
                    assert (row[f'BR_{item}_BH_MAX'] == 35)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 45), rf'Error en {item} fila {idx}'
        
        
def test_ZD3_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD3']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)
    # breakpoint()
    assert not df1.empty, "No hay datos para ZD3"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 45)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 55)
                    assert pd.isna(row['QAH_R_HEIGHT'])
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        # assert pd.isna(row[f'{use}_BH_MIN'])
                        assert (row[f'BR_{use}_BH_MAX'] == 45)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 55)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 45)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 55)
                    assert pd.isna(row['QAH_R_HEIGHT'])
        
            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    # assert pd.isna(row[f'{item}_BH_MIN'])
                    assert (row[f'BR_{item}_BH_MAX'] == 45)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 55), rf'Error en {item} fila {idx}'


def test_ZD4_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD4']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD4"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 55)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 65)
                    assert pd.isna(row['QAH_R_HEIGHT'])
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        # assert pd.isna(row[f'{use}_BH_MIN'])
                        assert (row[f'BR_{use}_BH_MAX'] == 55)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 65)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    # assert pd.isna(row['R_BH_MIN'])
                    assert (row['BR_R_BH_MAX'] == 55)
                    assert pd.isna(row['QAH_R_BH_MAX'])
                else:
                    assert (row['BR_R_HEIGHT'] == 65)
                    assert pd.isna(row['QAH_R_HEIGHT'])
        
            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    # assert pd.isna(row[f'{item}_BH_MIN'])
                    assert (row[f'BR_{item}_BH_MAX'] == 55)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 65), rf'Error en {item} fila {idx}'


"""NO DATA FOR ZD6 GROUP IN WFB"""

# def test_ZD6_Height(df):
#     df1 = df[df['ZD_WF'] == 'ZD6']

#     for col in columnas:
#         df1[col] = df1[col].apply(safe_convert)

#     assert not df1.empty, "No hay datos para ZD6"
#     for idx, row in df1.iterrows():
#         if row['is_br'] == True:
#             if row['BR_R']==True:
#                 if row['SB'] == True:
#                     assert (row['R_BH_MIN']==35)
#                     assert (row['BR_R_BH_MAX'] == 55)
#                     assert (row['QAH_R_BH_MAX'] == 55)
#                 else:
#                     assert (row['BR_R_HEIGHT'] == 195)
#                     assert (row['QAH_R_HEIGHT'] == 195)
                    
#             for use in use_not_r:
#                 if row[f'BR_{use}'] == True:
#                     if row['SB'] == True:
#                         assert (row[f'{use}_BH_MIN'] == 35)
#                         assert (row[f'BR_{use}_BH_MAX'] == 55)
#                     else:
#                         assert (row[f'BR_{use}_HEIGHT'] == 195)
#         else:
#             if 'R' in row['permited_uses']:
#                 if row['SB'] == True:
#                     assert (row['R_BH_MIN'] == 35)
#                     assert (row['BR_R_BH_MAX'] == 55)
#                     assert (row['QAH_R_BH_MAX'] == 55)
#                 else:
#                     assert (row['BR_R_HEIGHT'] == 195)
#                     assert (row['QAH_R_HEIGHT'] == 195)

#             for item in row['permited_uses']:
#                 if item == 'R':
#                     continue
#                 if row['SB'] == True:
#                     assert (row[f'{item}_BH_MIN'] == 35)
#                     assert (row[f'BR_{item}_BH_MAX'] == 55)
#                 else:
#                     assert (row[f'BR_{item}_HEIGHT'] == 195), rf'Error en {item} fila {idx}'


def test_ZD7_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD7']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD7"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 65)
                    assert (row['QAH_R_BH_MAX'] == 65)
                else:
                    assert (row['BR_R_HEIGHT'] == 255)
                    assert (row['QAH_R_HEIGHT'] == 255)
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 65)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 255)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 65)
                    assert (row['QAH_R_BH_MAX'] == 55)
                else:
                    assert (row['BR_R_HEIGHT'] == 255)
                    assert (row['QAH_R_HEIGHT'] == 255)

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 65)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 255), rf'Error en {item} fila {idx}'
                    
def test_ZD8_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD8']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD8"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 85)
                    assert (row['QAH_R_BH_MAX'] == 85)
                else:
                    assert (row['BR_R_HEIGHT'] == 315)
                    assert (row['QAH_R_HEIGHT'] == 315)
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 85)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 315)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 85)
                    assert (row['QAH_R_BH_MAX'] == 85)
                else:
                    assert (row['BR_R_HEIGHT'] == 315)
                    assert (row['QAH_R_HEIGHT'] == 315)

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 85)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 315), rf'Error en {item} fila {idx}'


def test_ZD9_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD9']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD9"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 95)
                    assert (row['QAH_R_BH_MAX'] == 95)
                else:
                    assert (row['BR_R_HEIGHT'] == 375)
                    assert (row['QAH_R_HEIGHT'] == 375)
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 95)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 375)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 95)
                    assert (row['QAH_R_BH_MAX'] == 95)
                else:
                    assert (row['BR_R_HEIGHT'] == 375)
                    assert (row['QAH_R_HEIGHT'] == 375)

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 95)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 375), rf'Error en {item} fila {idx}'



def test_ZD10_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD10']

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD10"
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 105)
                    assert (row['QAH_R_BH_MAX'] == 105)
                else:
                    assert (row['BR_R_HEIGHT'] == 435)
                    assert (row['QAH_R_HEIGHT'] == 435)
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 105)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 435)
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 105)
                    assert (row['QAH_R_BH_MAX'] == 105)
                else:
                    assert (row['BR_R_HEIGHT'] == 435)
                    assert (row['QAH_R_HEIGHT'] == 435)

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 105)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 435), rf'Error en {item} fila {idx}'
                    
                    
                    
def test_ZD12_ZD13_ZD14_ZD15_Height(df):
    df1 = df[df['ZD_WF'].isin(['ZD12','ZD13','ZD14','ZD15'])]

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD12-ZD15  "
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 155)
                    assert (row['QAH_R_BH_MAX'] == 155)
                else:
                    assert (row['BR_R_HEIGHT'] == 'no limit')
                    assert (row['QAH_R_HEIGHT'] == 'no limit')
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 155)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 'no limit')
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 155)
                    assert (row['QAH_R_BH_MAX'] == 155)
                else:
                    assert (row['BR_R_HEIGHT'] == 'no limit')
                    assert (row['QAH_R_HEIGHT'] == 'no limit')

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 155)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 'no limit'), rf'Error en {item} fila {idx}'
                    
                    
                    
def test_ZD11_Height(df):
    df1 = df[df['ZD_WF'].isin(['ZD11'])]

    for col in columnas:
        df1[col] = df1[col].apply(safe_convert)

    assert not df1.empty, "No hay datos para ZD11  "
    for idx, row in df1.iterrows():
        if row['is_br'] == True:
            if row['BR_R']==True:
                if row['SB'] == True:
                    assert (row['R_BH_MIN']==35)
                    assert (row['BR_R_BH_MAX'] == 135)
                    assert (row['QAH_R_BH_MAX'] == 135)
                else:
                    assert (row['BR_R_HEIGHT'] == 'no limit')
                    assert (row['QAH_R_HEIGHT'] == 'no limit')
                    
            for use in use_not_r:
                if row[f'BR_{use}'] == True:
                    if row['SB'] == True:
                        assert (row[f'{use}_BH_MIN'] == 35)
                        assert (row[f'BR_{use}_BH_MAX'] == 135)
                    else:
                        assert (row[f'BR_{use}_HEIGHT'] == 'no limit')
        else:
            if 'R' in row['permited_uses']:
                if row['SB'] == True:
                    assert (row['R_BH_MIN'] == 35)
                    assert (row['BR_R_BH_MAX'] == 135)
                    assert (row['QAH_R_BH_MAX'] == 135)
                else:
                    assert (row['BR_R_HEIGHT'] == 'no limit')
                    assert (row['QAH_R_HEIGHT'] == 'no limit')

            for item in row['permited_uses']:
                if item == 'R':
                    continue
                if row['SB'] == True:
                    assert (row[f'{item}_BH_MIN'] == 35)
                    assert (row[f'BR_{item}_BH_MAX'] == 135)
                else:
                    assert (row[f'BR_{item}_HEIGHT'] == 'no limit'), rf'Error en {item} fila {idx}'