# Protein-Music-Generation
This script uniquely transforms protein sequences into melodies by assigning piano notes to amino acids based on the increasing order of their vibrational frequencies. Using secondary structure information (helix, sheet, coil) to influence note duration and dynamics, the script creates a melodic representation that reflects both the sequence and structural properties of proteins.
# Features
- Protein Data Retrieval: Downloads PDB files directly from the RCSB database.
- Sequence and Structure Analysis: Extracts amino acid sequences and secondary structure information using Biopython.
- Vibrational Frequency Mapping: Assigns piano notes to amino acids in ascending order of their vibrational frequencies, creating a unique auditory representation.
- Melody Generation: Produces MIDI files with dynamic musical interpretations of protein structures.
# Calculating vibrational frequency of amino acids
- Vibrational frequency can be calculated using DFT theorem using Gaussian software
