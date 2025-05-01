class LineReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def __iter__(self):
        with open(self.file_path) as file:
            for line in file:
                yield line.strip()
                
                
for line in LineReader("test.txt"):
    print(line)