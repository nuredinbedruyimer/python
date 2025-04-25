
import os
class ChangeDir:
    def __init__(self, dest):
        self.dest = dest
    def __enter__(self):
        self.curr_working_dir = os.getcwd()
        os.chdir(self.dest)
    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir(self.curr_working_dir)
        
with ChangeDir("NewGen"):
    print(os.listdir())
with ChangeDir("OldGen"):
    print(os.listdir())
        