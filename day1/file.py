print("FILES")
print("*open - use - close*")

str = input("Input some text ")
str += '\n'

files = open('data/text.txt', 'a')
files.write(str)
files.close()


files = open('data/text.txt','rt')
print(files.read(3))
for line in files:
    print(line)
files.close
