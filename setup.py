from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="SkateStreet",
    version="1.0",
    description="Skate Street game",
    opitions={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)
