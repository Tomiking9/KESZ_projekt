import copy

class Hasse:
    def __init__(self, vector, max_size):
        self.vector = vector
        self.max_size = max_size # gyartosor hossza
        self.sample_vectors = []

    @property
    def vector(self):
        return self._vector
    @vector.setter
    def vector(self, value):
        self._vector = value

    @property
    def max_size(self):
        return self._max_size
    @max_size.setter
    def max_size(self, value):
        self._max_size = value


    def get_start_vectors(self):
        res = list()
        for i in self.vector:
            temp = dict()
            for j in self.vector:
                temp[j] = 0
            temp[i] = self.max_size // i
            res.append(temp)
        return res

    def get_component(self, vector):
        for k,v in vector.items():
            if v != 0: return k

    def calculate_length(self, vector):
        _sum = 0
        for k,v in vector.items():
            _sum += (k*v)
        return _sum

    def get_fit(self, vector, pos):
        for k,v in vector.items():
            if k == pos: continue
            length = self.calculate_length(vector)
            if length + k < self.max_size:
                new_vect = vector.copy()
                new_vect[k] += ((self.max_size - length) // k)
                if new_vect not in self.sample_vectors:
                    self.sample_vectors.append(new_vect)


    def get_all_combinations(self, vector):
        res = list()
        pos = self.get_component(vector)
        while vector[pos] > 0:
            vector[pos] -= 1
            self.get_fit(vector.copy(), pos)

# eleg a minimalisat belereakni (?), vegyeseket hogy, duplikaltak torlese

    def get_sample_vectors(self, start_vectors):
        for vector in start_vectors:
            self.get_all_combinations(vector)



h_test = Hasse([100, 160, 250], 600)
h_test.get_sample_vectors(h_test.get_start_vectors())
h = Hasse([100, 110, 120, 175], 600)

# h = Hasse([100, 110, 120, 175], 4)
# mx = h.get_sample_vectors()
# print(mx)
