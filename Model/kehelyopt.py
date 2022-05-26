import model

df = model.read_data()
lp = model.LpModel("result", df)
kehely_model = lp.build_model()
model.solve_lp(kehely_model)