import model, vectors

df = vectors.read_from_file()
lp = model.LpModel("result", df)
kehely_model = lp.build_model()
model.solve_lp(kehely_model)