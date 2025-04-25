class OpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        
with OpenFile("file1.txt", "w") as file:
    file.write(" I love one peice anime more than any other anime by far")
    
print(f"is the file closed : {"YES" if file.closed else "NO"}")