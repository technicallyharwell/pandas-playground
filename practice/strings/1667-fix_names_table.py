"""
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.



Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.
"""
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """
    approach:
    1 - set all chars in name to lower
    2 - set first char for each name to upper
    """
    # users['name'] = users['name'].str.lower()
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:]
    # return users.sort_values('user_id')

    # eliminate the first .lower() instruction
    # users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    # return users.sort_values('user_id')

    # using .capitalize() method    - fastest performance (beats others by ~18%)
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')



