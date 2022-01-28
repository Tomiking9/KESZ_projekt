import copy
from turtle import st
from xml import dom
import numpy as np, pandas as pd

class Matrix:
    def __init__(self, vector=list(), quantity=list()):
        self.vector = vector
        self.quantity = quantity
    
    @property
    def vector(self):
        return self._vector
    @vector.setter
    def vector(self, value):
        self._vector = value

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def __str__(self):
        headers = [str(i) for i in self.vector]
        data = [[self.quantity[i-1][j-1] for i in range(len(headers)+1)] for j in range(len(headers)+1)]            
        data = np.array(data)

        data = pd.DataFrame(data[1:,1:], columns=headers, index=headers)
        data.columns.name = "Length"
        return str(data)
        
class Hasse:
    def __init__(self, vector, max_size):
        self.vector = vector
        self.max_size = max_size

    @property
    def vector(self):
        return self._vector
    @vector.setter
    def vector(self, value):
        self._vector = value

    def make_default_vectors(self, pos):
        empty = dict()
        for i in self.vector:
            empty[i] = 0
        empty[pos] = 1
        return empty

    def compare_values(self, original_vect, new_vect):
        original_vect_components = list(original_vect.values())
        new_vect_components = list(new_vect.values())

        return new_vect_components > original_vect_components # TODO: not gud, make it gud / maybe gud??

    def increase_component(self, vector, pos):
        copy_vect = copy.copy(vector)
        copy_vect[pos] += 1
        return copy_vect

    def end_of_batch_check(self, vector):
        return vector[self.vector[-1]] == 15 # TODO: make it not ugly af

    def get_dominant_vectors(self):
        dominant_vectors = list()
        # add starting vectors
        for i in self.vector:
            dominant_vectors.append(self.make_default_vectors(i))

        # get all combinations
        removed_vectors = list()
        while True:
            for start_vector in dominant_vectors:
                for component in self.vector:
                    new_vector = self.increase_component(start_vector, component)
                    if self.compare_values(start_vector, new_vector) and (new_vector not in dominant_vectors):
                        dominant_vectors.append(new_vector)
                        if start_vector not in removed_vectors:
                            removed_vectors.append(start_vector)
                dominant_vectors = [v for v in dominant_vectors if (v not in removed_vectors)]

                if self.end_of_batch_check(start_vector): # TODO: no comment needed
                    break
            if self.end_of_batch_check(start_vector):
                break
        return dominant_vectors

    def convert_into_vector(self, _dict):
        vector = list()
        for val in _dict.values():
            vector.append(val)
        return tuple(vector)

    def get_sample_vectors(self):
        vectors = self.get_dominant_vectors()
        sample_vectors = list()
        for vect in vectors:
            sample_vectors.append(self.convert_into_vector(vect))
        return sample_vectors

    def dump_into_txt(self, matrix):
        with open("matrix.txt", 'w') as file:
            file.write(str(tuple(self.vector)) + '\n')
            for i in matrix:
                file.write(str(i))
                file.write('\n')

h = Hasse([40,60,80,100], 15)
mx = h.get_sample_vectors()
h.dump_into_txt(mx)
print(mx)
