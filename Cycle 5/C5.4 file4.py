import csv


f=open('D:\csv.csv', 'r')
c = csv.reader(f)
for row in c:
    print(row)
