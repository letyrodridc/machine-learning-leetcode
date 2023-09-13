# https://leetcode.com/problems/find-total-time-spent-by-each-employee/?lang=pythondata
import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"]-employees["in_time"]
    res = employees.groupby(["emp_id", "event_day"]).sum()
    res = res.reset_index()
    res = res.rename(columns={"event_day": "day"})
    return res[["day","emp_id","total_time"]]