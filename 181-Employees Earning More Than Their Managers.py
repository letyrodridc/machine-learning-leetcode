# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/?lang=pythondata
import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee2 = employee.copy()
    employee2 = employee2.drop("managerId", axis=1)
    employee2 = employee2.rename(columns={"id": "managerId"})
    inner_join = pd.merge(employee2,
                          employee,
                          on='managerId',
                          how='inner')

    inner_join = inner_join.rename(columns={"name_y": "Employee"})
    inner_join = inner_join[inner_join["salary_y"] > inner_join["salary_x"]]
    return inner_join[["Employee"]]
