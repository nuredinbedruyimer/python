with open("file1.txt", "r") as file:
    file_content = file.read()
    print(file_content)
with open("file1.txt", "r") as file:
    file_content = file.readline()
    # print(file_content)
with open("file1.txt", 'r') as file:
    file_content = file.readlines()
    print(file_content)
    
    