import employee_info

def test_get_employees_by_age():
    result = []
    input_lower_limit = 20
    input_upper_limit = 26
    correct = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    result = employee_info.get_employees_by_age_range(input_lower_limit,input_upper_limit)

    assert(result == correct)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    correct = 60166.67

    assert(result == correct)

def test_get_employees_by_dept():
    result = []
    input_dept = "Marketing"
    correct = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]

    result = employee_info.get_employees_by_dept(input_dept)

    assert(result == correct)