import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N > salaries.shape[0] or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [salaries.iloc[N - 1]]})