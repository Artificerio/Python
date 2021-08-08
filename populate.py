import os
import sys

class dirVars:
    project_name = ""
    directory = ""
    parent_dir = ""
    path = ""

    def __init__(self, u_pn, u_dir, u_par_dir, u_path):
        self.project_name = u_pn
        self.directory = u_dir
        self.parent_dir = u_par_dir
        self.path = u_path

    @staticmethod
    def isValid(path):
        if(os.path.exists(path)):
            print("Path %s already exists" %path)

    @staticmethod
    def createDir(directory):
        os.mkdir(directory)
        print("Project was created")

    @staticmethod
    def populate(path):
        os.chdir(path)
        path = "/home/artem/.vim/templates/standart.cpp"
        with open(path, 'r') as rf:
            with open("main.cpp", 'w') as wf:
                for line in rf:
                    wf.write(line)
        
        cmakelists = "/home/artem/.vim/templates/CMakeLists.txt"
        with open(cmakelists, 'r') as rf:
            with open("CMakeLists.txt", 'w') as wf:
                for line in rf:
                    wf.write(line)



print("Enter your project_name: \n")

u_pn = input()
u_dir = u_pn
u_par_dir = "/home/artem/code/SFML"
u_path = os.path.join(u_par_dir, u_dir)

project_x = dirVars(u_pn,u_dir,u_par_dir,u_path)
project_x.isValid(project_x.path)

project_x.createDir(project_x.directory)
project_x.populate(project_x.path)
