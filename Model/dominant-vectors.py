import numpy as np, pandas as pd

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

# test_arr = [[10, 0, 0], [10, 5, 0], [0, 10, 20]]
# test = Matrix([40,60,80], test_arr)
# print(test)