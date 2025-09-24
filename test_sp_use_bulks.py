import pytest
import pandas as pd
import ast

uses = ['R','CF', 'C','M']

# columnas = ['BR_R', 'QAH_R', 'BR_CF', 'BR_C', 'BR_M',
#        'BRT_R', 'BRT_R+25_CF_C', 'BRT_R-25_CF_C', 'BRT_CF', 'BRT_C', 'BRT_M',
#        'BRT_CF_C', 'BH_R', 'BH_CF', 'BH_C', 'BH_M', 'AH_R', 'AH_R+25_MX',
#        'AH_R-25_MX', 'AH_CF', 'AH_C', 'AH_M', 'STBH_R', 'STBH_R+25_CF_C',
#        'STBH_R-25_CF_C', 'STBH_CF', 'STBH_C', 'STBH_M', 'STBH_CF_C', 'STAH_R',
#        'STAH_R+25_CF_C', 'STAH_R-25_CF_C', 'STAH_CF', 'STAH_C', 'STAH_M',
#        'STAH_CF_C', 'TB_R', 'TB_R25_CF_C',]

br_columns = ['BR_R', 'QAH_R', 'BR_CF', 'BR_C', 'BR_M',]
brt_columns = ['BRT_R', 'BRT_R+25_CF_C', 'BRT_R-25_CF_C', 'BRT_CF', 'BRT_C', 'BRT_M','BRT_CF_C']
bh_columns = ['BH_R', 'BH_CF', 'BH_C', 'BH_M']
ah_columns = ['AH_R', 'AH_R+25_MX', 'AH_R-25_MX', 'AH_CF', 'AH_C', 'AH_M']
stbh_columns = ['STBH_R', 'STBH_R+25_CF_C', 'STBH_R-25_CF_C', 'STBH_CF', 'STBH_C', 'STBH_M', 'STBH_CF_C']
stah_columns = ['STAH_R', 'STAH_R+25_CF_C', 'STAH_R-25_CF_C', 'STAH_CF', 'STAH_C', 'STAH_M', 'STAH_CF_C']
tb_columns = ['TB_R', 'TB_R25_CF_C']
all_not_columns =  brt_columns + bh_columns + ah_columns + stbh_columns + stah_columns + tb_columns

@pytest.fixture(scope="module")
def df():
    return pd.read_csv("USE_BULKS_YARD_250718_1422.csv", sep=';', low_memory=False)

def safe_convert(val):
    try:
        return pd.to_numeric(val)
    except Exception:
        return val


def test_USE_BULK_SP_C_R8(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'C' in x
    ) & df['ZONEDIST'].isin(['R8'])
    
    
    # cond = (df['SP'] == 'C') & (df['ZONEDIST'] == 'R8') 
    df_cond = df[cond].copy()
    # breakpoint()
    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all()
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    
def test_USE_BULK_SP_HSQ_M1_6(df):
    import ast
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'HSQ' in x
    ) & df['ZONEDIST'].isin(['M1-6'])
    # breakpoint()
    # cond = (df['SP'] == 'HSQ') & (df['ZONEDIST'] == 'M1-6') 
    df_cond = df[cond].copy()
    
    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == True).all()
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    

    import ast

def test_USE_BULK_SP_FH_C4_4A(df):
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'FH' in x
    ) & df['ZONEDIST'].isin(['C4-4A', 'C4-5X'])

    df_cond = df[cond].copy()

    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='BH' y ZONEDIST en ['C4-4A', 'C4-5X']"

    # ✅ Validaciones esperadas si hay datos
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all()
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()

    

def test_USE_BULK_SP_FH_R5D(df):
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'FH' in x
    ) & df['ZONEDIST'].isin(['R5D'])
    # cond = (df['SP'][0] == 'BH') & (df['ZONEDIST'].isin(['C4-4A', 'C4-5X', 'R5D'])) 
    df_cond = df[cond].copy()
    
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='FH' y ZONEDIST en [R5D]"

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == False).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all()
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    

    
def test_USE_BULK_SP_SNX(df):
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'SNX' in x
    ) & df['ZONEDIST'].isin(['M1-5/R7D','M1-5/R7X','M1-5/R9A','M1-5/R9X','M1-5/R10','M1-6/R10'])
    # cond = (df['SP'][0] == 'BH') & (df['ZONEDIST'].isin(['C4-4A', 'C4-5X', 'R5D'])) 
    df_cond = df[cond].copy()
    # breakpoint()
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='SNX' y ZONEDIST en ['M1-5/R7D','M1-5/R7X','M1-5/R9A','M1-5/R9X','M1-5/R10','M1-6/R10'] "

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == True).all()
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    

    
    
def test_USE_BULK_SP_TMU(df):
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'TMU' in x
    ) & df['ZONEDIST'].isin(['C6-3A','C6-2A']) #C6-3 case
    # cond = (df['SP'][0] == 'BH') & (df['ZONEDIST'].isin(['C4-4A', 'C4-5X', 'R5D'])) 
    df_cond = df[cond].copy()
    # breakpoint()
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='SNX' y ZONEDIST en ['M1-5/R7D','M1-5/R7X','M1-5/R9A','M1-5/R9X','M1-5/R10','M1-6/R10'] "

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    
def test_USE_BULK_SP_TMU_C6_3(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    df['SPSA'] = df['SPSA'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    # breakpoint()
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'TMU' in x
    ) & df['ZONEDIST'].isin(['C6-3'])&  df['SPSA'].apply( lambda x: isinstance(x, list) and 'A2' in x and 'A3' not in x
    ) #C6-3 case
    """special case for C6-3, where SPSA must be A2 and not A3"""
    # cond = (df['SP'][0] == 'BH') & (df['ZONEDIST'].isin(['C4-4A', 'C4-5X', 'R5D'])) 
    
    df_cond = df[cond].copy()
    
    # breakpoint()
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='SNX' y ZONEDIST en ['M1-5/R7D','M1-5/R7X','M1-5/R9A','M1-5/R9X','M1-5/R10','M1-6/R10'] "

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    
    
    
# def test_USE_BULK_SP_LI_SPSD_A_C6_2_C6_2G(df):
#     # breakpoint()
#     df['SP'] = df['SP'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     df['SPSD'] = df['SPSD'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     # breakpoint()
#     cond = df['SP'].apply(
#         lambda x: isinstance(x, list) and 'LI' in x
#     ) & df['ZONEDIST'].isin(['C6-2', 'C6-2G'])&  df['SPSD'].apply( lambda x: isinstance(x, list) and 'A' in x
#     ) #C6-3 case
#     df_cond = df[cond].copy()
    
#     breakpoint()
#     # ✅ Validar que hay datos que cumplen la condición
#     assert not df_cond.empty, "❌ Error: No hay filas con SP='LI' , SPSD = 'A' y ZONEDIST en ['C6-2', 'C6-2G']"

#     # breakpoint()
#     assert (df_cond['BR_R'] == True).all()
#     assert (df_cond['QAH_R'] == True).all()
#     assert (df_cond['BR_CF'] == True).all()
#     assert (df_cond['BR_C'] == True).all()
#     assert (df_cond['BR_M'] == False).all() ## rev
    
#     for col in all_not_columns:
#         assert (df_cond[col] == False).all()
    
    
# def test_USE_BULK_SP_LI_SPSD_A1_C6_2_C6_2G_C6_1(df):
#     # breakpoint()
#     df['SP'] = df['SP'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     df['SPSD'] = df['SPSD'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     # breakpoint()
#     cond = df['SP'].apply(
#         lambda x: isinstance(x, list) and 'LI' in x
#     ) & df['ZONEDIST'].isin(['C6-2', 'C6-2G','C6-1'])&  df['SPSD'].apply( lambda x: isinstance(x, list) and 'A1' in x
#     ) #C6-3 case
#     df_cond = df[cond].copy()
    
#     # breakpoint()
#     # ✅ Validar que hay datos que cumplen la condición
#     assert not df_cond.empty, "❌ Error: No hay filas con SP='LI' , SPSD = 'A1' y ZONEDIST en ['C6-2', 'C6-2G']"

#     # breakpoint()
#     assert (df_cond['BR_R'] == True).all()
#     assert (df_cond['QAH_R'] == True).all()
#     assert (df_cond['BR_CF'] == True).all()
#     assert (df_cond['BR_C'] == True).all()
#     assert (df_cond['BR_M'] == False).all() ## rev
    
#     for col in all_not_columns:
#         assert (df_cond[col] == False).all()
    
    
    
def test_USE_BULK_SP_LI_SPSD_B_C6_3_C6_1_C6_1G(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    df['SPSD'] = df['SPSD'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    # breakpoint()
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'LI' in x
    ) & df['ZONEDIST'].isin(['C6-3', 'C6-1G','C6-1'])&  df['SPSD'].apply( lambda x: isinstance(x, list) and 'B' in x
    ) #C6-3 case
    df_cond = df[cond].copy()
    
    # breakpoint()
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='LI' , SPSD = 'B' y ZONEDIST en ['C6-3', 'C6-1G','C6-1']"

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
    
    
    
# def test_USE_BULK_SP_LI_SPSD_C_C6_1_C6_1G(df):
#     # breakpoint()
#     df['SP'] = df['SP'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     df['SPSD'] = df['SPSD'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
#     # breakpoint()
#     cond = df['SP'].apply(
#         lambda x: isinstance(x, list) and 'LI' in x
#     ) & df['ZONEDIST'].isin(['C6-1G','C6-1'])&  df['SPSD'].apply( lambda x: isinstance(x, list) and 'C' in x
#     ) #C6-3 case
#     df_cond = df[cond].copy()
    
#     breakpoint()
#     # ✅ Validar que hay datos que cumplen la condición
#     assert not df_cond.empty, "❌ Error: No hay filas con SP='LI' , SPSD = 'C' y ZONEDIST en ['C6-1G','C6-1']"

#     # breakpoint()
#     assert (df_cond['BR_R'] == True).all()
#     assert (df_cond['QAH_R'] == True).all()
#     assert (df_cond['BR_CF'] == True).all()
#     assert (df_cond['BR_C'] == True).all()
#     assert (df_cond['BR_M'] == False).all() ## rev
    
#     for col in all_not_columns:
#         assert (df_cond[col] == False).all()



def test_USE_BULK_SP_DJ_not_M1_4(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    
    
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'DJ' in x
    ) & df['ZONEDIST'].isin(['R6A','R7A','R7X'])&(df['OVERLAY'].isin(['C1-1','C1-2','C1-3','C1-4','C1-5','C2-1','C2-2','C2-3','C2-4','C2-5']))
    df_cond = df[cond].copy()
    # breakpoint()
    
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='DJ'  y ZONEDIST en ['R6A','R7A','R7X','C4-4A','C4-5X','C6-2','C6-3','C6-4']"

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()


def test_USE_BULK_SP_DJ_ZD_R_not_OVERLAY(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    
    
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'DJ' in x
    ) & df['ZONEDIST'].isin(['R6A','R7A','R7X'])&(~df['OVERLAY'].isin(['C1-1','C1-2','C1-3','C1-4','C1-5','C2-1','C2-2','C2-3','C2-4','C2-5']))
    df_cond = df[cond].copy()
    # breakpoint()
    
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='DJ'  y ZONEDIST en ['R6A','R7A','R7X','C4-4A','C4-5X','C6-2','C6-3','C6-4']"

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == False).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()


# def test_USE_BULK_SP_DJ_ZD_C_not_M1_4(df):
#     # breakpoint()
#     df['SP'] = df['SP'].apply(
#         lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
#     )   
    
#     cond = df['SP'].apply(
#         lambda x: isinstance(x, list) and 'DJ' in x
#     ) & df['ZONEDIST'].isin(['C4-5X','C6-2','C6-3','C6-4'])
#     df_cond = df[cond].copy()
#     breakpoint()
    
#     # ✅ Validar que hay datos que cumplen la condición
#     assert not df_cond.empty, "❌ Error: No hay filas con SP='DJ'  y ZONEDIST en ['C4-4A','C4-5X','C6-2','C6-3','C6-4']"

#     # breakpoint()
#     assert (df_cond['BR_R'] == True).all()
#     assert (df_cond['QAH_R'] == True).all()
#     assert (df_cond['BR_CF'] == True).all()
#     assert (df_cond['BR_C'] == True).all()
#     assert (df_cond['BR_M'] == False).all() ## rev
    
#     for col in all_not_columns:
#         assert (df_cond[col] == False).all()

# # def DJ_M1_4(df):
# #     pass

def test_USE_BULK_SP_MP(df):
    # breakpoint()
    df['SP'] = df['SP'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x
    )   
    
    # # breakpoint()
    # cond = df['SP'].apply(
    #     lambda x: isinstance(x, list) and 'MP' in x and 'empty' not in  x) & df['ZONEDIST'].isin(['R10','C5-1'])
    cond = df['SP'].apply(
        lambda x: isinstance(x, list) and 'MP' in x and 'empty' not in  x) & df['ZONEDIST'].isin(['R10','C5-1'])
    
    
    df_cond = df[cond].copy()
    # breakpoint()
    
    # ✅ Validar que hay datos que cumplen la condición
    assert not df_cond.empty, "❌ Error: No hay filas con SP='DJ'  y ZONEDIST en ['R6A','R7A','R7X','C4-4A','C4-5X','C6-2','C6-3','C6-4']"

    # breakpoint()
    assert (df_cond['BR_R'] == True).all()
    assert (df_cond['QAH_R'] == True).all()
    assert (df_cond['BR_CF'] == True).all()
    assert (df_cond['BR_C'] == True).all()
    assert (df_cond['BR_M'] == False).all() ## rev
    
    for col in all_not_columns:
        assert (df_cond[col] == False).all()
        
        