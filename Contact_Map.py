import Bio.PDB
import numpy
from Bio.PDB import Selection
import matplotlib.pyplot as plt


def main():
    pdb_file = "2hhb"
    pdb_filename = pdb_file+".pdb"
    structure = Bio.PDB.PDBParser().get_structure(pdb_file, pdb_filename)           #wczytanie struktury
    model = structure[0]
    residues = structure.get_residues()
    residues = Selection.unfold_entities(model, 'R')
    counter=0
    for r in residues:
        counter=counter+1
    contact_matrix = numpy.zeros((counter, counter), dtype = int)         #stworzenie macierzy z samymi zerami


    for row, residue_one in enumerate(residues):                #row to index, a residue_one nazwa residuum
        for col, residue_two in enumerate(residues):
            #print(col, row)
            if col == row or residue_one.id[0].isspace()!=1 or residue_two.id[0].isspace()!=1:
                continue
            diff_vector = residue_one["CA"].coord - residue_two["CA"].coord
            diff_vector = numpy.sqrt(numpy.sum(diff_vector * diff_vector))
            print (diff_vector, end="")
            if diff_vector < 8.0:
                contact_matrix[row][col] = 1


    # wykres
    plt.imshow(contact_matrix, cmap='viridis', interpolation='nearest')
    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
