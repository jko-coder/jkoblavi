# 1 - Create A single list

Employees_identification=[]
Employees_information=["1121", "1122", "1127", "1132", "1137", "1138", "1152", "1157", "1121", "1152"]

Employees_name=["Jackie Grainger", "Jignesh Thrakkar", "Dion Green", "Jacob Gerber", "Sarah Sanderson", "Brandon Heck", "David Toma", "Charles King", "Jackie Grainger", "David Toma"]
Employees_hourlywages=[22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75, 22.22, 22.65]
Bool_values=["False", "True", "True", "False", "False"]
# print(Employees_information, Employees_name, Employees_hourlywages, Bool_values)
Employees_files = [Employees_information, Employees_name, Employees_hourlywages, Bool_values]

Employees_identification.append(Employees_files)
# print(Employees_identification) 

Employee_database = open("text_files/Employeedatabase.csv")

for line in Employee_database:
    tmp_line = line.split(",")
#    print(tmp_line)

# 2 - Create Dictionary
Company_database =[]
Employees_information ={"1121", "1122", "1127", "1132", "1137", "1138", "1152", "1157", "1121", "1152"}
Employees_name ={"Jackie Grainger", "Jignesh Thrakkar", "Dion Green", "Jacob Gerber",
"Sarah Sanderson", "Brandon Heck", "David Toma", "Charles King", "Jackie Grainger", "David Toma"}
Employees_hourlywages ={22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75, 22.22, 22.65}
Bool_values ={"False", "True", "True", "False", "False"}

import json

json_file = open("text_files\Config_Employeedatabase.json")
Config_Employeedatabase = json.load(json_file)
json_file.close()

# print(Config_Employeedatabase)

# 3 No dupliate data in the dictionaries
Employee_database ={"Employee1":["1121", "Jackie Grainger", 22.22],
"Employee2":["1122", "Jignesh Thrakkar", 25.25],
"Employee3":["1127", "Dion Green" , 28.75, "FALSE"],
"Employee4": ["1132", "Jason Gerber", 24.32],
"Employee5":["1137", "Sarah Sanderson", 23.45, "TRUE"],
"Employee6":["1138", "Brandon Heck", 25.84, "TRUE"],
"Employee7":["1152", "David Toma",22.65],
"Employee8":["1157", "Charles King", 23.75, "FALSE"],
"Employee9":["1121", "Jackie Grainger", 22.22, "FALSE"],
"Employee10":["1152", "David Toma", 22.65]}

# print("the original dictionary is : " + str(Employee_database))
temp =[]
res = dict()
for key, val in Employee_database.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
        # print("The dictioanry after values removal : " + str(res))


# 4 Multiply the current hourly rate by 1.3 and provide the Total_Hourly_rate
Employees_hourlywages=[22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75, 22.22, 22.65]

for Total_Hourly_rate in Employees_hourlywages:
    # print(Total_Hourly_rate *1.3)

 Total_Hourly_rate ={37.375, 31.616, 30.485, 33.592, 29.445, 30.875, 28.886,}
 
Total_Hourly_rate ={37.375, 31.616, 30.485, 33.592, 29.445, 30.875, 28.886, 29.445}

Company_database.append(Total_Hourly_rate)
# print(Company_database)


# 4 Multiply the current hourly rate by 1.3 and provide the Total_Hourly_rate
Employee_database ={"Employee1":["1121", "Jackie Grainger", 22.22],
"Employee2":["1122", "Jignesh Thrakkar", 25.25],
"Employee3":["1127", "Dion Green" , 28.75, "FALSE"],
"Employee4": ["1132", "Jason Gerber", 24.32],
"Employee5":["1137", "Sarah Sanderson", 23.45, "TRUE"],
"Employee6":["1138", "Brandon Heck", 25.84, "TRUE"],
"Employee7":["1152", "David Toma",22.65],
"Employee8":["1157", "Charles King", 23.75, "FALSE"],
"Employee9":["1121", "Jackie Grainger", 22.22, "FALSE"],
"Employee10":["1152", "David Toma", 22.65]}

import json

json_file = open("text_files\Config_Employeedatabase.json")
Config_Employeedatabase = json.load(json_file)
json_file.close()
# print(Config_Employeedatabase)
Config_Employeedatabase[22.22]=22.22*1.3



Employees_hourlywages=[22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75, 22.22, 22.65]

for Total_Hourly_rate in Employees_hourlywages:
    # print(Total_Hourly_rate *1.3)

 Total_Hourly_rate ={37.375, 31.616, 30.485, 33.592, 29.445, 30.875, 28.886,}

# 5 Determine if anyone's total hourly rate is between 28.15 and 30.65.
#  If they are, add stored dictionary information on the person to a new list called underpaid_salaries.
Total_Hourly_rate ={37.375, 31.616, 30.485, 33.592, 29.445, 30.875, 28.886,}
Underpaid_salaries = [28.886, 29.445, 30.485]
# print(Underpaid_salaries)

# 6 Apply the if conditions
Employees_hourlywages=[22.22, 25.25, 28.75, 24.32, 23.45, 25.84, 22.65, 23.75, 22.22, 22.65]
Employees_name=["Jackie Grainger", "Jignesh Thrakkar", "Dion Green", "Jacob Gerber", "Sarah Sanderson", "Brandon Heck", "David Toma", "Charles King", "Jackie Grainger", "David Toma"]
Salaries_raise = [23.33, 26.26, 29.32, 25.29, 24.62, 26.87, 23.78]

for range in Employees_hourlywages:
    if range % 22< range <24:
        print(str(range +0.05))
    elif range % 24< range <26:
        print(str(range + 0.04))
    elif range % 26< range <28:
        print(str(range + 0.03))
    else:
        print(str(range + 0.02))

company_raise= dict(zip(Employees_name, Salaries_raise))
print(company_raise)

# 7 Print out all the data for this assignment
print(tmp_line)
print("The dictioanry after values removal : " + str(res))
print(company_raise)


    

        
        
        






