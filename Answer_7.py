# Create a new column qty which displays the quantity of product purchased.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
numerical_features = df.select_dtypes(include=['number'])

numeric_df = numerical_features.copy()
numeric_df['qty'] = numeric_df['Total_Amount'] / numeric_df['Amount']
print(numeric_df)


"""Output:
        Transaction_ID  Customer_ID       Phone  Zipcode  Age  Year  \
0              8691788        37249  1414786801    77985   21  2023   
1              2174773        69749  6852899987    99071   19  2023   
2              6679610        30192  8362160449    75929   48  2023   
3              7232460        62101  2776751724    88420   56  2023   
4              4983775        27901  9098267635    48704   22  2024   
...                ...          ...         ...      ...  ...   ...   
293906         4246475        12104  7466353743     4567   31  2024   
293907         1197603        69772  5754304957    16852   35  2023   
293908         7743242        28449  9382530370    88038   41  2024   
293909         9301950        45477  9373222023    67608   41  2023   
293910         2882826        53626  9518926645    25242   28  2024   

        Total_Purchases      Amount  Total_Amount  Ratings  qty  
0                     3  108.028757    324.086270        5  3.0  
1                     2  403.353907    806.707815        4  2.0  
2                     3  354.477600   1063.432799        2  3.0  
3                     7  352.407717   2466.854021        4  7.0  
4                     2  124.276524    248.553049        1  2.0  
...                 ...         ...           ...      ...  ...  
293906                5  194.792597    973.962984        1  5.0  
293907                1  285.137301    285.137301        5  1.0  
293908                3   60.701761    182.105285        2  3.0  
293909                1  120.834784    120.834784        4  1.0  
293910                7  340.319059   2382.233417        2  7.0  

[293911 rows x 11 columns]
"""