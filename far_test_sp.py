import pytest
import pandas as pd


uses = ['R','CF', 'C','M']

columnas = ['FAR_R_BR','FAR_BR_QAH','FAR_CF','FAR_CF_MX','FAR_C','FAR_M']
            # 'FAR_R_BR','FAR_BR_QAH','FAR_CF','FAR_CF_MX','FAR_C','FAR_M'
# columnas = ['FAR_R_BR','FAR_BR_QAH','FAR_CF','FAR_CF_MX','FAR_C','FAR_M']


    
@pytest.fixture(scope="module")
def df():
    return pd.read_csv("RESULT_FAR.csv", sep=';', low_memory=False)

def safe_convert(val):
    try:
        return pd.to_numeric(val)
    except Exception:
        return val


def test_FAR_SP_C(df):
    cond = (df['SP'] == 'C') & (df['ZONEDIST'] == 'R8') 
    df_cond = df[cond].copy()
    
    # breakpoint()
    assert not df_cond.empty, "DataFrame should not be empty for this condition"
    for col in columnas:
        df_cond[col] = df_cond[col].apply(safe_convert)
    
    assert (df_cond['FAR_R_BR'] == 6.02).all()
    assert (df_cond['FAR_BR_QAH'] == 7.2).all()

    assert (df_cond['FAR_CF'] == 6).all()
    assert (df_cond['FAR_CF_MX'] == 6).all()
    
    if (df_cond['NYCO'] == True).all():
        assert (df_cond['FAR_C'] == 2).all()
    elif (df_cond['NYCO'] == False).all():
        assert df_cond['FAR_C'].isna().all()
    
    assert df_cond['FAR_M'].isna().all()
            
    
def test_FAR_SP_FH(df):
    
    #test if the BBL starts with any of the values in valores
    cond1 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X')

    df_cond1 = df[cond1].copy()
    assert not df_cond1.empty, "DataFrame should not be empty for this condition"
    for col in columnas:
        df_cond1[col] = df_cond1[col].apply(safe_convert)
        
    assert (df_cond1['FAR_R_BR'] == 5).all()
    assert (df_cond1['FAR_BR_QAH'] == 6).all()
    assert (df_cond1['FAR_CF'] == 5).all()
    assert (df_cond1['FAR_CF_MX'] == 5).all()

    assert (df_cond1['FAR_C'] == 5).all()
    assert df_cond1['FAR_M'].isna().all()
    
    
    
def test_FAR_SP_MP(df):
    cond1 = (df['SP'] == 'MP') & (df['ZONEDIST'].isin(['C5-1']))
    # breakpoint()
    df_cond1 = df[cond1].copy()

    assert not df_cond1.empty, "DataFrame should not be empty for this condition"
    for col in columnas:
        df_cond1[col] = df_cond1[col].apply(safe_convert)

    # breakpoint()
    assert (df_cond1['FAR_R_BR'] == 10).all()
    assert (df_cond1['FAR_BR_QAH'] == 12).all()
    assert (df_cond1['FAR_CF'] == 10).all()
    assert (df_cond1['FAR_CF_MX'] == 10).all()
    assert (df_cond1['FAR_C'] == 4).all()
    assert df_cond1['FAR_M'].isna().all()


def test_FAR_SP_DJ_C6_2(df):
    
    #test if the BBL starts with any of the values in valores
    cond_c6_2_mih_t_w100ws_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-2') & (df['MIH'] == True) & (df['W100WS'] == True)
    cond_c6_2_mih_t_w100ws_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-2') & (df['MIH'] == True) & (df['W100WS'] == False)
    cond_c6_2_mih_f_w100ws_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-2') & (df['MIH'] == False) & (df['W100WS'] == True)
    cond_c6_2_mih_f_w100ws_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-2') & (df['MIH'] == False) & (df['W100WS'] == False)
    
    
    #C6-2
    df_cond_c6_2_mih_t_w100ws_t = df[cond_c6_2_mih_t_w100ws_t].copy()
    df_cond_c6_2_mih_t_w100ws_f = df[cond_c6_2_mih_t_w100ws_f].copy()
    df_cond_c6_2_mih_f_w100ws_t = df[cond_c6_2_mih_f_w100ws_t].copy()
    df_cond_c6_2_mih_f_w100ws_f = df[cond_c6_2_mih_f_w100ws_f].copy()
    
    
    assert not df_cond_c6_2_mih_t_w100ws_t.empty, "DataFrame should not be empty for this condition"
    assert not df_cond_c6_2_mih_t_w100ws_f.empty, "DataFrame should not be empty for this condition"
    assert not df_cond_c6_2_mih_f_w100ws_t.empty, "DataFrame should not be empty for this condition"
    assert not df_cond_c6_2_mih_f_w100ws_f.empty, "DataFrame should not be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_2_mih_t_w100ws_t[col] = df_cond_c6_2_mih_t_w100ws_t[col].apply(safe_convert) 
        df_cond_c6_2_mih_t_w100ws_f[col] = df_cond_c6_2_mih_t_w100ws_f[col].apply(safe_convert) 
        df_cond_c6_2_mih_f_w100ws_t[col] = df_cond_c6_2_mih_f_w100ws_t[col].apply(safe_convert) 
        df_cond_c6_2_mih_f_w100ws_f[col] = df_cond_c6_2_mih_f_w100ws_f[col].apply(safe_convert)

    assert (df_cond_c6_2_mih_t_w100ws_t['FAR_R_BR'] == 7.2).all()
    assert (df_cond_c6_2_mih_t_w100ws_t['FAR_BR_QAH'] == 7.2).all()
    assert (df_cond_c6_2_mih_t_w100ws_t['FAR_CF'] == 6).all()
    assert (df_cond_c6_2_mih_t_w100ws_t['FAR_CF_MX'] == 6).all()
    assert (df_cond_c6_2_mih_t_w100ws_t['FAR_C'] == 6).all()
    assert df_cond_c6_2_mih_t_w100ws_t['FAR_M'].isna().all()

    assert (df_cond_c6_2_mih_t_w100ws_f['FAR_R_BR'] == 6.02).all()
    assert (df_cond_c6_2_mih_t_w100ws_f['FAR_BR_QAH'] == 7.2).all()
    assert (df_cond_c6_2_mih_t_w100ws_f['FAR_CF'] == 6).all()
    assert (df_cond_c6_2_mih_t_w100ws_f['FAR_CF_MX'] == 6).all()
    assert (df_cond_c6_2_mih_t_w100ws_f['FAR_C'] == 6).all()
    assert  df_cond_c6_2_mih_t_w100ws_f['FAR_M'].isna().all()
    
    assert (df_cond_c6_2_mih_f_w100ws_t['FAR_R_BR'] == 7.2).all()
    assert (df_cond_c6_2_mih_f_w100ws_t['FAR_BR_QAH'] == 8.64).all()
    assert (df_cond_c6_2_mih_f_w100ws_t['FAR_CF'] == 6).all()
    assert (df_cond_c6_2_mih_f_w100ws_t['FAR_CF_MX'] == 6).all()
    assert (df_cond_c6_2_mih_f_w100ws_t['FAR_C'] == 6).all()
    assert  df_cond_c6_2_mih_f_w100ws_t['FAR_M'].isna().all()
    
    assert (df_cond_c6_2_mih_f_w100ws_f['FAR_R_BR'] == 6.02).all()
    assert (df_cond_c6_2_mih_f_w100ws_f['FAR_BR_QAH'] == 7.2).all()
    assert (df_cond_c6_2_mih_f_w100ws_f['FAR_CF'] == 6).all()
    assert (df_cond_c6_2_mih_f_w100ws_f['FAR_CF_MX'] == 6).all()
    assert (df_cond_c6_2_mih_f_w100ws_f['FAR_C'] == 6).all()
    assert  df_cond_c6_2_mih_f_w100ws_f['FAR_M'].isna().all()

            
def test_FAR_SP_DJ_C6_3(df):

    #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-3')
    
    
    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR'] == 7.52).all()
    assert (df_cond_c6_3['FAR_BR_QAH'] == 9.02).all()
    assert (df_cond_c6_3['FAR_CF'] == 8).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 8).all()
    assert (df_cond_c6_3['FAR_C'] == 8).all()
    assert df_cond_c6_3['FAR_M'].isna().all()

    

    #######here########
    
def test_FAR_SP_DJ_C6_4(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-4')
    
    
    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    

    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR'] == 10).all()
    assert (df_cond_c6_3['FAR_BR_QAH'] == 12).all()
    assert (df_cond_c6_3['FAR_CF'] == 10).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 10).all()
    assert (df_cond_c6_3['FAR_C'] == 12).all()
    assert df_cond_c6_3['FAR_M'].isna().all()



    
def test_FAR_SP_DJ_M1_4(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'DJ') & (df['ZONEDIST']=='M1-4')
    
    
    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert df_cond_c6_3['FAR_R_BR'].isna().all()
    assert df_cond_c6_3['FAR_BR_QAH'].isna().all()
    
    assert (df_cond_c6_3['FAR_CF'] == 2).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 2).all()
    assert (df_cond_c6_3['FAR_C'] == 2).all()
    assert (df_cond_c6_3['FAR_M'] == 2).all()


def test_FAR_SP_SNX_M1_5_R7D(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7D')
    
    
    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 4.66).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 5.6).all()
    
    
    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()


def test_FAR_SP_SNX_M1_5_R7X(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7X')
    
    
    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 6).all()
    
    
    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()
    
def test_FAR_SP_SNX_M1_5_R9A(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R9A')


    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 7.52).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 8.5).all()
    
    
    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()
    
def test_FAR_SP_SNX_M1_5_R9X_block_531(df):
    "corrections in next iteration"
    
    valores = ['100531']
    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') &(df['BBL'].astype(str).str.startswith(tuple(valores)))& (df['ZONEDIST']=='M1-5/R9X')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 9).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 10.8).all()
    
    
    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()
    
def test_FAR_SP_SNX_M1_5_R9X_no_block_531(df):
    "corrections in next iteration"
    valores = ['100531']
    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') &(~df['BBL'].astype(str).str.startswith(tuple(valores)))& (df['ZONEDIST']=='M1-5/R9X')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 9).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 9.7).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()
    


def test_FAR_SP_SNX_M1_5_R10(df):

    #  #test if the BBL starts with any of the values in valores
    cond_c6_3 = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R10')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 10).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()
    
    
    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert (df_cond_c6_3['FAR_M'] == 5).all()
    
    
def test_FAR_SP_SNX_M1_6_R10_no_block(df):
    "corrections in next iteration"
    block = ['100531','100544']
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'SNX') &(~df['BBL'].astype(str).str.startswith(tuple(block)))& (df['ZONEDIST']=='M1-6/R10')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 10).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 10).all()
    assert (df_cond_c6_3['FAR_M'] == 10).all()
    
def test_FAR_SP_SNX_M1_6_R10_block(df):
    "corrections in next iteration"
    block = ['100531','100544']
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'SNX') &(df['BBL'].astype(str).str.startswith(tuple(block)))& (df['ZONEDIST']=='M1-6/R10')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    

    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 10).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 7).all()
    assert (df_cond_c6_3['FAR_M'] == 7).all()
    
    
    
def test_FAR_SP_HSQ_no_A_M1_6(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'HSQ')&(df['ZONEDIST']=='M1-6')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 10).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()


    assert (df_cond_c6_3['FAR_CF'] == 10).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 10).all()
    assert (df_cond_c6_3['FAR_C'] == 10).all()
    assert (df_cond_c6_3['FAR_M'] == 10).all()
    
    

def test_FAR_SP_TMU_SPSA_A1_C6_2A(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A1')&(df['ZONEDIST']=='C6-2A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 6).all()


    assert (df_cond_c6_3['FAR_CF'] == 5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 5).all()
    assert (df_cond_c6_3['FAR_C'] == 5).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
    
    
def test_FAR_SP_TMU_SPSA_A2_C6_3(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A2')&(df['ZONEDIST']=='C6-3')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 7.52).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 9.02).all()


    assert (df_cond_c6_3['FAR_CF'] == 6).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
    
    
def test_FAR_SP_TMU_SPSA_A3_C6_3A(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A3')&(df['ZONEDIST']=='C6-3A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 7.52).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 9.02).all()


    assert (df_cond_c6_3['FAR_CF'] == 7.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 7.5).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_TMU_SPSA_A4_C6_3A(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A4')&(df['ZONEDIST']=='C6-3A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 6.5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 7.8).all()


    assert (df_cond_c6_3['FAR_CF'] == 7.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 7.5).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_TMU_SPSA_A5_C6_2A(df):
    "corrections in next iteration"
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A5')&(df['ZONEDIST']=='C6-2A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 5.5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 6.6).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_TMU_SPSA_A6_C6_2A(df):
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A6')&(df['ZONEDIST']=='C6-2A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 6).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 7.2).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    

def test_FAR_SP_TMU_SPSA_A7_C6_2A(df):
    
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'TMU')&(df['SPSA'] == 'A7')&(df['ZONEDIST']=='C6-2A')

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 6).all()


    assert (df_cond_c6_3['FAR_CF'] == 6.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 6.5).all()
    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
    
"""in CL test only zd with changes"""
"""more cases in R8"""

# def test_FAR_SP_CL_SPSA_A_R8_no_OVERLAY(df):
    
#     #  #test if the BBL starts with any of the values in block
#     cond_c6_3 = (df['SP'] == 'CL')&(df['SPSA'] == 'A')&(df['ZONEDIST']=='R8')

#     #C6-2
#     df_cond_c6_3 = df[cond_c6_3].copy()
#     for col in columnas:
        
#         df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
#     assert (df_cond_c6_3['FAR_R_BR']== 4.2).all()
#     assert (df_cond_c6_3['FAR_BR_QAH']== 5.04).all()


#     assert (df_cond_c6_3['FAR_CF'] == 4.2).all()
#     assert (df_cond_c6_3['FAR_CF_MX'] == 4.2).all()
    
#     assert (df_cond_c6_3['FAR_C'] == 6).all()
#     assert df_cond_c6_3['FAR_M'].isna().all()


def test_FAR_SP_CL_SPSA_C2_R9_no_OVERLAY(df):

    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'CL')&(df['SPSA'] == 'C2')&(df['ZONEDIST']=='R9')&(df['NYCO']== False)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 6.66).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 8).all()


    assert (df_cond_c6_3['FAR_CF'] == 10).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 10).all()
    
    assert df_cond_c6_3['FAR_C'].isna().all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_CL_SPSA_C2_R9_OVERLAY(df):

    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'CL')&(df['SPSA'] == 'C2')&(df['ZONEDIST']=='R9')&(df['NYCO']==True)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 6.66).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 8).all()


    assert (df_cond_c6_3['FAR_CF'] == 10).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 10).all()
    
    assert (df_cond_c6_3['FAR_C'] == 2).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_LI_SPSD_A_C6_2_C6_2G_W100C(df):

    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LI')&(df['SPSD'] == 'A')&(df['ZONEDIST'].isin(['C6-2','C6-2G']))&(df['W100C']==True)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 4.8).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 5.76).all()


    assert (df_cond_c6_3['FAR_CF'] == 4.8).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 4.8).all()
    
    assert (df_cond_c6_3['FAR_C'] == 4.8).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    

def test_FAR_SP_LI_SPSD_A_C6_2_C6_2G_NO_W100C(df):

    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LI')&(df['SPSD'] == 'A')&(df['ZONEDIST'].isin(['C6-2','C6-2G']))&(df['W100C']==False)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 4.1).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 4.92).all()


    assert (df_cond_c6_3['FAR_CF'] == 4.1).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 4.1).all()

    assert (df_cond_c6_3['FAR_C'] == 4.1).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_LI_SPSD_A1_C6_2_C6_2G_C6_1_W100C(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LI')&(df['SPSD'] == 'A1')&(df['ZONEDIST'].isin(['C6-2','C6-2G','C6-1']))&(df['W100C']==True)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 4.1).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 4.92).all()


    assert (df_cond_c6_3['FAR_CF'] == 4.1).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 4.1).all()

    assert (df_cond_c6_3['FAR_C'] == 5.1).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_LI_SPSD_A1_C6_2_C6_2G_C6_1_NO_W100C(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LI')&(df['SPSD'] == 'A1')&(df['ZONEDIST'].isin(['C6-2','C6-2G','C6-1']))&(df['W100C']==False)

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 3.5).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 4.2).all()


    assert (df_cond_c6_3['FAR_CF'] == 3.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 3.5).all()

    assert (df_cond_c6_3['FAR_C'] == 4.5).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
def test_FAR_SP_LI_SPSD_B_C6_3(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LI')&(df['SPSD'] == 'B')&(df['ZONEDIST'].isin(['C6-3']))

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 7.52).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 9.02).all()


    assert (df_cond_c6_3['FAR_CF'] == 7.5).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 7.5).all()

    assert (df_cond_c6_3['FAR_C'] == 6).all()
    assert df_cond_c6_3['FAR_M'].isna().all()
    
    
def test_FAR_SP_LIC_SPSD_QPS_AREA_1_M6_R10(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LIC')&(df['SPSD'] == 'Queens Plaza Subdistrict')&(df['SPSA'] == 'Area A-1')&(df['ZONEDIST'].isin(['M1-6/R10']))

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 12).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()


    assert (df_cond_c6_3['FAR_CF'] == 12).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 12).all()

    assert (df_cond_c6_3['FAR_C'] == 12).all()
    assert (df_cond_c6_3['FAR_M'] == 12).all()
    
def test_FAR_SP_LIC_SPSD_QPS_AREA_2_M6_R10(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LIC')&(df['SPSD'] == 'Queens Plaza Subdistrict')&(df['SPSA'] == 'Area A-2')&(df['ZONEDIST'].isin(['M1-6/R10']))

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 12).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 12).all()


    assert (df_cond_c6_3['FAR_CF'] == 12).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 12).all()

    assert (df_cond_c6_3['FAR_C'] == 12).all()
    assert (df_cond_c6_3['FAR_M'] == 12).all()
    
def test_FAR_SP_LIC_SPSD_QPS_AREA_B_M1_5_R9(df):
    """corrections in next iteration"""
    #  #test if the BBL starts with any of the values in block
    cond_c6_3 = (df['SP'] == 'LIC')&(df['SPSD'] == 'Queens Plaza Subdistrict')&(df['SPSA'] == 'Area B')&(df['ZONEDIST'].isin(['M1-5/R9']))

    #C6-2
    df_cond_c6_3 = df[cond_c6_3].copy()
    # breakpoint()
    assert not df_cond_c6_3.empty, "DataFrame should be empty for this condition"
    
    # breakpoint()
    for col in columnas:
        
        df_cond_c6_3[col] = df_cond_c6_3[col].apply(safe_convert) 
        
    assert (df_cond_c6_3['FAR_R_BR']== 8).all()
    assert (df_cond_c6_3['FAR_BR_QAH']== 8).all()


    assert (df_cond_c6_3['FAR_CF'] == 8).all()
    assert (df_cond_c6_3['FAR_CF_MX'] == 8).all()

    assert (df_cond_c6_3['FAR_C'] == 8).all()
    assert (df_cond_c6_3['FAR_M'] == 8).all()