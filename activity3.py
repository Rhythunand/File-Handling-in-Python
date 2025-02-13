file = open('Codingal.txt', 'r')
counter = 0

Content = file.read()
colist = Content.split("\n")

for i in colist :
  if i :
    counter += 1

print("The number of lines in the file :")
print(counter)