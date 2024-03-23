with open("file1.txt", "w") as file:
    file.write("Hello World From Python.")
    file.write("File Handling From Python.")
    file.write("Writing On File In Python.")
    file.write("Writing On File With overiding In Python.")
    
with open("file1.txt", "a") as file:
    file.write("\n File Handling and append the text")

    
with open("example.bin", "wb") as file:
    file.write(b"Binary data here.")

with open("example.bin", "rb") as file:
    content = file.read()
    print(content)
    