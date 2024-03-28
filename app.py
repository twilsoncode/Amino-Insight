from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import aa_molecular_formula
import aa_pI
import aa_molecular_weight
import aa_analysis
import aa_graphs

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route('/')
def run_index():
    return render_template("index.html")

@app.route('/aromaticity')
def run_aromaticity():
    return render_template("aromaticity.html")

@app.route('/tutorial')
def run_tutorial():
    return render_template("tutorial.html")

@app.route('/secondary_structure_fraction')
def run_secondary_structure_fraction():
    return render_template("secondary_structure_fraction.html")

@app.route('/instability_index')
def run_instability_index():
    return render_template("instability_index.html")

@app.route('/gravy')
def run_gravy():
    return render_template("gravy.html")

@app.route('/molar_extinction_coefficient')
def run_molar_extinction_coefficient():
    return render_template("molar_extinction_coefficient.html")

@app.route('/count_amino_acids')
def run_count_amino_acids():
    return render_template("count_amino_acids.html")

@app.route('/table')
def run_table():
    return render_template("table.html")

@app.route('/nglviewer')
def run_nglviewer():
    return render_template("nglviewer.html")

@app.route('/aa_viewer_test')
def run_aa_viewer_test():
    return render_template("aa_viewer_test.html")

@app.route('/privacy_policy')
def run_privacy_policy():
    return render_template("privacy_policy.html")

@app.route('/graph')
def run_graph():
    return render_template("graph.html")

@app.route('/molecular_formula')
def run_molecular_formula():
    return render_template("molecular_formula.html")

@app.route('/molecular_weight')
def run_molecular_weight():
    return render_template("molecular_weight.html")

@app.route('/isoelectric_point')
def run_isoelectric_point():
    return render_template("isoelectric_point.html")

@app.route('/aa_viewer')
def run_aa_viewer():
    return render_template("aa_viewer.html")

@app.route('/aa_cf', methods=['POST'])
def run_aa_cf():
    data = request.form.get('data').upper()
    if data == "":
        result = ""
    else:
        result = str(aa_molecular_formula.aa_mf_one_sequence(data))
    return result

@app.route('/aa_pI_array_y', methods=['POST'])
def run_aa_pI_array_y():
    pI_data = request.form.get('pI_data').upper()
    result = aa_pI.aa_pI_matrix(pI_data)
    return jsonify(result)

@app.route('/aa_pI_array_x', methods=['POST'])
def run_aa_pI_array_x():
    result = aa_pI.aa_pH_array()
    return jsonify(result)

@app.route('/aa_pI_value', methods=['POST'])
def run_aa_pI_value():
    value = request.form.get('aa_pI_data').upper()
    if value == "":
        result = ""
    else:
        result = str(aa_pI.aa_pI_value(value))
    return result


@app.route('/aa_mw_array_y', methods=['POST'])
def run_aa_mw_array_y():
    mw_data = request.form.get('mw_data').upper()
    result = aa_graphs.aa_mw_graph_y(mw_data)
    return jsonify(result)

@app.route('/aa_graph_array_x', methods=['POST'])
def run_aa_graph_array_x():
    mw_data = request.form.get('mw_data').upper()
    result = aa_graphs.aa_graph_x(mw_data)
    return jsonify(result)

@app.route('/aa_pI_graph_array_y', methods=['POST'])
def run_aa_pI_graph_array_y():
    pI_data = request.form.get('pI_data').upper()
    result = aa_graphs.aa_pI_graph_y(pI_data)
    return jsonify(result)


@app.route('/aa_mw_value', methods=['POST'])
def run_aa_mw_value():
    mw_data = request.form.get('aa_mw_data').upper()
    if mw_data == "":
        result = ""
    else:
        result = str(aa_molecular_weight.aa_mw(mw_data))
    return result

@app.route('/aa_aromaticity_value', methods=['POST'])
def run_aa_aromaticity_value():
    aromaticity_data = request.form.get('aa_aromaticity_data').upper()
    if aromaticity_data == "":
        result = ""
    else:
        result = str(aa_analysis.aa_aromaticity(aromaticity_data))
    return result

@app.route('/aa_instability_index_value', methods=['POST'])
def run_aa_instability_index_value():
    instability_index_data = request.form.get('aa_instability_index_data').upper()
    if instability_index_data == "":
        result = ""
    else:
        result = str(aa_analysis.aa_instability_index(instability_index_data))
    return result

@app.route('/aa_secondary_structure_fraction_value', methods=['POST'])
def run_aa_secondary_structure_fraction_value():
    secondary_structure_fraction_data = request.form.get('aa_secondary_structure_fraction_data').upper()
    if secondary_structure_fraction_data == "":
        result = ""
    else:
        result = str(aa_analysis.aa_secondary_structure_fraction(secondary_structure_fraction_data))
    return result

@app.route('/aa_gravy_value', methods=['POST'])
def run_aa_gravy_value():
    gravy_data = request.form.get('aa_gravy_data').upper()
    if gravy_data == "":
        result = ""
    else:
        result = str(aa_analysis.aa_gravy(gravy_data))
    return result

@app.route('/aa_molar_extinction_coefficient_value', methods=['POST'])
def run_aa_molar_extinction_coefficient_value():
    molar_extinction_coefficient_data = request.form.get('aa_molar_extinction_coefficient_data').upper()
    if molar_extinction_coefficient_data == "":
        result = ""
    else:
        result = str(aa_analysis.aa_molar_extinction_coefficient(molar_extinction_coefficient_data))
    return result

@app.route('/aa_count_amino_acids_value', methods=['POST'])
def run_aa_count_amino_acids_value():
    count_amino_acids_data = request.form.get('aa_count_amino_acids_data').upper()
    if count_amino_acids_data == "":
        result = ""
    else:
        result = jsonify(aa_analysis.aa_count_amino_acids(count_amino_acids_data))
    return result

if __name__ == '__main__':
    app.run(debug=True)