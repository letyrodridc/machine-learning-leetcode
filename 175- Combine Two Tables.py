# https://leetcode.com/problems/combine-two-tables/?lang=pythondata
import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = person.merge(address, left_on='personId', right_on='personId', how='left')
    df = df[['lastName', 'firstName', 'city', 'state']]
    return df
