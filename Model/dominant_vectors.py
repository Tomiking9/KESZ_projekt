import copy


class SampleVectorGenerator:
    def __init__(self, vector, max_size):
        self.vector = vector      # kelyhek hossza
        self.max_size = max_size  # gyartosor hossza
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

    def get_minimal_element(self):
        return min(*self.vector)

    def get_start_vectors(self):
        res = list()
        for i in self.vector:
            temp = dict()
            for j in self.vector:
                temp[j] = 0
            temp[i] = self.max_size // i
            res.append(temp)
        for i in res:
            _i = i.copy()
            if self.calculate_length(_i) > self.max_size - self.get_minimal_element():
                self.sample_vectors.append(_i)
        return res

    def get_starting_component(self, vector):
        for k, v in vector.items():
            if v != 0: return k

    def calculate_length(self, vector):
        _sum = 0
        for k,v in vector.items():
            _sum += (k*v)
        return _sum

    def get_fit(self, vector, pos):
        for key in vector.keys():
            if key == pos: continue
            length = self.calculate_length(vector)
            if length + key <= self.max_size:
                new_vect = vector.copy()
                # new_vect[k] += ((self.max_size - length) // k)
                new_vect[key] += 1
                self.get_fit(new_vect, pos)
                if new_vect not in self.sample_vectors and self.calculate_length(new_vect) > \
                        (self.max_size - self.get_minimal_element()):
                    self.sample_vectors.append(new_vect)

    def get_all_combinations(self, vector):
        pos = self.get_starting_component(vector)
        while vector[pos] > 0:
            vector[pos] -= 1
            self.get_fit(vector.copy(), pos)

    def get_sample_vectors(self):
        start = self.get_start_vectors()
        for vector in start:
            self.get_all_combinations(vector)


# h_test1 = SampleVectorGenerator([40,60,80], 600)
# h_test2 = SampleVectorGenerator([100,160,250], 600)
# h_test3 = SampleVectorGenerator([40, 60, 80, 100], 600)

# h_test1.get_sample_vectors()
# for i in h_test1.sample_vectors:
#     print(i)
# print("---------------------")

# h_test2.get_sample_vectors()
# for i in h_test2.sample_vectors:
#     print(i)
# print("---------------------")

# h_test3.get_sample_vectors()
# for i in h_test3.sample_vectors:
#     print(i)

h = SampleVectorGenerator([110, 100, 120, 175], 600)
h.get_sample_vectors()
for i in h.sample_vectors:
    print(i)
print(len(h.sample_vectors))

