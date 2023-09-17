# https://leetcode.com/problems/delete-duplicate-emails
import pandas as pd


# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(keep='first', subset='email', inplace=True)



