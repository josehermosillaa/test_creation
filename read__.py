import pandas as pd

SG = pd.read_csv("/home/josehermosilla/Escritorio/diferencias/BR_REGULATION_SP_250820_2029/BR_REGULATION_SP_250820_2029.csv", sep=';', low_memory=False)
# SG = SG[SG['BBL'].isin([3048420006,3048420039])]
# zd_list = [
# 'M1-1A/R6B',
# 'M1-2A/R6A',
# 'M1-2A/R7D',
# 'M1-3A/R7D',
# 'M1-4A/R9A',
# 'M1-3/R7D',
# ]
# SG = SG[SG['ZONEDIST'].isin(zd_list)]
# SG.to_csv('zd_usebulk_test.csv',sep=';')
breakpoint()
select_columns =[
'INDEX',
'BBL',
'A_TOTAL',
'ZONEDIST',
'OVERLAY',
'ADJ',
'SP',
'SPSD',
'SPSA',
'SB',
'PP',
'W100WS',
'R_BH_MIN',
'BR_R_BH_MAX',
'QAH_R_BH_MAX',
'BR_R_HEIGHT',
'QAH_R_HEIGHT',
'SZ_REG',
'GEOMETRY',
'ADJ_R_REGULATION',
'PP_REGULATION',
'SPLT_REGULATION',
'BH_REGULATION',
'HT_REGULATION',
'R_SWL_REGULATION',
'C_SWL_REGULATION',
'SETBACK_REGULATION',
'BRTB_LCMAX_REGULATION',
'BRTB_LCMIN_REGULATION',
'TB_ZFA_REGULATION',
'SP_REGULATION',
]
SG[['SP', 'SPSD', 'SPSA']] = SG[['SP', 'SPSD', 'SPSA']].replace('empty', '')

SG = SG.replace({True: 'true', False: 'false'})


SG = SG[select_columns]
SG.to_csv("TB_REGULATION_SP_250722_1756_new_processed.csv",sep=';', index=False)
# SG = SG.columns.tolist()
# breakpoint()
# SG_columns = pd.DataFrame(SG.columns, columns=['Column Names'])
# SG_columns.to_excel("USE_BULKS_YARD_columns.xlsx", index=False)