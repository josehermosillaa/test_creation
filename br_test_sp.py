import pytest
import pandas as pd


uses = ['CF', 'C','M']

columnas = ['R_BH_MIN', 'BR_R_BH_MAX', 'QAH_R_BH_MAX', 'BR_R_HEIGHT', 'QAH_R_HEIGHT']
for use in uses:
    columnas.append(rf'{use}_BH_MIN')
    columnas.append(rf'BR_{use}_BH_MAX')
    columnas.append(rf'BR_{use}_HEIGHT')

@pytest.fixture(scope="module")
def df():
    df = pd.read_csv("BR_REGULATION_C_SP.csv", sep=';', low_memory=False)
    df = df[df['SA'] != 'WFB'].copy()
    df = df.replace({'true': True, 'false': False, 'True': True, 'False': False})
    return df

def safe_convert(val):
    try:
        return pd.to_numeric(val)
    except Exception:
        return val

def test_BR_SP_C(df):
    cond1 = (df['SP'] == 'C') & (df['ZONEDIST'] == 'R8') & (df['SB'] == True)
    cond2 = (df['SP'] == 'C') & (df['ZONEDIST'] == 'R8') & (df['SB'] == False)

    df_cond1 = df[cond1].copy()
    df_cond2 = df[cond2].copy()

    
    for col in columnas:
        df_cond1[col] = df_cond1[col].apply(safe_convert)
        df_cond2[col] = df_cond2[col].apply(safe_convert)

    assert (df_cond1['R_BH_MIN'] == 60).all()
    assert (df_cond1['BR_R_BH_MAX'] == 95).all()
    assert (df_cond1['QAH_R_BH_MAX'] == 105).all()
    assert (df_cond2['BR_R_HEIGHT'] == 155).all()
    assert (df_cond2['QAH_R_HEIGHT'] == 175).all()

    for use in uses:
        if use in ['R','CF']:
            assert (df_cond1[rf'{use}_BH_MIN'] == 60).all()
            assert (df_cond1[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_cond2[rf'BR_{use}_HEIGHT'] == 155).all()
        elif use == 'M':
            if (df_cond1['NYCO']).all():
                assert (df_cond1[rf'{use}_BH_MIN'] == 60).all()
                assert (df_cond1[rf'BR_{use}_BH_MAX'] == 95).all()
                assert (df_cond2[rf'BR_{use}_HEIGHT'] == 155).all()
        elif use == 'M':
            assert df_cond1[rf'{use}_BH_MIN'].isna().all()
            assert df_cond1[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond2[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_cond2[rf'BR_{use}']==False).all()
            
    

def test_BR_SP_FH(df):
    valores = '403237', '403236', '403236'
    #test if the BBL starts with any of the values in valores
    cond1 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X')&(df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == True)
    cond2 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X')&(df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == False)
    # cond2 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X') & (df['SB'] == False)
    # breakpoint()
    df_cond1 = df[cond1].copy()
    df_cond2 = df[cond2].copy()

    
    for col in columnas:
        df_cond1[col] = df_cond1[col].apply(safe_convert)
        df_cond2[col] = df_cond2[col].apply(safe_convert)

    assert (df_cond1['R_BH_MIN'] == 40).all()
    assert (df_cond1['BR_R_BH_MAX'] == 95).all()
    assert (df_cond1['QAH_R_BH_MAX'] == 105).all()
    assert (df_cond2['BR_R_HEIGHT'] == 125).all()
    assert (df_cond2['QAH_R_HEIGHT'] == 145).all()

    for use in uses:
        if use != 'M':
            assert (df_cond1[rf'{use}_BH_MIN'] == 40).all()
            assert (df_cond1[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_cond2[rf'BR_{use}_HEIGHT'] == 125).all()
        else:
            assert df_cond1[rf'{use}_BH_MIN'].isna().all()
            assert df_cond1[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond2[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_cond2[rf'BR_{use}'] == False).all()
            
    
def test_BR_SP_MP(df):
##todo rev if nyco is true and is false for values in R10
    #test if the BBL starts with any of the values in valores
    cond1 = (df['SP'] == 'MP') & (df['ZONEDIST'].isin(['R10','C5-1']))&(df['W100WS'] == True) & (df['SB'] == True)
    cond2 = (df['SP'] == 'MP') & (df['ZONEDIST'].isin(['R10','C5-1']))&(df['W100WS'] == True) &(df['SB'] == False)
    
    cond3 = (df['SP'] == 'MP') & (df['ZONEDIST'].isin(['R10','C5-1']))&(df['W100WS'] == False)& (df['SB'] == True)
    cond4 = (df['SP'] == 'MP') & (df['ZONEDIST'].isin(['R10','C5-1']))&(df['W100WS'] == False)& (df['SB'] == False)
    # cond2 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X') & (df['SB'] == False)
    # breakpoint()
    df_cond1 = df[cond1].copy()
    df_cond2 = df[cond2].copy()
    df_cond3 = df[cond3].copy()
    df_cond4 = df[cond4].copy()

    
    for col in columnas:
        df_cond1[col] = df_cond1[col].apply(safe_convert)
        df_cond2[col] = df_cond2[col].apply(safe_convert)
        df_cond3[col] = df_cond3[col].apply(safe_convert)
        df_cond4[col] = df_cond4[col].apply(safe_convert)
    #W100WS = True
    #SB True
    assert (df_cond1['R_BH_MIN'] == 125).all()
    assert (df_cond1['BR_R_BH_MAX'] == 155).all()
    assert (df_cond1['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_cond2['BR_R_HEIGHT'] == 215).all()
    assert (df_cond2['QAH_R_HEIGHT'] == 235).all()
    
    #W100WS = False
    #SB True
    assert (df_cond3['R_BH_MIN'] == 60).all()
    assert (df_cond3['BR_R_BH_MAX'] == 125).all()
    assert (df_cond3['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_cond4['BR_R_HEIGHT'] == 185).all()
    assert (df_cond4['QAH_R_HEIGHT'] == 235).all()
    
    for use in uses:
        if use in ['R', 'CF']:
            assert (df_cond1[rf'{use}_BH_MIN'] == 125).all()
            assert (df_cond1[rf'BR_{use}_BH_MAX'] == 155).all()
            assert (df_cond2[rf'BR_{use}_HEIGHT'] == 215).all()
            
            assert (df_cond3[rf'{use}_BH_MIN'] == 60).all()
            assert (df_cond3[rf'BR_{use}_BH_MAX'] == 125).all()
            assert (df_cond4[rf'BR_{use}_HEIGHT'] == 185).all()
        elif use == 'C':
            if (df_cond1['NYCO']).all():
                assert (df_cond1[rf'{use}_BH_MIN'] == 125).all()
                assert (df_cond1[rf'BR_{use}_BH_MAX'] == 155).all()
                assert (df_cond2[rf'BR_{use}_HEIGHT'] == 215).all()
                
                assert (df_cond3[rf'{use}_BH_MIN'] == 60).all()
                assert (df_cond3[rf'BR_{use}_BH_MAX'] == 125).all()
                assert (df_cond4[rf'BR_{use}_HEIGHT'] == 185).all()
        elif use == 'M':
            assert df_cond1[rf'{use}_BH_MIN'].isna().all()
            assert df_cond1[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond2[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_cond2[rf'BR_{use}']==False).all()
            
            assert df_cond3[rf'{use}_BH_MIN'].isna().all()
            assert df_cond3[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond4[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_cond4[rf'BR_{use}']==False).all()
            
        

def test_BR_SP_DJ_C4_5X(df):

    #test if the BBL starts with any of the values in valores
    cond_c4_5x_sb_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C4-5X') & (df['SB'] == True)
    cond_c4_5x_sb_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C4-5X') & (df['SB'] == False)
    
    
    #C6-2
    
    df_c4_5x_sb_t = df[cond_c4_5x_sb_t].copy() 
    df_c4_5x_sb_f = df[cond_c4_5x_sb_f].copy()
    
    for col in columnas:
        df_c4_5x_sb_t[col] = df_c4_5x_sb_t[col].apply(safe_convert)
        df_c4_5x_sb_f[col] = df_c4_5x_sb_f[col].apply(safe_convert)
        

    # C4-5X
    #SB True
    assert (df_c4_5x_sb_t['R_BH_MIN'] == 40).all()
    assert (df_c4_5x_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_c4_5x_sb_t['QAH_R_BH_MAX'] == 105).all()
    #SB False
    assert (df_c4_5x_sb_f['BR_R_HEIGHT'] == 125).all()
    assert (df_c4_5x_sb_f['QAH_R_HEIGHT'] == 145).all()
    #breakpoint()
    for use in uses:
        if use != 'M':
            assert (df_c4_5x_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_c4_5x_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_c4_5x_sb_f[rf'BR_{use}_HEIGHT'] == 125).all()
        else:
            assert df_c4_5x_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_c4_5x_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_c4_5x_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (df_c4_5x_sb_f[rf'BR_{use}']==False).all() #entrega como NAN revision!



    
    
def test_BR_SP_DJ_C6_2(df):
    
    #C6-2
    
    cond1 = (df['SP'] == 'DJ') & (df['ZONEDIST'] == 'C6-2') & (df['ES'] == True)
    cond2 = (df['SP'] == 'DJ') & (df['ZONEDIST'] == 'C6-2') & (df['ES'] == False)&(df['MIH']==True)
    
    cond3 = (df['SP'] == 'DJ') & (df['ZONEDIST'] == 'C6-2') & (df['ES'] == False)&(df['MIH']==False)
    
    final_cond_c6_2_w100ws_t_sb_t =(cond1|cond2)&(df['W100WS'] == True) & (df['SB'] == True)
    final_cond_c6_2_w100ws_t_sb_f =(cond1|cond2)&(df['W100WS'] == True) & (df['SB'] == False)
    final_cond_c6_2_w100ws_f_sb_t =(cond1|cond2)&(df['W100WS'] == False) & (df['SB'] == True)
    final_cond_c6_2_w100ws_f_sb_f =(cond1|cond2)&(df['W100WS'] == False) & (df['SB'] == False)
    
    
    final_cond3_c6_2_w100ws_t_sb_t = cond3 & (df['W100WS'] == True) & (df['SB'] == True)
    final_cond3_c6_2_w100ws_t_sb_f = cond3 & (df['W100WS'] == True) & (df['SB'] == False)
    final_cond3_c6_2_w100ws_f_sb_t = cond3 & (df['W100WS'] == False) & (df['SB'] == True)
    final_cond3_c6_2_w100ws_f_sb_f = cond3 & (df['W100WS'] == False) & (df['SB'] == False)
    

    final_cond_c6_2_w100ws_t_sb_t = df[final_cond_c6_2_w100ws_t_sb_t].copy()
    final_cond_c6_2_w100ws_t_sb_f = df[final_cond_c6_2_w100ws_t_sb_f].copy()
    final_cond_c6_2_w100ws_f_sb_t = df[final_cond_c6_2_w100ws_f_sb_t].copy()
    final_cond_c6_2_w100ws_f_sb_f = df[final_cond_c6_2_w100ws_f_sb_f].copy()
    
    final_cond3_c6_2_w100ws_t_sb_t = df[final_cond3_c6_2_w100ws_t_sb_t].copy()
    final_cond3_c6_2_w100ws_t_sb_f = df[final_cond3_c6_2_w100ws_t_sb_f].copy()
    final_cond3_c6_2_w100ws_f_sb_t = df[final_cond3_c6_2_w100ws_f_sb_t].copy()
    final_cond3_c6_2_w100ws_f_sb_f = df[final_cond3_c6_2_w100ws_f_sb_f].copy()
    

    
    for col in columnas:
        final_cond_c6_2_w100ws_t_sb_t[col] = final_cond_c6_2_w100ws_t_sb_t[col].apply(safe_convert)
        final_cond_c6_2_w100ws_t_sb_f[col] = final_cond_c6_2_w100ws_t_sb_f[col].apply(safe_convert)
        final_cond_c6_2_w100ws_f_sb_t[col] = final_cond_c6_2_w100ws_f_sb_t[col].apply(safe_convert)
        final_cond_c6_2_w100ws_f_sb_f[col] = final_cond_c6_2_w100ws_f_sb_f[col].apply(safe_convert)
        
        final_cond3_c6_2_w100ws_t_sb_t[col] = final_cond3_c6_2_w100ws_t_sb_t[col].apply(safe_convert)
        final_cond3_c6_2_w100ws_t_sb_f[col] = final_cond3_c6_2_w100ws_t_sb_f[col].apply(safe_convert)
        final_cond3_c6_2_w100ws_f_sb_t[col] = final_cond3_c6_2_w100ws_f_sb_t[col].apply(safe_convert)
        final_cond3_c6_2_w100ws_f_sb_f[col] = final_cond3_c6_2_w100ws_f_sb_f[col].apply(safe_convert)
        

    # C6-2
    
    assert (final_cond_c6_2_w100ws_t_sb_t['R_BH_MIN'] == 40).all()
    assert (final_cond_c6_2_w100ws_t_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (final_cond_c6_2_w100ws_t_sb_t['QAH_R_BH_MAX'] == 105).all()
    assert (final_cond_c6_2_w100ws_t_sb_f['BR_R_HEIGHT'] == 250).all()
    assert (final_cond_c6_2_w100ws_t_sb_f['QAH_R_HEIGHT'] == 250).all()
    
    assert (final_cond_c6_2_w100ws_f_sb_t['R_BH_MIN'] == 40).all()
    assert (final_cond_c6_2_w100ws_f_sb_t['BR_R_BH_MAX'] == 85).all()
    assert (final_cond_c6_2_w100ws_f_sb_t['QAH_R_BH_MAX'] == 105).all()
    assert (final_cond_c6_2_w100ws_f_sb_f['BR_R_HEIGHT'] == 250).all()
    assert (final_cond_c6_2_w100ws_f_sb_f['QAH_R_HEIGHT'] == 250).all()
    
    assert (final_cond3_c6_2_w100ws_t_sb_t['R_BH_MIN'] == 40).all()
    assert (final_cond3_c6_2_w100ws_t_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (final_cond3_c6_2_w100ws_t_sb_t['QAH_R_BH_MAX'] == 125).all()
    assert (final_cond3_c6_2_w100ws_t_sb_f['BR_R_HEIGHT'] == 250).all()
    assert (final_cond3_c6_2_w100ws_t_sb_f['QAH_R_HEIGHT'] == 250).all()
    
    assert (final_cond3_c6_2_w100ws_f_sb_t['R_BH_MIN'] == 40).all()
    assert (final_cond3_c6_2_w100ws_f_sb_t['BR_R_BH_MAX'] == 85).all()
    assert (final_cond3_c6_2_w100ws_f_sb_t['QAH_R_BH_MAX'] == 105).all()
    assert (final_cond3_c6_2_w100ws_f_sb_f['BR_R_HEIGHT'] == 250).all()
    assert (final_cond3_c6_2_w100ws_f_sb_f['QAH_R_HEIGHT'] == 250).all()
    
    
    for use in uses:
        if use != 'M':
            assert (final_cond_c6_2_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (final_cond_c6_2_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (final_cond_c6_2_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
            
        
            assert (final_cond_c6_2_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (final_cond_c6_2_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 85).all()
            assert (final_cond_c6_2_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
            

            assert (final_cond3_c6_2_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (final_cond3_c6_2_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (final_cond3_c6_2_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
            

            assert (final_cond3_c6_2_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (final_cond3_c6_2_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 85).all()
            assert (final_cond3_c6_2_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
            
        else:
            assert final_cond_c6_2_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert final_cond_c6_2_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert final_cond_c6_2_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (final_cond_c6_2_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert final_cond_c6_2_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert final_cond_c6_2_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert final_cond_c6_2_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (final_cond_c6_2_w100ws_f_sb_f[rf'BR_{use}']==False).all()
            
            
            assert final_cond3_c6_2_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert final_cond3_c6_2_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert final_cond3_c6_2_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (final_cond3_c6_2_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            
            assert final_cond3_c6_2_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert final_cond3_c6_2_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert final_cond3_c6_2_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (final_cond3_c6_2_w100ws_f_sb_f[rf'BR_{use}']==False).all()
            


    #######here########
    
def test_BR_SP_DJ_C6_3(df):

    #test if the BBL starts with any of the values in valores
    cond_c6_3_w100ws_t_sb_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-3') & (df['W100WS'] == True)& (df['SB'] == True)
    cond_c6_3_w100ws_t_sb_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-3') & (df['W100WS'] == True)& (df['SB'] == False)
    
    cond_c6_3_w100ws_f_sb_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-3') & (df['W100WS'] == False)& (df['SB'] == True)
    cond_c6_3_w100ws_f_sb_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-3') & (df['W100WS'] == False)& (df['SB'] == False)
    
    
    df_c6_3_w100ws_t_sb_t = df[cond_c6_3_w100ws_t_sb_t].copy()
    df_c6_3_w100ws_t_sb_f = df[cond_c6_3_w100ws_t_sb_f].copy()
    df_c6_3_w100ws_f_sb_t = df[cond_c6_3_w100ws_f_sb_t].copy()
    df_c6_3_w100ws_f_sb_f = df[cond_c6_3_w100ws_f_sb_f].copy()
    
    
    # df_cond3 = df[cond3].copy()
    # df_cond4 = df[cond4].copy()

    
    for col in columnas:
        df_c6_3_w100ws_t_sb_t[col] = pd.to_numeric(df_c6_3_w100ws_t_sb_t[col], errors='coerce')
        df_c6_3_w100ws_t_sb_f[col] = pd.to_numeric(df_c6_3_w100ws_t_sb_f[col], errors='coerce')
        df_c6_3_w100ws_f_sb_t[col] = pd.to_numeric(df_c6_3_w100ws_f_sb_t[col], errors='coerce')
        df_c6_3_w100ws_f_sb_f[col] = pd.to_numeric(df_c6_3_w100ws_f_sb_f[col], errors='coerce')
        
        
    # C6-3
    #SB True
    assert (df_c6_3_w100ws_t_sb_t['R_BH_MIN'] == 40).all()
    assert (df_c6_3_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_c6_3_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    #SB False
    assert (df_c6_3_w100ws_t_sb_f['BR_R_HEIGHT'] == 250).all()  
    assert (df_c6_3_w100ws_t_sb_f['QAH_R_HEIGHT'] == 250).all()

    assert (df_c6_3_w100ws_f_sb_t['R_BH_MIN'] == 40).all()
    assert (df_c6_3_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_c6_3_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    #SB False
    assert (df_c6_3_w100ws_f_sb_f['BR_R_HEIGHT'] == 250).all()  
    assert (df_c6_3_w100ws_f_sb_f['QAH_R_HEIGHT'] == 250).all()
    
    for use in uses:
        if use != 'M':
            assert (df_c6_3_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_c6_3_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_c6_3_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
        
            assert (df_c6_3_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_c6_3_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_c6_3_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 250).all()
        else:
            assert df_c6_3_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_c6_3_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_c6_3_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (df_c6_3_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_c6_3_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_c6_3_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_c6_3_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (df_c6_3_w100ws_f_sb_f[rf'BR_{use}']==False).all()
            
            
            



    
def test_BR_SP_DJ_C6_4(df):

    #test if the BBL starts with any of the values in valores
    cond_c6_4_w100ws_t_sb_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-4') & (df['W100WS'] == True)& (df['SB'] == True)
    cond_c6_4_w100ws_t_sb_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-4') & (df['W100WS'] == True)& (df['SB'] == False)
    
    cond_c6_4_w100ws_f_sb_t = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-4') & (df['W100WS'] == False)& (df['SB'] == True)
    cond_c6_4_w100ws_f_sb_f = (df['SP'] == 'DJ') & (df['ZONEDIST']=='C6-4') & (df['W100WS'] == False)& (df['SB'] == False)
    
    
    df_c6_4_w100ws_t_sb_t = df[cond_c6_4_w100ws_t_sb_t].copy() 
    df_c6_4_w100ws_t_sb_f = df[cond_c6_4_w100ws_t_sb_f].copy()
    df_c6_4_w100ws_f_sb_t = df[cond_c6_4_w100ws_f_sb_t].copy()
    df_c6_4_w100ws_f_sb_f = df[cond_c6_4_w100ws_f_sb_f].copy()
    
    
    # df_cond3 = df[cond3].copy()
    # df_cond4 = df[cond4].copy()

    
    for col in columnas:
        df_c6_4_w100ws_t_sb_t[col] = pd.to_numeric(df_c6_4_w100ws_t_sb_t[col], errors='coerce')
        df_c6_4_w100ws_t_sb_f[col] = pd.to_numeric(df_c6_4_w100ws_t_sb_f[col], errors='coerce')
        df_c6_4_w100ws_f_sb_t[col] = pd.to_numeric(df_c6_4_w100ws_f_sb_t[col], errors='coerce')
        df_c6_4_w100ws_f_sb_f[col] = pd.to_numeric(df_c6_4_w100ws_f_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_c6_4_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_c6_4_w100ws_t_sb_t['BR_R_BH_MAX'] == 155).all()
    assert (df_c6_4_w100ws_t_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_c6_4_w100ws_t_sb_f['BR_R_HEIGHT'] == 290).all()  
    assert (df_c6_4_w100ws_t_sb_f['QAH_R_HEIGHT'] == 290).all()

    assert (df_c6_4_w100ws_f_sb_t['R_BH_MIN'] == 40).all()
    assert (df_c6_4_w100ws_f_sb_t['BR_R_BH_MAX'] == 125).all()
    assert (df_c6_4_w100ws_f_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_c6_4_w100ws_f_sb_f['BR_R_HEIGHT'] == 290).all()  
    assert (df_c6_4_w100ws_f_sb_f['QAH_R_HEIGHT'] == 290).all()
    
    for use in uses:
        if use != 'M':
            assert (df_c6_4_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_c6_4_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 155).all()
            assert (df_c6_4_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 290).all()
            
            assert (df_c6_4_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_c6_4_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 125).all()
            assert (df_c6_4_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 290).all()
        else:
            assert df_c6_4_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_c6_4_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_c6_4_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (df_c6_4_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_c6_4_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_c6_4_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_c6_4_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            #assert (df_c6_4_w100ws_f_sb_f[rf'BR_{use}']==False).all()
            

    
def test_BR_SP_SNX_M1_5_R7D(df):

    #test if the BBL starts with any of the values in valores
    cond1_sb_t = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7D') & (df['MIH'] == True)& (df['SB'] == True)
    cond1_sb_f = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7D') & (df['MIH'] == True)& (df['SB'] == False)
    
    
    
    df_cond1_sb_t = df[cond1_sb_t].copy() 
    df_cond1_sb_f = df[cond1_sb_f].copy()

    
    for col in columnas:
        df_cond1_sb_t[col] = pd.to_numeric(df_cond1_sb_t[col], errors='coerce')
        df_cond1_sb_f[col] = pd.to_numeric(df_cond1_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_cond1_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_cond1_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_cond1_sb_t['QAH_R_BH_MAX'] == 105).all()
    #SB False
    assert (df_cond1_sb_f['BR_R_HEIGHT'] == 115).all()  
    assert (df_cond1_sb_f['QAH_R_HEIGHT'] == 115).all()
    
    for use in uses:
        assert (df_cond1_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond1_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
        assert (df_cond1_sb_f[rf'BR_{use}_HEIGHT'] == 115).all()
        

def test_BR_SP_SNX_M1_5_R7X(df):

    #test if the BBL starts with any of the values in valores
    cond1_sb_t = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7X') & (df['MIH'] == True)& (df['SB'] == True)
    cond1_sb_f = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R7X') & (df['MIH'] == True)& (df['SB'] == False)
    
    
    
    df_cond1_sb_t = df[cond1_sb_t].copy() 
    df_cond1_sb_f = df[cond1_sb_f].copy()


    
    for col in columnas:
        df_cond1_sb_t[col] = pd.to_numeric(df_cond1_sb_t[col], errors='coerce')
        df_cond1_sb_f[col] = pd.to_numeric(df_cond1_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_cond1_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_cond1_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_cond1_sb_t['QAH_R_BH_MAX'] == 105).all()
    #SB False
    assert (df_cond1_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_cond1_sb_f['QAH_R_HEIGHT'] == 145).all()
    
    for use in uses:
        assert (df_cond1_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond1_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
        assert (df_cond1_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()


def test_BR_SP_SNX_M1_5_R9X_not_100531(df):
    valores = '100531',
    #test if the BBL starts with any of the values in valores
    cond1 = (df['SP'] == 'SNX') & (df['ZONEDIST'] == 'M1-5/R9X')&(df['MIH'] == True)&(~df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == True)
    cond2 = (df['SP'] == 'SNX') & (df['ZONEDIST'] == 'M1-5/R9X')&(df['MIH'] == True)&(~df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == False)
    # cond2 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X') & (df['SB'] == False)
    # breakpoint()
    df_cond1 = df[cond1].copy()
    df_cond2 = df[cond2].copy()

    
    for col in columnas:
        df_cond1[col] = pd.to_numeric(df_cond1[col], errors='coerce')
        df_cond2[col] = pd.to_numeric(df_cond2[col], errors='coerce')

    assert (df_cond1['R_BH_MIN'] == 85).all()
    assert (df_cond1['BR_R_BH_MAX'] == 145).all()
    assert (df_cond1['QAH_R_BH_MAX'] == 145).all()
    assert (df_cond2['BR_R_HEIGHT'] == 205).all()
    assert (df_cond2['QAH_R_HEIGHT'] == 205).all()
    
    for use in uses:
        assert (df_cond1[rf'{use}_BH_MIN'] == 85).all()
        assert (df_cond1[rf'BR_{use}_BH_MAX'] == 145).all()
        assert (df_cond2[rf'BR_{use}_HEIGHT'] == 205).all()
        
        

def test_BR_SP_SNX_M1_5_R9X_100531(df):
    valores = '100531',
    #test if the BBL starts with any of the values in valores
    cond1 = (df['SP'] == 'SNX') & (df['ZONEDIST'] == 'M1-5/R9X')&(df['MIH'] == True)&(df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == True)
    cond2 = (df['SP'] == 'SNX') & (df['ZONEDIST'] == 'M1-5/R9X')&(df['MIH'] == True)&(df['BBL'].astype(str).str.startswith(tuple(valores))) & (df['SB'] == False)
    # cond2 = (df['SP'] == 'FH') & (df['ZONEDIST'] == 'C4-5X') & (df['SB'] == False)
    # breakpoint()
    df_cond1 = df[cond1].copy()
    df_cond2 = df[cond2].copy()

    
    for col in columnas:
        df_cond1[col] = pd.to_numeric(df_cond1[col], errors='coerce')
        df_cond2[col] = pd.to_numeric(df_cond2[col], errors='coerce')

    assert (df_cond1['R_BH_MIN'] == 60).all()
    assert (df_cond1['BR_R_BH_MAX'] == 125).all()
    assert (df_cond1['QAH_R_BH_MAX'] == 125).all()
    assert (df_cond2['BR_R_HEIGHT'] == 195).all()
    assert (df_cond2['QAH_R_HEIGHT'] == 195).all()
    
    for use in uses:
        assert (df_cond1[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond1[rf'BR_{use}_BH_MAX'] == 125).all()
        assert (df_cond2[rf'BR_{use}_HEIGHT'] == 195).all()
        
        
        
        

def test_BR_SP_SNX_M1_5_R10(df):

    #test if the BBL starts with any of the values in valores
    cond1_sb_t = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R10') & (df['MIH'] == True)& (df['SB'] == True)
    cond1_sb_f = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-5/R10') & (df['MIH'] == True)& (df['SB'] == False)
    
    df_cond1_sb_t = df[cond1_sb_t].copy() 
    df_cond1_sb_f = df[cond1_sb_f].copy()


    
    for col in columnas:
        df_cond1_sb_t[col] = pd.to_numeric(df_cond1_sb_t[col], errors='coerce')
        df_cond1_sb_f[col] = pd.to_numeric(df_cond1_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_cond1_sb_t['R_BH_MIN'] == 125).all() 
    assert (df_cond1_sb_t['BR_R_BH_MAX'] == 155).all()
    assert (df_cond1_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_cond1_sb_f['BR_R_HEIGHT'] == 275).all()  
    assert (df_cond1_sb_f['QAH_R_HEIGHT'] == 275).all()
    
    for use in uses:
        assert (df_cond1_sb_t[rf'{use}_BH_MIN'] == 125).all()
        assert (df_cond1_sb_t[rf'BR_{use}_BH_MAX'] == 155).all()
        assert (df_cond1_sb_f[rf'BR_{use}_HEIGHT'] == 275).all()
    
    
def test_BR_SP_SNX_M1_6_R10(df):

    #test if the BBL starts with any of the values in valores
    cond1_sb_t = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-6/R10') & (df['MIH'] == True)& (df['SB'] == True)
    cond1_sb_f = (df['SP'] == 'SNX') & (df['ZONEDIST']=='M1-6/R10') & (df['MIH'] == True)& (df['SB'] == False)
    
    df_cond1_sb_t = df[cond1_sb_t].copy() 
    df_cond1_sb_f = df[cond1_sb_f].copy()

    
    for col in columnas:
        df_cond1_sb_t[col] = pd.to_numeric(df_cond1_sb_t[col], errors='coerce')
        df_cond1_sb_f[col] = pd.to_numeric(df_cond1_sb_f[col], errors='coerce')

    assert (df_cond1_sb_t['R_BH_MIN'] == 125).all() 
    assert (df_cond1_sb_t['BR_R_BH_MAX'] == 155).all()
    assert (df_cond1_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_cond1_sb_f['BR_R_HEIGHT'] == 275).all()  
    assert (df_cond1_sb_f['QAH_R_HEIGHT'] == 275).all()
    
    for use in uses:
        assert (df_cond1_sb_t[rf'{use}_BH_MIN'] == 125).all()
        assert (df_cond1_sb_t[rf'BR_{use}_BH_MAX'] == 155).all()
        assert (df_cond1_sb_f[rf'BR_{use}_HEIGHT'] == 275).all()
    


def test_BR_SP_HSQ_no_SPSD_M1_6(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'HSQ')&(df['SPSD']=='empty') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'HSQ')&(df['SPSD']=='empty') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == True)& (df['SB'] == False)
    w100ws_f_sb_t = (df['SP'] == 'HSQ')&(df['SPSD']=='empty') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'HSQ')&(df['SPSD']=='empty') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == False)& (df['SB'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()

    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 125).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 155).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 290).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 290).all()

    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 125).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 185).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 235).all()
    
    for use in uses:
        assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 125).all()
        assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 155).all()
        assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 290).all()
        
        assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 125).all()
        assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 185).all()


def test_BR_SP_HSQ_SPSD_M1_6(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'HSQ')&(df['SPSD']=='A') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'HSQ')&(df['SPSD']=='A') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == True)& (df['SB'] == False)
    w100ws_f_sb_t = (df['SP'] == 'HSQ')&(df['SPSD']=='A') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'HSQ')&(df['SPSD']=='A') & (df['ZONEDIST']=='M1-6') & (df['W100WS'] == False)& (df['SB'] == False)
    

    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()

    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    # C6-4
    #SB True
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 125).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 155).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 430).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 430).all()
    
    
    
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 125).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 155).all()
    #SB False
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 185).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 235).all()
    
    
    for use in uses:
        assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 125).all()
        assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 155).all()
        assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 430).all()
        
        assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 125).all()
        assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 185).all()
        
    
def test_BR_SP_CL_SPSA_A_R8_no_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == True)&(df['NYCO']==False)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == False)&(df['NYCO']==False)  
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == True)&(df['NYCO']==False)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == False)&(df['NYCO']==False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 66).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 95).all()
    
    for use in uses:
        if use == 'CF':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 66).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        elif use == 'C':
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        
    
    
def test_BR_SP_CL_SPSA_A_R8_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == True)&(df['NYCO']==True)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == False)&(df['NYCO']==True)  
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == True)&(df['NYCO']==True)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == False)&(df['NYCO']==True)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 66).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 95).all()
    
    for use in uses:
        if use != 'M':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 66).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()


def test_BR_SP_CL_SPSA_A_C6_2(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['C6-2'])) & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['C6-2'])) & (df['W100WS'] == True)& (df['SB'] == False)    
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['C6-2'])) & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='A') & (df['ZONEDIST'].isin(['C6-2'])) & (df['W100WS'] == False)& (df['SB'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 66).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 95).all()
    
    for use in uses:
        if use != 'M':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 66).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        
def test_BR_SP_CL_SPSA_C2_R8_no_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == True)& (df['NYCO'] == False)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == False)& (df['NYCO'] == False) 
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == True)& (df['NYCO'] == False)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == False)& (df['NYCO'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 66).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 66).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 95).all()
        
    for use in uses:
        if use == 'CF':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 66).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        elif use == 'C':    
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        

def test_BR_SP_CL_SPSA_C2_R8_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == True)& (df['NYCO'] == True)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == True)& (df['SB'] == False)& (df['NYCO'] == True) 
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == True)& (df['NYCO'] == True)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R8'])) & (df['W100WS'] == False)& (df['SB'] == False)& (df['NYCO'] == True)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 66).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 66).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 95).all()
        
    for use in uses:
        if use != 'M':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 66).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        
        




def test_BR_SP_CL_SPSA_C2_R9_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == True)& (df['SB'] == True)& (df['NYCO'] == True)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == True)& (df['SB'] == False)&(df['NYCO'] == True)  
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == False)& (df['SB'] == True)&(df['NYCO'] == True)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == False)& (df['SB'] == False)&(df['NYCO'] == True)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 185).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 135).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 185).all()
    
    for use in uses:
        if use != 'M':
            
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 135).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
    




def test_BR_SP_CL_SPSA_C2_R9_no_OVERLAY(df):

    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == True)& (df['SB'] == True)& (df['NYCO'] == False)
    w100ws_t_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == True)& (df['SB'] == False)&(df['NYCO'] == False)  
    w100ws_f_sb_t = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == False)& (df['SB'] == True)&(df['NYCO'] == False)
    w100ws_f_sb_f = (df['SP'] == 'CL')&(df['SPSA']=='C2') & (df['ZONEDIST'].isin(['R9'])) & (df['W100WS'] == False)& (df['SB'] == False)&(df['NYCO'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 185).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 135).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 185).all()
    
    for use in uses:
        if use == 'CF':
            
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 135).all()
        elif use == 'C':
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
    


def test_BR_TMU_SPSA_A2_C6_3(df):
    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'TMU')&(df['SPSA']=='A2') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'TMU')&(df['SPSA']=='A2') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == True)& (df['SB'] == False)    
    w100ws_f_sb_t = (df['SP'] == 'TMU')&(df['SPSA']=='A2') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'TMU')&(df['SPSA']=='A2') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == False)& (df['SB'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 185).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 135).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 185).all()
    
    for use in uses:
        if use != 'M':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 135).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
        
        
def test_BR_TMU_SPSA_A4_C6_3A(df):
    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'TMU')&(df['SPSA']=='A4') & (df['ZONEDIST'].isin(['C6-3A'])) & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'TMU')&(df['SPSA']=='A4') & (df['ZONEDIST'].isin(['C6-3A'])) & (df['W100WS'] == True)& (df['SB'] == False)    
    w100ws_f_sb_t = (df['SP'] == 'TMU')&(df['SPSA']=='A4') & (df['ZONEDIST'].isin(['C6-3A'])) & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'TMU')&(df['SPSA']=='A4') & (df['ZONEDIST'].isin(['C6-3A'])) & (df['W100WS'] == False)& (df['SB'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 175).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 175).all()
    
    for use in uses:
        if use != 'M':
            
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()
    
    
    #########################################################
    #here#
    #########################################################
def test_BR_LI_SPSD_A_C6_2G_C6_2(df):
    #test if the BBL starts with any of the values in valores
    w100c_t_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='A') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2'])) & (df['W100C'] == True)& (df['SB'] == True)
    w100c_t_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='A') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2'])) & (df['W100C'] == True)& (df['SB'] == False)    
    w100c_f_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='A') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2'])) & (df['W100C'] == False)& (df['SB'] == True)
    w100c_f_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='A') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2'])) & (df['W100C'] == False)& (df['SB'] == False)
    
    df_w100c_t_sb_t = df[w100c_t_sb_t].copy() 
    df_w100c_t_sb_f = df[w100c_t_sb_f].copy()
    df_w100c_f_sb_t = df[w100c_f_sb_t].copy()
    df_w100c_f_sb_f = df[w100c_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100c_t_sb_t[col] = pd.to_numeric(df_w100c_t_sb_t[col], errors='coerce')
        df_w100c_t_sb_f[col] = pd.to_numeric(df_w100c_t_sb_f[col], errors='coerce')
        df_w100c_f_sb_t[col] = pd.to_numeric(df_w100c_f_sb_t[col], errors='coerce')
        df_w100c_f_sb_f[col] = pd.to_numeric(df_w100c_f_sb_f[col], errors='coerce')
        

    #R7A
    assert (df_w100c_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100c_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100c_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100c_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100c_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100c_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100c_f_sb_t['BR_R_BH_MAX'] == 65).all()
    assert (df_w100c_f_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100c_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100c_f_sb_f['QAH_R_HEIGHT'] == 95).all()
    
    for use in uses:
        if use != 'M':
            assert (df_w100c_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100c_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100c_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100c_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100c_f_sb_t[rf'BR_{use}_BH_MAX'] == 65).all()
            assert (df_w100c_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        else:   
            assert df_w100c_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100c_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100c_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100c_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100c_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100c_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100c_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100c_f_sb_f[rf'BR_{use}']==False).all()
    
    
    
    
def test_BR_LI_SPSD_A1_C6_2G_C6_2_C6_1(df):

    #test if the BBL starts with any of the values in valores
    w100c_t_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='A1') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2', 'C6-1'])) & (df['W100C'] == True)& (df['SB'] == True)
    w100c_t_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='A1') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2', 'C6-1'])) & (df['W100C'] == True)& (df['SB'] == False)    
    w100c_f_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='A1') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2', 'C6-1'])) & (df['W100C'] == False)& (df['SB'] == True)
    w100c_f_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='A1') & (df['ZONEDIST'].isin(['C6-2G', 'C6-2', 'C6-1'])) & (df['W100C'] == False)& (df['SB'] == False)
    
    df_w100c_t_sb_t = df[w100c_t_sb_t].copy() 
    df_w100c_t_sb_f = df[w100c_t_sb_f].copy()
    df_w100c_f_sb_t = df[w100c_f_sb_t].copy()
    df_w100c_f_sb_f = df[w100c_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100c_t_sb_t[col] = pd.to_numeric(df_w100c_t_sb_t[col], errors='coerce')
        df_w100c_t_sb_f[col] = pd.to_numeric(df_w100c_t_sb_f[col], errors='coerce')
        df_w100c_f_sb_t[col] = pd.to_numeric(df_w100c_f_sb_t[col], errors='coerce')
        df_w100c_f_sb_f[col] = pd.to_numeric(df_w100c_f_sb_f[col], errors='coerce')
    #R7A
    assert (df_w100c_t_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_w100c_t_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_w100c_t_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100c_t_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_w100c_t_sb_f['QAH_R_HEIGHT'] == 115).all()
    #R8B
    assert (df_w100c_f_sb_t['R_BH_MIN'] == 55).all() 
    assert (df_w100c_f_sb_t['BR_R_BH_MAX'] == 65).all()
    assert (df_w100c_f_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_w100c_f_sb_f['BR_R_HEIGHT'] == 75).all()  
    assert (df_w100c_f_sb_f['QAH_R_HEIGHT'] == 95).all()
    
    for use in uses:
        if use != 'M':
            
            assert (df_w100c_t_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_w100c_t_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_w100c_t_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
            
            assert (df_w100c_f_sb_t[rf'{use}_BH_MIN'] == 55).all()
            assert (df_w100c_f_sb_t[rf'BR_{use}_BH_MAX'] == 65).all()
            assert (df_w100c_f_sb_f[rf'BR_{use}_HEIGHT'] == 75).all()
        else:
            assert df_w100c_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100c_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100c_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100c_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100c_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100c_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100c_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100c_f_sb_f[rf'BR_{use}']==False).all()
        
        

def test_BR_LI_SPSD_B_C6_3(df):
    #test if the BBL starts with any of the values in valores
    w100ws_t_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='B') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == True)& (df['SB'] == True)
    w100ws_t_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='B') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == True)& (df['SB'] == False)    
    w100ws_f_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='B') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == False)& (df['SB'] == True)
    w100ws_f_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='B') & (df['ZONEDIST'].isin(['C6-3'])) & (df['W100WS'] == False)& (df['SB'] == False)
    
    df_w100ws_t_sb_t = df[w100ws_t_sb_t].copy() 
    df_w100ws_t_sb_f = df[w100ws_t_sb_f].copy()
    df_w100ws_f_sb_t = df[w100ws_f_sb_t].copy()
    df_w100ws_f_sb_f = df[w100ws_f_sb_f].copy()
    
    
    for col in columnas:
        df_w100ws_t_sb_t[col] = pd.to_numeric(df_w100ws_t_sb_t[col], errors='coerce')
        df_w100ws_t_sb_f[col] = pd.to_numeric(df_w100ws_t_sb_f[col], errors='coerce')
        df_w100ws_f_sb_t[col] = pd.to_numeric(df_w100ws_f_sb_t[col], errors='coerce')
        df_w100ws_f_sb_f[col] = pd.to_numeric(df_w100ws_f_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_w100ws_t_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_t_sb_t['BR_R_BH_MAX'] == 105).all()
    assert (df_w100ws_t_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_t_sb_f['BR_R_HEIGHT'] == 145).all()  
    assert (df_w100ws_t_sb_f['QAH_R_HEIGHT'] == 185).all()
    #R8B
    assert (df_w100ws_f_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_w100ws_f_sb_t['BR_R_BH_MAX'] == 95).all()
    assert (df_w100ws_f_sb_t['QAH_R_BH_MAX'] == 135).all()
    
    assert (df_w100ws_f_sb_f['BR_R_HEIGHT'] == 135).all()  
    assert (df_w100ws_f_sb_f['QAH_R_HEIGHT'] == 185).all()
    
    for use in uses:
        if use != 'M':
            assert (df_w100ws_t_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'] == 105).all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'] == 145).all()
            
            assert (df_w100ws_f_sb_t[rf'{use}_BH_MIN'] == 60).all()
            assert (df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'] == 95).all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'] == 135).all()
            
        else:
            assert df_w100ws_t_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_t_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_t_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_t_sb_f[rf'BR_{use}']==False).all()
            
            assert df_w100ws_f_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_w100ws_f_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_w100ws_f_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_w100ws_f_sb_f[rf'BR_{use}']==False).all()


def test_BR_LI_SPSD_C_C6_1G_C6_1(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LI')&(df['SPSD']=='C') & (df['ZONEDIST'].isin(['C6-1G', 'C6-1'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LI')&(df['SPSD']=='C') & (df['ZONEDIST'].isin(['C6-1G', 'C6-1'])) & (df['SB'] == False)    
    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()

    
    
    for col in columnas:
        df_cond_sb_t[col] = pd.to_numeric(df_cond_sb_t[col], errors='coerce')
        df_cond_sb_f[col] = pd.to_numeric(df_cond_sb_f[col], errors='coerce')
        
        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 40).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 75).all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 115).all()


    for use in uses:
        if use != 'M':
            assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 40).all()
            assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 75).all()
            assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
        else:
            assert df_cond_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_cond_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            assert (df_cond_sb_f[rf'BR_{use}']==False).all()


def test_BR_LIC_SPSD_CSS_SPSA_SHRS_C5_3(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LIC')&(df['SPSD']=='Court Square Subdistrict') & (df['SPSA']=='Special Height Regulations Section') & (df['ZONEDIST'].isin(['C5-3'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LIC')&(df['SPSD']=='Court Square Subdistrict') & (df['SPSA']=='Special Height Regulations Section') & (df['ZONEDIST'].isin(['C5-3'])) & (df['SB'] == False)    

    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()
    
    
    for col in columnas:
        df_cond_sb_t[col] = pd.to_numeric(df_cond_sb_t[col], errors='coerce')  
        df_cond_sb_f[col] = pd.to_numeric(df_cond_sb_f[col], errors='coerce')
        

        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 85).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 85).all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 85).all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 85).all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 85).all()
    
    for use in uses:
        if use != 'M':
            assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 85).all()
            assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 85).all()
            assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 85).all()
        else:
            assert df_cond_sb_t[rf'{use}_BH_MIN'].isna().all()
            assert df_cond_sb_t[rf'BR_{use}_BH_MAX'].isna().all()
            assert df_cond_sb_f[rf'BR_{use}_HEIGHT'].isna().all()
            

    


def test_BR_LIC_SPSD_QPS_SPSA_A1_M1_6_R10(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area A-1') & (df['ZONEDIST'].isin(['M1-6/R10'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area A-1') & (df['ZONEDIST'].isin(['M1-6/R10'])) & (df['SB'] == False)    

    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()
    
    
    for col in columnas:
        df_cond_sb_t[col] = df_cond_sb_t[col].apply(safe_convert)
        df_cond_sb_f[col] = df_cond_sb_f[col].apply(safe_convert)
        
        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 'No limit').all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 'No limit').all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 'No limit').all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 'No limit').all()
    
    for use in uses:
        assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 'No limit').all()
        assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 'No limit').all()
        
        
        


def test_BR_LIC_SPSD_QPS_SPSA_A2_M1_6_R10(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area A-2') & (df['ZONEDIST'].isin(['M1-6/R10'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area A-2') & (df['ZONEDIST'].isin(['M1-6/R10'])) & (df['SB'] == False)    

    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()
    
    
    for col in columnas:
        df_cond_sb_t[col] = df_cond_sb_t[col].apply(safe_convert)
        df_cond_sb_f[col] = df_cond_sb_f[col].apply(safe_convert)
        
        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 150).all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 150).all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 'No limit').all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 'No limit').all()
    
    for use in uses:
        assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 150).all()
        assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 'No limit').all()
        
        

def test_BR_LIC_SPSD_QPS_SPSA_B_M1_5_R9(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area B') & (df['ZONEDIST'].isin(['M1-5/R9'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area B') & (df['ZONEDIST'].isin(['M1-5/R9'])) & (df['SB'] == False)    

    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()
    
    
    for col in columnas:
        df_cond_sb_t[col] = df_cond_sb_t[col].apply(safe_convert)
        df_cond_sb_f[col] = df_cond_sb_f[col].apply(safe_convert)
        
        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 100).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 150).all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 150).all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 'No limit').all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 'No limit').all()
    for use in uses:
        assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 100).all()
        assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 150).all()
        assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 'No limit').all()
        
        
        
    
def test_BR_LIC_SPSD_QPS_SPSA_C_M1_5_R7_3(df):
    #test if the BBL starts with any of the values in valores
    cond_sb_t = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area C') & (df['ZONEDIST'].isin(['M1-5/R7-3'])) & (df['SB'] == True)
    cond_sb_f = (df['SP'] == 'LIC')&(df['SPSD']=='Queens Plaza Subdistrict') & (df['SPSA']=='Area C') & (df['ZONEDIST'].isin(['M1-5/R7-3'])) & (df['SB'] == False)    

    
    df_cond_sb_t = df[cond_sb_t].copy() 
    df_cond_sb_f = df[cond_sb_f].copy()
    
    
    for col in columnas:
        df_cond_sb_t[col] = df_cond_sb_t[col].apply(safe_convert)
        df_cond_sb_f[col] = df_cond_sb_f[col].apply(safe_convert)
        
        
    #R7A
    assert (df_cond_sb_t['R_BH_MIN'] == 60).all() 
    assert (df_cond_sb_t['BR_R_BH_MAX'] == 100).all()
    assert (df_cond_sb_t['QAH_R_BH_MAX'] == 100).all()
    
    assert (df_cond_sb_f['BR_R_HEIGHT'] == 'No limit').all()  
    assert (df_cond_sb_f['QAH_R_HEIGHT'] == 'No limit').all()
    
    for use in uses:
        assert (df_cond_sb_t[rf'{use}_BH_MIN'] == 60).all()
        assert (df_cond_sb_t[rf'BR_{use}_BH_MAX'] == 100).all()
        assert (df_cond_sb_f[rf'BR_{use}_HEIGHT'] == 'No limit').all()
        
        
        

