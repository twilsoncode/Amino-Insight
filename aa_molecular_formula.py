import pandas as pd

def aa_mf_one_sequence(sequence):
    df_aa6 = pd.read_csv("amino acids6.csv")
    noC = 0
    noH = 0
    noO = 0
    noN = 0
    noS = 0    
    for a in range(0, len(df_aa6)):
        for b in range(0, len(sequence)): #starting the loop at 1 to skip methionine inclusion            
            mf = ""
            if sequence[b] == "X":
                mf = "Unknown"
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
                    except IndexError:
                        pass
            molecule_noC = noC
            molecule_noH = noH - (2 * ((len(sequence))-1))
            molecule_noO = noO - ((len(sequence))-1)
            molecule_noN = noN
            molecule_noS = noS

            if molecule_noC > 1:
                mf = mf + "C" + str(molecule_noC)
            if molecule_noC == 1:
                mf = mf + "C"
            if molecule_noH > 1:
                mf = mf + "H" + str(molecule_noH)
            if molecule_noH == 1:
                mf = mf + "H"
            if molecule_noN > 1:
                mf = mf + "N" + str(molecule_noN)
            if molecule_noN == 1:
                mf = mf + "N"
            if molecule_noO > 1:
                mf = mf + "O" + str(molecule_noO)
            if molecule_noO == 1:
                mf = mf + "O"
            if molecule_noS > 1:
                mf = mf + "S" + str(molecule_noS)
            if molecule_noS == 1:
                mf = mf + "S"

    mf_sub = ""
    for x in range(0,len(mf)):
        if mf == "Unknown":
            mf_sub = "Unknown"
            break
        if mf[x] == "0":
            mf_sub += "₀"
        if mf[x] == "1":
            mf_sub += "₁"
        if mf[x] == "2":
            mf_sub += "₂"
        if mf[x] == "3":
            mf_sub += "₃"
        if mf[x] == "4":
            mf_sub += "₄"
        if mf[x] == "5":
            mf_sub += "₅"
        if mf[x] == "6":
            mf_sub += "₆"
        if mf[x] == "7":
            mf_sub += "₇"
        if mf[x] == "8":
            mf_sub += "₈"
        if mf[x] == "9":
            mf_sub += "₉"
        if mf[x] == "C":
            mf_sub += "C"
        if mf[x] == "H":
            mf_sub += "H"
        if mf[x] == "O":
            mf_sub += "O"
        if mf[x] == "N":
            mf_sub += "N"
        if mf[x] == "S":
            mf_sub += "S"     
    return mf_sub