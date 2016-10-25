#! /usr/bin/env python

import sys
import csv

CHARACTERS = "abcdefghijklmnopqrstuvwxyz_~"
BIG_INTEGER = 100

def column_score(shredded_text, letter_proximity_matrix, column_i, column_j, row_count):
    score = 0.0
    if column_i != column_j:
        for r in range(row_count):
            letter_i = shredded_text[r][column_i].lower()
            letter_j = shredded_text[r][column_j].lower()
            letter_i = letter_i if (letter_i.isalpha()) else '_'
            letter_j = letter_j if (letter_j.isalpha()) else '_'
            score += letter_proximity_matrix[letter_i][letter_j] / row_count
        score = 100 - score

    return int(score)

letter_proximity_csv = sys.argv[1]

letter_proximity_matrix = {x: {y:0.0 for y in CHARACTERS} for x in CHARACTERS}

with open(letter_proximity_csv) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        letter_proximity_matrix[row['first_letter']][row['second_letter']] = float(row['cond_prob'])
    letter_proximity_matrix['~']['~'] = 100.0

shredded_text = []
for line in sys.stdin:
    shredded_text.append(line.replace('\n', ''))

row_count = len(shredded_text)
column_count = len(shredded_text[0])
dimension = column_count + 1

print "NAME : column similarity";
print "TYPE : ATSP"
print "DIMENSION : " + str(dimension)
print "EDGE_WEIGHT_TYPE : EXPLICIT"
print "EDGE_WEIGHT_FORMAT : FULL_MATRIX"
print "NODE_COORD_TYPE : NO_COORDS"
print "DISPLAY_DATA_TYPE : NO_DISPLAY\n"
print "EDGE_WEIGHT_SECTION :"

print "0 " * dimension

for i in range(column_count):
    row = "0 "
    for j in range(column_count):
        row += str(column_score(shredded_text, letter_proximity_matrix, i, j, row_count)) + " "
    print row
