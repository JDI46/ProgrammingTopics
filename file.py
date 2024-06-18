#how to open a file
# file = open('file.txt', 'r')
# print(file.read())
# file.close()

# #how to open file as variable
# with open("file.txt", "r") as file:
#     line1 = file.readlines()[0]
#     print([line1.strip()])
# #a /n will pop up so I need to be able to remove those from this list. Above is how
# with open("file.txt", "r") as file:
#     line1 = file.readw
#     line1 = line1.replace("/n", "")
#     print(line1)
# #to remove all the white space for all it it
# #how to write and replace file
# with open("file2.txt", "w") as file:
#     file.write("This is a new file")
# #changing the text can overwride the file. 
#     file.write('to write\n')
# #this is how to append more lines

#this is append a mode
# with open("file2.txt", "a") as file:
#     file.write("\nThis is a new file")

# with open("file2.txt", "r+") as file:
#     score = file.read()
#     new_score = int(score) + 1
#     file.write(str(new_score))

with open('file2.txt', 'r+') as file:
    # lines = file.readlines()[:3]
    for line in file:
        print(line)
