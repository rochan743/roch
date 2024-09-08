file1 = open("football.txt" , "r")
file2 = open("rugby.txt" , "r")

n = open("f2r.txt" , "x")
n.write(file1.read() + "\n" + "\n" + file2.read())

n.close()
file1.close()
file2.close()