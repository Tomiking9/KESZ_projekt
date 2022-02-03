# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help
from pathlib import Path
from pulp import *
# pulpTestAll()

class LpModel:
    def __init__(self, name, type, obj_function, constraints, variables):
        self.name = name
        self.type = type # min/max
        self.obj_function = obj_function
        self.constraints = constraints
        self.variables = variables # separated sample vectors
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception # TODO: vmi ertelmes
        self._name = value
    
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if value == "min":
            return LpMinimize
        elif value == "max":
            return LpMaximize
        else:
            raise Exception
    
    @property
    def obj_funciton(self):
        return self._obj_function
    @obj_funciton.setter
    def obj_function(self, value):
        if not isinstance(value, list):
            raise Exception
        self._obj_function = value

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

    # TODO: dict -> list (?)
    def generate_variables(self):
        variables = list()
        for batch in range(len(self.variables)):
            temp = dict()
            for vector in self.variables[batch]:
                key = 'x_'
                for component in vector:
                    key += str(component)
                temp[LpVariable(key, LpInteger)] = vector[batch]
            variables.append(temp)
        return variables


    def generate_constraints(self):
        pass

    def generate_obj_function(self):
        pass

    def build_model(self):
        prob = LpProblem(self.name, self.type)

    def __str__(self):
        pass

test = LpModel("test", "min", list(), list(), [[(3, 0, 0, 0), (2, 1, 0, 0), (2, 0, 1, 0), (2, 0, 0, 1), (1, 2, 0, 0), (1, 1, 1, 0), (1, 1, 0, 1), (1, 0, 2, 0), (1, 0, 1, 1), (1, 0, 0, 2)], [(2, 1, 0, 0), (1, 2, 0, 0), (1, 1, 1, 0), (1, 1, 0, 1), (0, 3, 0, 0), (0, 2, 1, 0), (0, 2, 0, 1), (0, 1, 2, 0), (0, 1, 1, 1), (0, 1, 0, 2)], [(2, 0, 1, 0), (1, 1, 1, 0), (1, 0, 2, 0), (1, 0, 1, 1), (0, 2, 1, 0), (0, 1, 2, 0), (0, 1, 1, 1), (0, 0, 3, 0), (0, 0, 2, 1), (0, 0, 1, 2)], [(2, 0, 0, 1), (1, 1, 0, 1), (1, 0, 1, 1), (1, 0, 0, 2), (0, 2, 0, 1), (0, 1, 1, 1), (0, 1, 0, 2), (0, 0, 2, 1), (0, 0, 1, 2), (0, 0, 0, 3)]])
var = test.generate_variables()
print(var)
for i in var:
    for j in i.keys():
        print(str(j) + '\t' + str(type(j)))