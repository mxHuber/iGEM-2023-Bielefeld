import os
import sys
import time

# Author: Maximilian Leo Huber 05.06.2023
# Example: python TripletFinder.py [FILE] 

# get starting time of program
program_start_time = time.time()

# check for correct number of arguments
if not len(sys.argv) == 2:
	print("Bad Inputs. Command is: python TripletFinder.py [FILE]")
	exit()

data_file = open(sys.argv[1])
lines = data_file.readlines()
data_file.close()

# TODO: go over all triplets and blast the area of ~100bp around it

program_end_time = time.time()
final_time = program_end_time - program_start_time

print("Program finished! It took " + str(final_time) + " to finish")

# TODO: print out statistics, like the scores of the 5 best triplet areas
