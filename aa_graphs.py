import pandas as pd
import numpy as np

def aa_graph_x(sequence):
    pos_array = np.arange(1, len(sequence) + 1)
    array = pos_array.tolist()
    return array


def aa_mw_graph_y(sequence):
    array_mw = []
    data = pd.read_csv("amino acids6.csv")
    for b in range(0, len(sequence)): 
        for a in range(0, len(data)):           
            if data.loc[a, "Single Letter Code"] == sequence[b]:
                array_mw.append(data.loc[a, "Molecular Weight"])
    return array_mw

def aa_pI_graph_y(sequence):
    array_pI = []
    data = pd.read_csv("amino acids6.csv")
    for b in range(0, len(sequence)): 
        for a in range(0, len(data)):           
            if data.loc[a, "Single Letter Code"] == sequence[b]:
                array_pI.append(data.loc[a, "Isoelectric point (Zimmerman et al., 1968)"])
    return array_pI

