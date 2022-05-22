# python -m pip install -U git+https://github.com/coin-or/pulp      <- terminalba
# https://coin-or.github.io/pulp/CaseStudies/index.html             <- help
from pulp import *
import dominant_vectors as dv
import database as db
import pandas as pd
class LpModel:
    def __init__(self, name, quantity, sample_vectors):
        self.name = name
        self.quantity = quantity
        self.sample_vectors = sample_vectors

    def generate_variables(self, name):
        variables = list()
        for vector in self.sample_vectors:
            var_name = name
            for i in vector:
                var_name += str(i)
            variables.append(LpVariable(var_name, 0, upBound=None, cat=LpInteger))
        return variables


    def get_coefficients(self, index):
        global lut
        component = lengths.index(lut.iloc[index]["lenght"])
        coefficents = list()

        for i in self.sample_vectors:
            coefficents.append(i[component])
        return coefficents

    def build_model(self):
        prob = LpProblem(self.name, LpMinimize)

        lp_x_vars = self.generate_variables("x_")
        lp_y_vars = self.generate_variables("y_")

        prob += lpSum([lp_x_vars[i] + lp_y_vars[i] for i in range(len(lp_x_vars))])

        for i in range(len(self.quantity)):
            coefficients = self.get_coefficients(i)
            prob += lpSum([coefficients[j] * lp_x_vars[j] for j in range(len(lp_x_vars))]) >= self.quantity[i]

        for i in range(len(lp_y_vars)):
            prob += lpSum([lp_x_vars[i] - 1000 * lp_y_vars[i]]) <= 0

        return prob


def solve_lp(model):
    model.writeLP("test.lp")
    model.solve()
    print("Status: ", LpStatus[model.status])
    for v in model.variables():
        print(v.name, "=", v.varValue)

def get_data():
    matrix = list()
    with open("/Users/szameltamas/Desktop/KESZ_projekt/Others/elements.txt", 'r') as file:
        content = file.readlines()
        content = [row.strip('\n') for row in content]
        for row in content:
            separated = row.split(';')
            temp = [int(i) for i in separated]
            matrix.append(temp)
    return matrix


lut = pd.DataFrame(get_data(), columns=["id", "lenght", "width", "quantity"]).drop(columns=["id"])
lengths = sorted(list(set(lut["lenght"].tolist()).union(set(lut["width"].tolist()))))
_quantity = lut["quantity"].tolist()


lp = LpModel("test", _quantity, dv.get_sample_vectors())
kehely_model = lp.build_model()
solve_lp(kehely_model)