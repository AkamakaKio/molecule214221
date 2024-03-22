def combine_molecules(molecule1, molecule2):
    atoms1 = count_atoms(molecule1)
    atoms2 = count_atoms(molecule2)
    combined_atoms = {atom: atoms1.get(atom, 0) + atoms2.get(atom, 0) for atom in set(atoms1) | set(atoms2)}
    return combined_atoms

molecule1 = "H2O"
molecule2 = "CO2"
print("Molecule 1:", molecule1)
print("Molecule 2:", molecule2)
print("Combined molecules:", combine_molecules(molecule1, molecule2))
