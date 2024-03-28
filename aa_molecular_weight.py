import pandas as pd

def aa_mw(sequence):
    C_mw = 12.011
    H_mw = 1.00784
    O_mw = 15.999
    S_mw = 32.065
    N_mw = 14.0067
    df_aa6 = pd.read_csv("amino acids6.csv")
    noC = 0
    noH = 0
    noO = 0
    noN = 0
    noS = 0
    
    for a in range(0, len(df_aa6)):
        for b in range(0, len(sequence)): #starting the loop at 1 to skip methionine inclusion            
            mw = ""
            if sequence[b] == "X":
                mw = "Unknown"
                pass          
            if df_aa6.loc[a, "Single Letter Code"] == sequence[b]:                
                aa_pos = a
                aa_mf = df_aa6.loc[aa_pos, "Molecular Formula"]
                for c in range(0,12):
                    try:
                        try:
                            if aa_mf[c] == "C":
                                noC = noC + int(aa_mf[c + 1])
                        except ValueError:
                            noC = noC + 1
                        try:
                            if aa_mf[c] == "H":
                                try:
                                    if aa_mf[c + 3] == "N":
                                        temp = ""
                                        temp += str(aa_mf[c + 1])
                                        temp += str(aa_mf[c + 2])
                                        noH = noH + int(temp)
                                    else:
                                        noH = noH + int(aa_mf[c + 1])
                                except IndexError:
                                    pass    
                        except ValueError:
                            noH = noH + 1
                        try:
                            if aa_mf[c] == "O":
                                noO = noO + int(aa_mf[c + 1])            
                        except IndexError:
                            noO = noO + 1
                            #print("test")
                        try:
                            if aa_mf[c] == "N":
                                noN = noN + int(aa_mf[c + 1])
                        except ValueError:
                            noN = noN + 1 
                        try:
                            if aa_mf[c] == "S":
                                noS = noS + int(aa_mf[c + 1])            
                        except IndexError:
                            noS = noS + 1
                            #print("test")  
                    except IndexError:
                        pass
    molecule_noC = noC
    molecule_noH = noH - (2 * ((len(sequence))-1))
    molecule_noO = noO - ((len(sequence))-1)
    molecule_noN = noN
    molecule_noS = noS

    total_Cw = C_mw * molecule_noC
    total_Hw = H_mw * molecule_noH
    total_Ow = O_mw * molecule_noO
    total_Nw = N_mw * molecule_noN
    total_Sw = S_mw * molecule_noS

    if mw != "Unknown":
        mw = str(total_Cw + total_Hw + total_Ow + total_Nw + total_Sw)
    return mw
