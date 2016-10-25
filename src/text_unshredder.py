#! /usr/bin/env python

import sys

def add_column(shredded_text_matrix, reconstructed_text_matrix, column, row_count):
    for i in range(row_count):
        reconstructed_text_matrix[i] += shredded_text_matrix[i][column]

tour_filename = sys.argv[1]

shredded_text_matrix = []
for line in sys.stdin:
    shredded_text_matrix.append(line.replace('\n', ''))

row_count = len(shredded_text_matrix)
column_count = len(shredded_text_matrix[0])

tour = []
with open(tour_filename, 'r') as f:
    in_tour_section = False
    for line in f:
        line = line.strip()
        if line == "TOUR_SECTION":
            in_tour_section = True
        elif in_tour_section:
            node = int(line)
            if node == -1:
                break
            tour.append(node - 2)

i = tour.index(-1)
tour = tour[i+1:] + tour[:i]

reconstructed_text_matrix = [""] * row_count
for i in range(column_count):
    add_column(shredded_text_matrix, reconstructed_text_matrix, tour[i], row_count)

for line in reconstructed_text_matrix:
    print line
