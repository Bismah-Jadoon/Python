st = "\nThis is a string that we append "

f = open("myfile.txt", "a") #it will generate a file with name myfile.txt 

f.write(st) # write the string (st) in the file

f.close()