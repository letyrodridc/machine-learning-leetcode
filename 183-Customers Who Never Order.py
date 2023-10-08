# 183. Customers Who Never Order
# https://leetcode.com/problems/customers-who-never-order/?lang=pythondata

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    df = df[df['id_y'].isna()][['name']]
    df.columns = ['Customers']
    return df