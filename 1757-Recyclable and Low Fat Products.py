# https://leetcode.com/problems/recyclable-and-low-fat-products/?lang=pythondata
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')].product_id)