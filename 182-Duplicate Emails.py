# https://leetcode.com/problems/duplicate-emails/?lang=pythondata
import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(person[person["email"].duplicated(keep='last')]["email"].unique(), columns=["email"])