import cx_Freeze
from cx_Freeze import *

setup(
    name = "interfaz",
    options = {'build_exe': {'packages': ['cv2', 'numpy']}},
    executables=[
        Executable(

            "interfaz.py",
        )
    ]
)