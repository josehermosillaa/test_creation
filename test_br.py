# HEIGHT/test_br.py
import os, sys

BASE_DIR = os.path.dirname(__file__)  # apunta a HEIGHT
sys.path.append(os.path.join(BASE_DIR, "01.BR", "00.geom_csv"))

# from BR_ZD import ZD_LIST
ZD_LIST = ['C4-11A', 'R10X', 'C4-12', 'R6-2', 'C5-4', 'C3A', 'M1-2/R5D', 'C6-2', 'M1-9A',
           'R4-1', 'M1-1A/R7-3', 'R5B', 'M1-6A', 'M1-7A',
           'C4-11', 'M1-1D', 'M1-4/R7D', 'R3-1', 'R7-1', 'C4-7A',
           'C4-6A', 'R2', 'C1-7A', 'C4-8', 'C6-9', 'C6-12', 'M1-2/R5B', 'M1-5/R9X',
           'C7-8', 'M1-2A/R6A', 'M3-1A', 'C4-5D', 'M1-5/R9-1', 'R9A', 'M1-3/R8', 'C3',
           'C4-2F', 'M1-4D', 'M1-2/R8', 'C2-7A', 'C5-2', 'C4-4L', 'M2-3A', 'C7-1', 'R6D',
           'R7-2', 'C1-8X', 'M2-1A', 'M1-5/R9A', 'C6-3', 'R1-2A', 'M1-5/R7X', 'M1-3D', 'C7-3', 'M1-3/R7D', 
           'R8B', 'R6A', 'R7B', 'C6-7.5', 'M1-1/R7D', 'C4-1', 'C2-8', 'C2-6A', 'M1-4/R7-3', 'M1-4/R9A',
           'C6-1G', 'M1-6/R10', 'R8X', 'R9-1', 'M1-2/R7-2', 'R10', 'R4', 'R7-3', 'R12', 'M1-8A', 'M1-2/R6A',
           'M1-6/R9', 'M1-4/R6A', 'R6-1', 'R8', 'C4-2', 'M1-8A/R11', 'C6-7', 'M1-5/R6A', 'M1-2D', 'M1-4/R8A', 
           'M1-5/R10', 'C6-2A', 'R5D', 'C5-3.5', 'C4-3', 'M1-1A', 'M1-2/R6B', 'M1-4/R7-2', 'R7A', 'C6-1', 'M1-9A/R12',
           'C7-7', 'R1-2', 'R6', 'R7X', 'M1-5/R7-2', 'C4-4', 'M1-4A', 'M1-2A', 'M1-2/R7A', 'C1-9A', 'C1-6A', 'M1-5D', 'M1-5/R8A', 
           'M1-1/R7-2', 'R11', 'M1-5/R7D', 'M1-6D', 'M1-3A', 'C5-3', 'C7-6', 'C4-5A', 'C5-1', 'C6-8', 'C5-1A', 
           'M1-2A/R7D', 'R10A', 'C1-7', 'C6-4.5', 'M1-8A/R12', 'M1-4A/R9A', 'C6-11', 'C7-9', 'C6-3A', 'C6-3D',
           'R4B', 'R7D', 'C1-9', 'C4-4D', 'R4A', 'C6-6', 'C6-5', 'M1-1/R5', 'C4-5', 'R2A', 'M1-2/R6', 
           'M1-5/R7-3', 'R1-1', 'R5', 'R3-2', 'R9D', 'R6B', 'C2-7X', 'M1-5A', 'C5-2A', 'M1-1/R6A', 
           'C1-6', 'C6-4A', 'M1-2/R8A', 'C2-8A', 'R9', 'C6-4M', 'M1-4/R9', 'M2-4A', 'M1-3/R7X', 
           'C6-3X', 'C4-5X', 'C2-6', 'C5-5', 'C7-5', 'C4-6', 'M1-4/R6', 'C1-8', 'C6-6.5', 
           'M1-2/R7-1', 'C7-4', 'R2X', 'C4-2A', 'M3-2A', 'M1-4/R6B', 'R3X', 'C6-2M', 'R8A', 'C4-4A',
           'C6-4', 'M1-4/R7X', 'C2-7', 'M1-1A/R6B', 'C6-1A', 'C6-2G', 'R10H', 'R11A', 'R3A',
           'C6-7T', 'C5-P', 'M2-2A', 'M1-4/R7A', 'C6-5.5', 'C7-2', 'C1-8A', 'C4-9', 'M1-3A/R7D', 
           'C4-3A', 'C5-2.5', 'R5A', 'C4-7', 'M1-6/R8X', 'M1-5/R9', 'R9X', 'C6-4X']


SP = ['M1-6', 'M2-4']

ZD_LIST = ZD_LIST + SP
"""preguntar si debo agregar los que podrian permitir br por ser special district"""

def is_br(row):
    # if row['ZONEDIST'] in ZD_LIST:
    if row in ZD_LIST: #para el test lo dejamos como variable simple y no fila del df
        return True
    return False