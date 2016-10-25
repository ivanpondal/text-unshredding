#! /usr/bin/env python

import math
import random
import sys

COLUMN_WIDTH = 80
PADDING_CHAR = '~'

def add_shuffled_column(original_text_matrix, shuffled_text_matrix, column, row_count):
    for i in range(row_count):
        shuffled_text_matrix[i] += original_text_matrix[i][column]

original_text = ""
for line in sys.stdin:
    original_text += line

original_text = original_text.replace('\n', ' ')

row_count = int(math.ceil(len(original_text) * 1.0 / COLUMN_WIDTH))

if len(original_text) % COLUMN_WIDTH != 0:
    original_text += PADDING_CHAR * (COLUMN_WIDTH - (len(original_text) % COLUMN_WIDTH))

original_text_matrix = [""] * row_count
for i in range(row_count):
    original_text_matrix[i] = original_text[i*COLUMN_WIDTH: i*COLUMN_WIDTH + COLUMN_WIDTH]

column_order = range(COLUMN_WIDTH)
random.shuffle(column_order)

shuffled_text_matrix = [""] * row_count
for i in range(COLUMN_WIDTH):
    add_shuffled_column(original_text_matrix, shuffled_text_matrix, column_order[i], row_count)

for line in shuffled_text_matrix:
    print line
