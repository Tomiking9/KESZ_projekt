import model, dominant_vectors as dv
import pandas as pd

lengths = list()
_quantity = list()
matrix = list()
with open("/Users/szameltamas/Desktop/KESZ_projekt/Others/elements.txt", 'r') as file:
    content = file.readlines()
    content = [row.strip('\n') for row in content]
    for row in content:
        separated = row.split(';')
        temp = [int(i) for i in separated]
        matrix.append(temp)

        if int(separated[1]) not in lengths:
            lengths.append(int(separated[1]))
        if int(separated[2]) not in lengths:
            lengths.append(int(separated[2]))
        _quantity.append(int(separated[3]))


df = pd.DataFrame(matrix, columns=["id", "lenght", "width", "quantity"])
df = df.drop(columns=["id"])
print(df)
#lp = model.LpModel("test", _quantity, dv.get_sample_vectors())
# kehely_model = lp.build_model()
# model.solve_lp(kehely_model)