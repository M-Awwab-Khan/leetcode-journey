import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    largest = -float(inf)
    second_largest = largest
    for salary in employee.salary.values:
        if salary > largest:
            second_largest = largest
            largest = salary
        elif salary > second_largest and salary != largest:
            second_largest = salary
    if largest == second_largest:
        second_largest = None
    return pd.DataFrame({'SecondHighestSalary': [second_largest]})