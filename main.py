import csv

def mustClean():
    with open('Test.csv') as input, open('Test.csv', 'w', newline='') as output:
        write = csv.writer(output)
        for row in csv.reader(input):
            if any(field.strip() for field in row):
                write.writerow(row)


fields = []
rows = []

print("What is your choice ? update(1)/retreive(0)/modify(2)")
update = int(input())

if (update==1):
    with open("Test.csv", 'a') as csvfile:
        new = []
        print("Key : ")
        new += [input()]
        print("Value : ")
        new += [input()]
        print(new)

        writer = csv.writer(csvfile)
        writer.writerow(new)
        csvfile.close()


elif(update==0):
    with open("Test.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

        print("Enter the Key :")
        key = input()
        check = 0

        for i in rows:
            if i==[]:
                continue

            elif key == i[0]:
                print(i[1])
                check = 1
                break;

        if (check == 0):
            print("That Key Does Not Exist !")
        csvfile.close()

elif(update == 2):

    print("Which Key ? ")
    key = input()

    with open("Test.csv", 'r') as readfile:
        reader = csv.reader(readfile)
        check = 0
        lines = list(reader)

        for i in range (0,len(lines)):
            if lines[i] == []:
                continue
            if lines[i][0]==key:
                print("Give the Value")
                value = input()
                lines[i] = [key, value]
                check = 1

        if check == 0:
            print("That Key Does Not Exist !")

        with open("Test.csv", 'w') as writefile:
            writer = csv.writer(writefile)
            writer.writerows(lines)

            readfile.close()
            writefile.close()