file_r = open('Codingal.txt', 'r')
print("File in read mode :")
print(file_r.read())
file_r.close()

file_w = open('Codingal.txt', 'w')
file_w.write(" File in write mode")
file_w.write("Hi! I am a penguin. I'm an year old ")
file_w.close()

file_a = open('Codingal.txt', 'a')
file_a.write("\n File in append mode")
file_a.write("Hi! I am a penguin. I'm an year old")
file_a.close()