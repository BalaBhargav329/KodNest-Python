# 1
products = {
"P101": ["Keyboard", 1200],
"P102": ["Mouse", 600],
"P103": ["Monitor", 8500]
}

print(products["P103"])
res = products.get("P103")
print(res)


# 2
employees = [
{"employee_id": "E101", "name": "Asha", "department": "Development"},
{"employee_id": "E102", "name": "Ravi", "department": "Testing"},
{"employee_id": "E103", "name": "Meera", "department": "Support"}
]

print(employees)

employee_by_id = {}

for employee in employees:
    employee_id = employee["employee_id"]
    employee_by_id[employee_id] = employee

print(employee_by_id)
