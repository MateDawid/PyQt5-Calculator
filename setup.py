from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "math", "PyQt5.QtWidgets", "PyQt5.QtGui", "sys"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name="PyQt5Calculator",
    options=options,
    version="1.0",
    description='Simple object-oriented calculator',
    executables=executables
)