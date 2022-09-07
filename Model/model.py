import vectors
from pulp import *
class LpModel:
    def __init__(self, name, data):
        self.name = name
        self.quantity = data["quantity"].tolist()
        self.sample_vectors = data


    @property
    def sample_vectors(self):
        return self._sample_vectors


    @sample_vectors.setter
    def sample_vectors(self, data):
        items = vectors.find_cohesive_items(data)
        self._sample_vectors = vectors.generate_sample_vectors(items)


    def generate_variables(self, name):
        variables = list()
        for vector in self.sample_vectors:
            var_name = name
            for i in vector:
                var_name += str(i) + ';'
            variables.append(LpVariable(var_name, 0, upBound=None, cat=LpInteger))
        return variables


    def get_coefficients(self, index):
        coefficents = list()
        
        for vector in self.sample_vectors:
            coefficents.append(vector[index])
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

def read_data():
    return vectors.read_from_file()

def solve_lp(model):
    solver = pulp.PULP_CBC_CMD(timeLimit=vectors.config["time_limit"])
    model.writeLP(model.name + ".lp")
    model.solve(solver)

    result = dict()
    i=0
    for var in model.variables():
        print(var.name, "=", var.varValue)
        if var.varValue != 0 and var.name.split('_')[0] != 'y':
            i=i+1
            name = var.name.split('_')[1][:-1]
            result[int(var.varValue)*1000+i] = str(int(var.varValue)) + ';' + name + '\n'

    with open(model.name + ".txt", 'w') as file:
        row = ""
        for var in sorted(result.items(), reverse=True):
            row += var[1]
        file.writelines(row[:-1])