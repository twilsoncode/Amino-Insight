from Bio.SeqUtils.IsoelectricPoint import IsoelectricPoint as pI
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import tkinter as tk
from matplotlib.figure import Figure

def aa_plot(sequence):
    #sequence = "K"
    protein = pI(sequence)

    array_pH = []
    array_charge = []

    for x in np.arange(0,14.01,0.01):
        #print(x)
        array_pH.append(x)

    #print(array_pH)
    #print(len(array_pH))

    #charge = protein.charge_at_pH(array_pH[1])
    #print(charge)

    for y in range(0, len(array_pH)):
        array_charge.append(protein.charge_at_pH(array_pH[y]))

    #print(array_charge)
    #isoelectric_point = protein.pi()
    #print(isoelectric_point)

    plt.plot(array_pH, array_charge)
    plt.title("A Graph To Show How The pH Affects Charge of the Sequence Protein")
    plt.xlabel("pH")
    plt.ylabel("Charge")
    plt.show()

def aa_pI_matrix(sequence):
    try:
        protein = pI(sequence)
    except IndexError:
        protein = pI("A")

    array_pH = []
    array_charge = []

    for x in np.arange(0,14.01,0.01):
        #print(x)
        array_pH.append(x)

    #print(array_pH)
    #print(len(array_pH))

    #charge = protein.charge_at_pH(array_pH[1])
    #print(charge)

    for y in range(0, len(array_pH)):
        array_charge.append(protein.charge_at_pH(array_pH[y]))

    return array_charge

def aa_pH_array():
    array_pH = []
    for x in np.arange(0,14.01,0.01):
        #print(x)
        array_pH.append(x)
    
    return array_pH

def aa_xy(sequence):
    protein = pI(sequence)

    array_pH = []
    array_charge = []

    for x in np.arange(0,14.01,0.01):
        #print(x)
        array_pH.append(x)

    #print(array_pH)
    #print(len(array_pH))

    #charge = protein.charge_at_pH(array_pH[1])
    #print(charge)

    for y in range(0, len(array_pH)):
        array_charge.append(protein.charge_at_pH(array_pH[y]))

    

    return array_charge

def aa_pI_value(sequence):
    protein = pI(sequence)
    isoelectric_point = protein.pi()
    print(isoelectric_point)
    for x in range(0, len(sequence)):
        if sequence[x] == "X":
            isoelectric_point = "Unknown"
    return(isoelectric_point)

def aa_blank_plot(root):
    fig = Figure(figsize = (6,8), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot()
    plot1.set_title("A Graph To Show How The pH Affects \n Charge of the Sequence Protein")
    plot1.set_xlabel("pH")
    plot1.set_ylabel("Charge")
    plot1.set_xbound(0,14)
    plot1.set_ybound(-1,1)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    #canvas.get_tk_widget().pack()
    
    canvas.get_tk_widget().grid(row=3, column=6, padx=20, pady=(20, 10), rowspan=6, columnspan=8, sticky="nsew")
    

    #label.grid(row=3, column=6, padx=20, pady=(20, 10), columnspan=6)

    #toolbar = tk.Frame(master=root)
    #toolbar.grid(row=5, column=1, padx=20, pady=(20, 10), rowspan=5, sticky="nsew")
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar = False)
    toolbar.grid(row=9, column=6, padx=20, pady=(20, 10), rowspan=1, columnspan=8, sticky="nsew")
    #toolbar = NavigationToolbar2Tk()
    toolbar.update()

def aa_plot_tk(sequence,root):
    fig = Figure(figsize = (6,8), dpi = 100)
    canvas = FigureCanvasTkAgg(fig, master=root)
    protein = pI(sequence)

    array_pH = []
    array_charge = []

    for x in np.arange(0,14.01,0.01):
        #print(x)
        array_pH.append(x)

    #print(array_pH)
    #print(len(array_pH))

    #charge = protein.charge_at_pH(array_pH[1])
    #print(charge)

    for y in range(0, len(array_pH)):
        array_charge.append(protein.charge_at_pH(array_pH[y]))

    #print(array_charge)
    #isoelectric_point = protein.pi()
    #print(isoelectric_point)

    
    #plt.plot(array_pH, array_charge)
    #plt.title("A Graph To Show How The pH Affects Charge of the Sequnce Protein")
    #plt.xlabel("pH")
    #plt.ylabel("Charge")
    
    plot1 = fig.add_subplot(111)
    plot1.plot(array_pH, array_charge)
    plot1.set_title("A Graph To Show How The pH Affects \n Charge of the Sequence Protein")
    plot1.set_xlabel("pH")
    plot1.set_ylabel("Charge")
    
    canvas.draw()
    #canvas.get_tk_widget().pack()
    canvas.get_tk_widget().grid(row=3, column=6, padx=20, pady=(20, 10), rowspan=6, columnspan=8, sticky="nsew")

    #label.grid(row=3, column=6, padx=20, pady=(20, 10), columnspan=6)

    #toolbar = tk.Frame(master=root)
    #toolbar.grid(row=5, column=1, padx=20, pady=(20, 10), rowspan=5, sticky="nsew")
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar = False)
    toolbar.grid(row=9, column=6, padx=20, pady=(20, 10), rowspan=1, columnspan=8, sticky="nsew")
    #toolbar = NavigationToolbar2Tk()
    toolbar.update()



    