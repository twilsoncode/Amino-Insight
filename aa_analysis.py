from Bio.SeqUtils.ProtParam import ProteinAnalysis

def aa_aromaticity(sequence):
    x = ProteinAnalysis(sequence)
    return x.aromaticity()

def aa_instability_index(sequence):
    x = ProteinAnalysis(sequence)
    return x.instability_index()

def aa_secondary_structure_fraction(sequence):
    x = ProteinAnalysis(sequence)
    return x.secondary_structure_fraction()

def aa_gravy(sequence):
    x = ProteinAnalysis(sequence)
    return x.gravy()

def aa_molar_extinction_coefficient(sequence):
    x = ProteinAnalysis(sequence)
    return x.molar_extinction_coefficient()

def aa_count_amino_acids(sequence):
    x = ProteinAnalysis(sequence)
    return x.count_amino_acids()