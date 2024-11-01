import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(20, 30)

    expected_result = [
        {'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000},
        {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}
    ]

    assert (result == expected_result)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    expected_result = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6  # Calculate based on the actual data
    
    assert (result == expected_result)

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Engineering")

    expected_result = [
        {'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000},
        {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}
    ]

    assert (result == expected_result)