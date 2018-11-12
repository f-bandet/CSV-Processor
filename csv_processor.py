### 
### Author: Faye Bandet
### Course: CSC 110
### Description: This is a program that processes a CSV file and finds the average, min, or max or a specified column.
###
def main():
    csv_file = input('Enter CSV file name: \n')
    column = int(input('Enter column number: \n'))
    operation = input('Enter column operation: \n')
    csv_f = open(csv_file, 'r')
    csv_data = []
    for line in csv_f:
        line = line.strip('\n')
        values = line.split(',')
        csv_data.append(values)
    list_csv_data = csv_data
    list_csv_data = [[(float(j)) for j in i] for i in list_csv_data]
    if operation == 'avg':
        find_avg(list_csv_data, column)
    elif operation == 'min':
        find_min(list_csv_data, column)
    elif operation == 'max':
        find_max(list_csv_data, column)
    else:
        print('Error')

def find_avg(list_csv_data, column):
### Finds the average from the data.
    average_list = []
    i = 0
    for i in range(0, len(list_csv_data)):
        number = list_csv_data[i][column - 1]
        average_list.append(number)
        i += 1
    average = float(sum(average_list)/len(average_list))
    print('The average for column', column, 'is:', average)

def find_min(list_csv_data, column):
### Uses the min function to determine the minimum.
    min_value = []
    for i in range(0, len(list_csv_data)):
        number = list_csv_data[i][column - 1]
        min_value.append(number)
        i += 1
    minimum = float(min(min_value))
    print('The minimum value in column', column, 'is:', minimum)
    
def find_max(list_csv_data, column):
### Uses the max function to determine the maximum.
    max_value = []
    for i in range(0, len(list_csv_data)):
        number = list_csv_data[i][column - 1]
        max_value.append(number)
        i += 1
    maximum = float(max(max_value))
    print('The maximum value in column', column, 'is:', maximum)
main()