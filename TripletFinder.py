import os
import sys
import time
from Bio.Blast import NCBIWWW

# Author: Maximilian Leo Huber 05.06.2023
# Example: python TripletFinder.py [FILE 1] [FILE 2]

# get starting time of program
program_start_time = time.time()

# check for correct number of arguments
if not len(sys.argv) == 3:
	print("Bad Inputs. Command is: python TripletFinder.py [FILE]")
	exit()

data_file = open(sys.argv[1])
fasta_string_1 = data_file.read()
data_file.close()

data_file = open(sys.argv[2])
fasta_string_2 = data_file.read()
data_file.close()

# TODO (max): manually add triplets maybe?
triplets_of_interest = []
triplet_indices = []

for i in range(len(fasta_string_1) - 2):
        current_triplet = fasta_string_1[i] + fasta_string_1[i + 1] + fasta_string_1[i + 2]
        for n in range(len(triplet_indices)):
                if (current_triplet == triplets_of_interest[n]):
                        triplet_indices.append(i)
                        continue
# in case we use smith waterman
gap_open_penalty = 1
gap_extend_penalty = 2

# map triplet indices to scores

# TODO (max): go over all triplets and blast the area of ~100bp around it
# Also, what do we do when the triplet is at the start or in less than a 50bp range of the start?

for i in range(len(triplet_indices)):
        # Also, what do we do when the triplet is at the start or in less than a 50bp range of the start?
        substring_start = triplet_indices[i] - 50
        substring_end = triplet_indices[i] + 50
        current_area = fasta_string_1[substring_start:substring_end]
        # TODO (max): compare. I'm not sure how to do that currently though, maybe use smith waterman? Blast seems suboptimal

program_end_time = time.time()
final_time = program_end_time - program_start_time

print("Finished! It took " + str((final_time) / 60) + " minutes to run.")

# TODO (max): print out statistics, like the scores of the 5 best triplet areas
