# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help
from pathlib import Path
from pulp import *


# pulpTestAll()

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
            raise Exception  # TODO: vmi ertelmes
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
        with open("meret.txt", 'r') as file:
            pass

    def generate_variables(self):
        variables = list()
        for vector in self.sample_vectors:
            name = 'x_'
            for i in vector:
                name += str(i)
            variables.append(LpVariable(name, 0, upBound=None, cat=LpInteger))
        return variables

    def get_coefficents(self, index):
        coefficents = list()
        for i in self.sample_vectors:
            coefficents.append(i[index])
        return coefficents

    # 2d korl feltetelekre dupla list comprehension (?)
    def build_model(self):
        prob = LpProblem(self.name, LpMinimize)

        lpVars = self.generate_variables()
        prob += lpSum([var for var in lpVars])

        for i in range(len(self.quantity)):
            coefficents = self.get_coefficents(i)
            prob += lpSum([coefficents[j] * lpVars[j] for j in range(len(lpVars))]) >= self.quantity[i]

        return prob

    def solve_lp(self, model):
        model.writeLP("test.lp")
        model.solve()
        print("Status: ", LpStatus[model.status])
        for v in model.variables():
            print(v.name, "=", v.varValue)


test = LpModel("test", [70, 100, 120],
               [(2, 0, 1), (1, 2, 0), (1, 1, 1), (1, 0, 3), (0, 3, 1), (0, 2, 2), (0, 1, 4), (0, 0, 6)])
model = test.build_model()
test.solve_lp(model)
