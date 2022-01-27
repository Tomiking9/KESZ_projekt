import copy
import numpy as np, pandas as pd
from itertools import chain, combinations

class Matrix:
    def __init__(self, vector, quantity):
        self.vector = vector
        self.quantity = quantity
    
    @property
    def vector(self):
        return self._vector
    # TODO: error handling
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


# peti
# test_arr = [[10, 0, 0], [10, 5, 0], [0, 10, 20]]
# test = Matrix([40,60,80], test_arr)
# print(test)

        
test_arr = [[10, 0, 0], [10, 5, 0], [0, 10, 20]]
test = Matrix([40,60,80], test_arr)
print(test)

class Hasse:
    def __init__(self, vector):
        self.vector = vector
    
    @property
    def vector(self):
        return self._vector
    @vector.setter
    def vector(self, value):
        self._vector = value

    def make_default_vector(self, pos):
        empty = dict()
        for i in self.vector:
            empty[i] = 0
        empty[pos] = 1
        return empty

    def compare_values(self, original_vect, new_vect):
        original_vect_components = list(original_vect.values())
        new_vect_components = list(new_vect.values())

        return new_vect_components > original_vect_components # TODO: not gud, make it gud

    def make_vector(self, vector, pos):
        copy_vect = copy.copy(vector)
        copy_vect[pos] += 1
        return copy_vect

    def dominant_vectors(self):
        res = list()
        # add starting vectors TODO: separate function
        for i in self.vector:
            res.append(self.make_default_vector(i))

        bad_vectors = list()
        while True:
            for i in res:
                for k in self.vector:
                    new_vect = self.make_vector(i, k)
                    if self.compare_values(i, new_vect) and (new_vect not in res):
                        res.append(new_vect)
                        if i not in bad_vectors:
                            bad_vectors.append(i)
                res = [item for item in res if (item not in bad_vectors)]
                if (len(res) > 1000):
                    break
            if (len(res) > 1000):
                break

        with open("vectors.txt", 'w') as file:
            for i in res:
                file.write(str(i) + '\n')
            



h = Hasse([40,60,80,100])
h.dominant_vectors()

