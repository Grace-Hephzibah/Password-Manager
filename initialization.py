import csv

csvData = [["Key", "Value"], ["Gmail Account", "SecretKey"], ["College Site", "CollegeKey"]]

with open('Test.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csvData)
    file.close()