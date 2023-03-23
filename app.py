employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
# print(employee_file.readline())
# print(employee_file.readlines()[1])

employee_file = open("employee.txt", "a")
employee_file.write("\nTat Oduor - Human Resource")
employee_file.close()


