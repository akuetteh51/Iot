import csv

txt=open("en.txt",'w')
data = open("ai.csv",'r')
# print(data.read())
read=csv.reader(data)
for line in read:
    print(line[5])
    txt.write(line[5]+"\n")


data.close()
txt.close()