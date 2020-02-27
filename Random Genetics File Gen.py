# Generates random DNA data file
import random
dna_letter = ['A', 'C', 'T', 'G']
sequence = ""
seq_length = input("Length of Sequence (in multiples of 1000): ")
length = int(seq_length) * 100
file_name = input("File Name: ")
for x in range(length):
    sequence += random.choice(dna_letter)
print(sequence)
