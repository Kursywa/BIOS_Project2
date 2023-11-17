import sys
import Bio.PDB
import numpy
from Bio.PDB import MMCIFParser
from Bio.PDB import PDBList
from Bio import PDB


def main():
    protein = "2HHB"
    pdbl = PDBList()  # create pdb list
    native_pdb = pdbl.retrieve_pdb_file(protein, file_format="pdb")  # download protein from PDB and save it to native_pdb
    parser = PDB.PDBParser(QUIET=True)  # creating parser
    structure = parser.get_structure("hemoglobin", native_pdb)  #parsing the protein and saving it to structure variable
    ca_atoms = []  # initializing array holding all CA atoms
    # accessing the
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    if 'CA' in atom:
                        ca_atoms.append(atom['CA'])  # might not remember coordinates, probably better to use dictionary?
    print(ca_atoms)


if __name__ == "__main__":
    main()
