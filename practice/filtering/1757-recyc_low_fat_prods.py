"""
PROBLEM STATEMENT:
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.



Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.
"""

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res = products.query('low_fats == "Y" and recyclable == "Y"')
    res = res[['product_id']]

    return res


