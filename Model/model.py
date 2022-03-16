# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help
from pulp import *
# pulpTestAll()
from dominant_vectors import SampleVectorGenerator
from Adatbázis import adatbazis as db


class LpModel:
    def __init__(self, name, quantity, sample_vectors):
        self.name = name
        self.quantity = quantity
        self.sample_vectors = sample_vectors

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception
        self._name = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, list):
            raise Exception
        self._quantity = value

    @property
    def sample_vectors(self):
        return self._sample_vectors

    @sample_vectors.setter
    def sample_vectors(self, value):
        if not isinstance(value, list):
            raise Exception
        self._sample_vectors = value

    def read_data_from_file(self, path):
        with open(path, 'r') as file:
            pass # TODO: Fucking .txt

    def generate_variables(self):
        variables = list()
        for vector in self.sample_vectors:
            name = 'x_'
            for i in vector:
                name += str(i)
            variables.append(LpVariable(name, 0, upBound=None, cat=LpInteger))
        return variables

    def get_coefficients(self, index):
        coefficents = list()
        for i in self.sample_vectors:
            coefficents.append(i[index])
        return coefficents

    # 2d korl feltetelekre dupla list comprehension (?)
    def build_model(self):
        prob = LpProblem(self.name, LpMinimize)

        lp_vars = self.generate_variables()
        prob += lpSum([var for var in lp_vars])

        for i in range(len(self.quantity)):
            coefficients = self.get_coefficients(i)
            prob += lpSum([coefficients[j] * lp_vars[j] for j in range(len(lp_vars))]) >= self.quantity[i]

        return prob

    def solve_lp(self, model):
        model.writeLP("test.lp")
        model.solve()
        print("Status: ", LpStatus[model.status])
        for v in model.variables():
            print(v.name, "=", v.varValue)


_quantity = [i[-1] for i in db.meret]
lengths = list(set([i for i in itertools.chain(*db.meret) if i not in _quantity]))  # 20000000000iq

lengths = [int(i*100) for i in lengths]
svg = SampleVectorGenerator(vector=lengths, max_size=600)
svg.get_sample_vectors()
test = LpModel("test", _quantity, svg.sample_vectors)

# test = LpModel("test", [70, 100, 120],
#                [(2, 0, 1), (1, 2, 0), (1, 1, 1), (1, 0, 3), (0, 3, 1), (0, 2, 2), (0, 1, 4), (0, 0, 6)])
# model = test.build_model()
# test.solve_lp(model)
# test.read_data_from_file(os.path.abspath("../Adatbázis/meret.txt"))

model = test.build_model()
test.solve_lp(model)
