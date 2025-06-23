import os
def is_python_installed():
  os.system("python --version") # if python is installed it should say something like 3.1.0
if __name__ == "__main__":
  is_python_installed()
