from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pulp"]}

setup(
    name="kehelyopt",
    version="0.1",
    description="Kehely gyartas optimalizalasa",
    packages=["Model"],
    options={"build_exe": build_exe_options},
    executables=[Executable("Model/kehelyopt.py")],
)