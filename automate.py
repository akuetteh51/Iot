import csv
s =open('Event.csv','r')
w=open('Event.txt','w')
line= csv.reader(s)

for lin in line:
    print(lin[5],"\n")
    w.write(lin[5]+"\n")
s.close()
w.close()