"""
PROBLEM STATEMENT:
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicate the same person.



Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.
"""
import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # authors who viewed their own articles will have rows where author_id == viewer_id
    # we will identify these rows, take only the unique author_id's present, and then sort
    df = views.query('author_id == viewer_id')
    df = df[['author_id']].rename(columns={'author_id': 'id'})
    df = df.drop_duplicates()
    return df.sort_values('id')



