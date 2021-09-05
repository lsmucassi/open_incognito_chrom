import os

with open('resources.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(f"opening... {line}")
        line = reader.readline()
        os.system(f"open -na \"Google Chrome\" --args --incognito \{line}")
