# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help
from pathlib import Path
from pulp import *
# pulpTestAll()

class LpModel:
    def __init__(self, name, constraints, variables):
        self.name = name
        self.constraints = constraints
        self.variables = variables # sample vectors
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception # TODO: vmi ertelmes
        self._name = value

    
    @property
    def constraints(self):
        return self._constraints
    @constraints.setter
    def constraints(self, value):
        if not isinstance(value, list):
            raise Exception
        self._constraints = value

    @property
    def variables(self):
        return self._variables
    @variables.setter
    def variables(self, value):
        if not isinstance(value, list):
            raise Exception
        self._variables = value

    def read_data_from_file(self, path):
        with open("meret.txt", 'r') as file:
            pass

    def generate_variables(self):
        variables = list()
        for vector in self.variables:
            name = 'x_'
            for i in vector:
                name += str(i)
            variables.append(LpVariable(name, 0, upBound=None, cat=LpInteger))
        return variables

    def get_coefficents(self, index):
        coefficents = list()
        for i in self.variables:
            coefficents.append(i[index])
        return coefficents

    def build_model(self):
        prob = LpProblem(self.name, LpMinimize)

        lpVars = self.generate_variables()
        prob += lpSum([var for var in lpVars])

        for i in range(len(self.constraints)):
            coefficents = self.get_coefficents(i)
            prob += lpSum([coefficents[j] * lpVars[j] for j in range(len(lpVars))]) >= self.constraints[i]

        return prob

    def solve_lp(self, model):
        print(model.objective)
        for k,v in model.constraints.items():
            print(k,v)
        model.writeLP("test.lp")
        model.solve()
        print("Status: ", LpStatus[model.status])
        for v in model.variables():
            print(v.name, "=", v.varValue)

test = LpModel("test", [70, 100, 120], [(2, 0, 1), (1, 2, 0), (1, 1, 1), (1, 0, 3), (0, 3, 1), (0, 2, 2), (0, 1, 4), (0, 0, 6)])
model = test.build_model()
test.solve_lp(model)

