import os
# Clearing the Screen
os.system('cls')

'''
The text file 'icecream.txt' contains sales data report of 3 ice cream stores. The report is group by the flavour of the  ice cream.
Read the text file and create a dictionary as follow:​
'''

# 1. opens the text file
icecream_file = open("D:\Prasmul\Pelajaran\Semester 2\Intermediate Programming\Tugas Kumpul\LabIntermediatePrograming-RegineAngelinaH\Tugas Lab 5\icecream.txt", "r")


# 2. make a dictionary
sales_data = {}
while True : 
    oneline_icecream = icecream_file.readline()
    for i in oneline_icecream:
        list_per_line = oneline_icecream.strip().split(':') 
        key = list_per_line.pop(0)

        modif_list = [eval(i) for i in list_per_line]
        sum_per_flavor = sum(modif_list)
        # print(sum_per_flavor)
        list_per_line.append(sum_per_flavor)

        sales_data[key] = list_per_line
    if not oneline_icecream:
        break


# 3. SUM the dict
print("Dictionary sales:")
print(sales_data, "\n\n")

'''
From the dictionary, print a sales report. The report should:​
Show the sales of each flavour in each store.​
Show the sum of sales for each flavour ​
Show the sum of sales for each store​
Sorted by flavour.​
'''
# make it loop dari each index0 dari setiap key
sum_per_day = []
total_per_day = []

# for i in sales_data :
#     print(d[0])

for key, value in sales_data.items() : 
    value1, value2, value3, value4 = value
    sum_per_day.append(value1)
    modif_list2 = [eval(i) for i in sum_per_day]
    total_per_day.append(sum(modif_list2))

# print("ini yg sum_per_day",sum_per_day)
# print("ini yg total_per_day",total_per_day)

# 4. print in a report
def print_report() :
    print("{:<15} {:<10} {:<10} {:<10} {:<10}".format('FLAVOR', 'DAY 1', 'DAY 2','DAY 3', 'SUM PER FALVOR' ))
    
    # print each data item.
    for key, value in sales_data.items():
        value1, value2, value3, value4 = value
        print("{:<15} {:<10} {:<10} {:<10} {:<10}".format(key, value1, value2, value3, value4))

    # print("Total per Day ", *total_per_day, sep="   ")
    print("{:<15} {:<10} {:<10} {:<10} {:<10}".format("Total Per Day", total_per_day[1], total_per_day[2], total_per_day[3], total_per_day[4]))
    print("\n")

print_report()


with open("icecream_report.txt", "x") as file:
    file.write("ICE CREAM REPORT\n")
    file.write("================================================================\n")
    a = "FLAVOR"
    b = "DAY 1"
    c = "DAY 2"
    d = "DAY 3"
    e = "SUM PER FLAVOR"
    file.write(f"{a:<15} {b:<10} {c:<10} {d:<10} {e:<10}\n")
    for key, value in sales_data.items():
        value1, value2, value3, value4 = value
        file.write(f"{key:<15} {str(value1):<10} {str(value2):<10} {str(value3):<10} {str(value4):<10}\n")
        
    print(f"Report successfully written to icecream_report.txt")
    file.write("================================================================\n")
    g = "Total per Day"
    file.write(f"{g:<15} {total_per_day[1]:<10} {total_per_day[2]:<10} {total_per_day[3]:<10} {total_per_day[4]:<10}\n")
    file.write(f"\n\nMade by Regine Angelina H | NIM 23502310025")
    file.close()