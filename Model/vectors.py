import sys
import pandas as pd
import numpy as np

MAX_SIZE = 600                                                                          # the rows length
sample_vectors = set()                                                                  # the resultant sample vectors

# returns a pandas dataframe
def read_from_file():
    matrix = list()
    with open("/Users/szameltamas/Desktop/KESZ_projekt/Others/elements2.txt", 'r') as file:
        content = file.readlines()
        content = [row.strip('\n') for row in content]
        for row in content:
            separated = row.split(';')
            temp = [int(i) for i in separated]
            matrix.append(temp)
    df = pd.DataFrame(matrix, columns=["lenght", "width", "quantity"])
    return df

def find_cohesive_items(df):                                                              # finds the items that can be put in the same row (with rotations)
    cohesive_params = dict()

    length_list = df["lenght"].tolist()
    width_list = df["width"].tolist()

    for i in range(len(length_list)):
        vector = length_list[i]
        vector_rev = width_list[i]

        if vector not in cohesive_params:
            cohesive_params[vector] = [-1 for k in range(len(length_list))]

        if vector_rev not in cohesive_params:
            cohesive_params[vector_rev] = [-1 for k in range(len(length_list))]

        for j in range(len(width_list)):
            if length_list[j] == vector:
                cohesive_params[vector][j] = width_list[j]
            if width_list[j] == vector_rev:
                cohesive_params[vector_rev][j] = length_list[j]
    return cohesive_params


def get_starting_index(quantity):
    for i in range(len(quantity)):
        if quantity[i] > 0:
            return i
def calculate_sample_length(vector, lengths):
    _sum = 0
    for i in range(len(vector)):
        if i == -1: continue
        _sum += (vector[i] * lengths[i])
    return _sum
def get_minimal_element(lengths):
    _min = sys.maxsize
    for i in lengths:
        if i == -1: continue
        if i < _min: _min = i
    return _min
def remove_duplicates(lst):
    res = list()
    for i in lst:
        if i not in res:
            res.append(i)
    return res

# to generate the sample vectors from all starting points, only 1 length is valid
def separate(vector):
    separated = list()

    for index in range(len(vector)):
        if vector[index] == -1: continue

        copy = vector.copy()
        for i in range(len(copy)):
            if i == index or copy[i] == -1: continue
            else: copy[i] = 0

        if copy not in separated:
            separated.append(copy) 

    return separated

# lengths to quantities, the maximum amount that can fit in the row (-1 if a sample cannot be matched with a different one)
def make_quantity_list(element):
    quantity = list()
    for i in range(len(element)):
        if element[i] > 0:
            quantity.append(MAX_SIZE // element[i])

        else:
            if element[i] == 0: quantity.append(0)
            else: quantity.append(-1)

    return quantity

# decrease quantity by one, check if we can fit another length in the row
def get_all_combinations(lengths, quantities):
    sample_vectors.add(tuple(quantities))

    pos = get_starting_index(quantities)
    while quantities[pos] > 0:
        quantities[pos] -= 1
        get_fit(quantities.copy(), pos, lengths)


def get_fit(vector, position, lengths):
    for index in range(len(vector)):
        if index == position or vector[index] == -1: continue                           # skip the current index (bc. infinite recursion) and (-1) values

        length = calculate_sample_length(vector, lengths)
        if length + lengths[index] <= MAX_SIZE:                                         # sample length with decreased quantity, see if other fits on the row
            new_vector = vector.copy()
            new_vector[index] += 1                                                      # if so, increase that by 1, calculate length again

            min_size = MAX_SIZE - get_minimal_element(lengths)
            if min_size <= calculate_sample_length(new_vector, lengths) <= MAX_SIZE:    # see if it doesnt leave any space behind
                sample_vectors.add(tuple(new_vector))
            get_fit(new_vector, index, lengths)                                         # recursive call, to get all possible combinations
            

def generate(lengths):
    separated_vectors = separate(lengths)                                               # check all samples from different starting values
    for vector in separated_vectors:
        get_all_combinations(lengths, make_quantity_list(vector))                       # from values to quantities

# returns a list of tuples, the sample vectors
def generate_sample_vectors(param):
    for value in param.values():
        generate(value)

    df = pd.DataFrame(list(sample_vectors))
    df = np.where(df[:] == -1, 0, df)
    filtered = pd.DataFrame(df)

    result = list((filtered.to_records(index=False)))                                   # apparently, removing the (-1)-s may make duplicated samples
    return remove_duplicates(result)