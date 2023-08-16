# pandas-playground
Pandas quick ref and practice problems

## Quick references
- [Pandas cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Pandas Series Reference](https://pandas.pydata.org/docs/reference/series.html)

## Concepts

### Filtering
- To reduce a DataFrame to a subset of rows meeting a criteria, the `.query('row_name > value')` method can be used
- To grab a subset of rows from the DF, specify the desired rows like `df[['row1', 'row2']]`
- Finding vals in one df but not in another: `df1[~df1['row1'].isin(df2['row1'])]`
- To remove duplicate entries from a df: `df.drop_duplicates(subset=['row1', 'row2'])`
  - To remove rows with null values: `df.dropna()`
- To filter a df based on a list of values: `df[df['row1'].isin(['val1', 'val2'])]`
