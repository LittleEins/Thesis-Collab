import csv # Module to import to open a csv file

# Opening csv file named 'AttendanceReport.csv' and assigning objectName as 'file'
with open('AttendanceReport.csv', 'r') as file:
    #Create reader object by passing 'file' in csv.reader() function
    reader = csv.reader(file)
    #For loops in reading the row(variable of csv module) in object 'reader'
    for row in reader:
        #printing row
        print('|'.join(row))
