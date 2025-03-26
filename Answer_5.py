# Put sr_no. column in the start of the data frame.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
numerical_features = df.select_dtypes(include=['number'])

numeric_df = numerical_features.copy()
numeric_df["Serial_Number"] = numeric_df.index + 1

numeric_df.insert(0, "Serial_Number", numeric_df.pop("Serial_Number"))
print(numeric_df)


"""Output:
        Serial_Number  Transaction_ID  Customer_ID       Phone  Zipcode  Age  \
0                   1         8691788        37249  1414786801    77985   21   
1                   2         2174773        69749  6852899987    99071   19   
2                   3         6679610        30192  8362160449    75929   48   
3                   4         7232460        62101  2776751724    88420   56   
4                   5         4983775        27901  9098267635    48704   22   
...               ...             ...          ...         ...      ...  ...   
293906         293907         4246475        12104  7466353743     4567   31   
293907         293908         1197603        69772  5754304957    16852   35   
293908         293909         7743242        28449  9382530370    88038   41   
293909         293910         9301950        45477  9373222023    67608   41   
293910         293911         2882826        53626  9518926645    25242   28   

        Year  Total_Purchases      Amount  Total_Amount  Ratings  
0       2023                3  108.028757    324.086270        5  
1       2023                2  403.353907    806.707815        4  
2       2023                3  354.477600   1063.432799        2  
3       2023                7  352.407717   2466.854021        4  
4       2024                2  124.276524    248.553049        1  
...      ...              ...         ...           ...      ...  
293906  2024                5  194.792597    973.962984        1  
293907  2023                1  285.137301    285.137301        5  
293908  2024                3   60.701761    182.105285        2  
293909  2023                1  120.834784    120.834784        4  
293910  2024                7  340.319059   2382.233417        2  

[293911 rows x 11 columns]
"""