import pytest
import pandas as pd
from zd_uses import permited_uses
from wf_groups import clasificar
from test_br import is_br
uses = ['R','CF', 'C','M']

columnas = ['R_BH_MIN', 'BR_R_BH_MAX', 'QAH_R_BH_MAX', 'BR_R_HEIGHT', 'QAH_R_HEIGHT']
for use in uses:
    columnas.append(rf'{use}_BH_MIN')
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
    
    # breakpoint()
    return df

def safe_convert(val):
    try:
        return pd.to_numeric(val)
    except Exception:
        return val
    
def test_ZD1_Height(df):
    df1 = df[df['ZD_WF'] == 'ZD1']
    breakpoint()