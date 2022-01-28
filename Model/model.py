# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help

from pulp import *
# pulpTestAll()

class LpModel:
    def __init__(self, name, type, obj_function, constraints, variables):
        self.name = name
        self.type = type # min/max
        self.obj_function = obj_function # ex: [0.013, 0.008]
        self.constraints = constraints # TODO: formatum? -> dict ahol KEY a <=, =, =>, VALUE list of tuples?
        self.variables = variables # list of tuples ex: [(1,0,0,0), (0,1,0,0), (0,0,1,0), ...]
    
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

    def read_data_from_csv(self, path):
        pass

    def generate_variables(self):
        pass

    def generate_constraints(self):
        pass

    def generate_obj_function(self):
        pass

    def build_model(self):
        prob = LpProblem(self.name, self.type)

    def __str__(self):
        pass
