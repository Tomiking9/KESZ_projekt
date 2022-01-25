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

    def powerset(self):
        s = list(self.vector)
        return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1)) # no empty set

    def is_subset(self, set, element):
        for i in set:
            if i.sort() == element.sort():
                return True
        return False

    def dominant_vectors(self):
        res = list()
        # add starting vectors TODO: separate function
        for i in self.vector:
            res.append([i])
        print(res)

        # add combinations TODO: separate function
        for i in range(3):
            for j in self.vector:
                temp = list()
                temp.append(self.vector[i]), temp.append(j)
                # check for subset
                if not self.is_subset(res, temp):
                    res.append(temp)
        print(res)

h = Hasse([40,60,80])
h.dominant_vectors()

