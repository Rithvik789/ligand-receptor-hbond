import os
from Bio.PDB import PDBParser, NeighborSearch

def calculate_interchain_hydrogen_bonds(pdb_file, receptor_chain="A", ligand_chains=("L", "H"), distance_cutoff=3.0):
   
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_file, pdb_file)

    receptor_atoms = [
        atom for chain in structure[0] if chain.id == receptor_chain for atom in chain.get_atoms()
    ]
 
    ligand_atoms = [
        atom for chain in structure[0] if chain.id in ligand_chains for atom in chain.get_atoms()
    ]
   

    print(f"Receptor atoms (Chain {receptor_chain}): {len(receptor_atoms)} atoms")
    print(f"Ligand atoms (Chains {ligand_chains}): {len(ligand_atoms)} atoms")
    
    hydrogen_bonds = []
    ns = NeighborSearch(receptor_atoms + ligand_atoms)


    for receptor_atom in receptor_atoms:
        if receptor_atom.element in ["N", "O"]:  # Donor atoms
            close_atoms = ns.search(receptor_atom.coord, distance_cutoff)
            for ligand_atom in close_atoms:
                if ligand_atom in ligand_atoms and ligand_atom.element in ["O", "N"] and ligand_atom != receptor_atom:
                    if receptor_atom.get_parent().id != ligand_atom.get_parent().id:  

                        print(f"Hydrogen bond found between:")
                        print(f"  Receptor atom: {receptor_atom.get_full_id()} ({receptor_atom.element})")
                        print(f"  Ligand atom: {ligand_atom.get_full_id()} ({ligand_atom.element})")
                        hydrogen_bonds.append((receptor_atom, ligand_atom))
    
    return hydrogen_bonds

directory = os.getcwd()

pdb_files = [f for f in os.listdir(directory) if f.endswith(".pdb")]


distance_cutoff = 3.7
receptor_chain = "A"
ligand_chains = ("L", "H")

output_file = "interchain_hydrogen_bonds.txt"
with open(output_file, "w") as f:
    for pdb_file in pdb_files:
        f.write(f"Analyzing file: {pdb_file}\n")
        print(f"Analyzing file: {pdb_file}")
        
        hydrogen_bonds = calculate_interchain_hydrogen_bonds(pdb_file, receptor_chain, ligand_chains, distance_cutoff)
        num_hbonds = len(hydrogen_bonds)
        
        f.write(f"Number of hydrogen bonds between {receptor_chain} and {ligand_chains} in {pdb_file}: {num_hbonds}\n")
        print(f"Number of hydrogen bonds between {receptor_chain} and {ligand_chains} in {pdb_file}: {num_hbonds}")
        
        for donor, acceptor in hydrogen_bonds:
            donor_info = f"Donor: {donor} ({donor.get_full_id()})"
            acceptor_info = f"Acceptor: {acceptor} ({acceptor.get_full_id()})"
            f.write(f"  {donor_info}, {acceptor_info}\n")
        
        f.write("\n")
        print()

print(f"Results saved to {output_file}")
