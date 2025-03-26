# Make America as the country of all the customers in the above dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
df['Country'] = 'America'
print(df)


"""Output:
        Transaction_ID  Customer_ID                 Name  \
0              8691788        37249  Michelle Harrington   
1              2174773        69749          Kelsey Hill   
2              6679610        30192         Scott Jensen   
3              7232460        62101        Joseph Miller   
4              4983775        27901        Debra Coleman   
...                ...          ...                  ...   
293906         4246475        12104         Meagan Ellis   
293907         1197603        69772          Mathew Beck   
293908         7743242        28449           Daniel Lee   
293909         9301950        45477       Patrick Wilson   
293910         2882826        53626       Dustin Merritt   

                           Email       Phone                       Address  \
0              Ebony39@gmail.com  1414786801             3959 Amanda Burgs   
1               Mark36@gmail.com  6852899987            82072 Dawn Centers   
2              Shane85@gmail.com  8362160449             4133 Young Canyon   
3               Mary34@gmail.com  2776751724   8148 Thomas Creek Suite 100   
4            Charles30@gmail.com  9098267635     5813 Lori Ports Suite 269   
...                          ...         ...                           ...   
293906      Courtney60@gmail.com  7466353743        389 Todd Path Apt. 159   
293907      Jennifer71@gmail.com  5754304957             52809 Mark Forges   
293908  Christopher100@gmail.com  9382530370  407 Aaron Crossing Suite 495   
293909       Rebecca65@gmail.com  9373222023               3204 Baird Port   
293910       William14@gmail.com  9518926645           143 Amanda Crescent   

              City            State  Zipcode  Country  Age  Gender  Income  \
0         Dortmund           Berlin    77985  America   21    Male     Low   
1       Nottingham          England    99071  America   19  Female     Low   
2          Geelong  New South Wales    75929  America   48    Male     Low   
3         Edmonton          Ontario    88420  America   56    Male    High   
4          Bristol          England    48704  America   22    Male     Low   
...            ...              ...      ...      ...  ...     ...     ...   
293906  Townsville  New South Wales     4567  America   31    Male  Medium   
293907     Hanover           Berlin    16852  America   35  Female     Low   
293908    Brighton          England    88038  America   41    Male     Low   
293909     Halifax          Ontario    67608  America   41    Male  Medium   
293910      Tucson    West Virginia    25242  America   28  Female     Low   

       Customer_Segment        Date  Year      Month      Time  \
0               Regular   9/18/2023  2023  September  22:03:55   
1               Premium  12/31/2023  2023   December  08:42:04   
2               Regular   4/26/2023  2023      April  04:06:29   
3               Premium  05-08-2023  2023        May  14:55:17   
4               Premium  01-10-2024  2024    January  16:54:07   
...                 ...         ...   ...        ...       ...   
293906          Regular   1/20/2024  2024    January  23:40:29   
293907              New  12/28/2023  2023   December  02:55:45   
293908          Premium   2/27/2024  2024   February  02:43:49   
293909              New  09-03-2023  2023  September  11:20:31   
293910          Premium  01-08-2024  2024    January  11:44:36   

        Total_Purchases      Amount  Total_Amount Product_Category  \
0                     3  108.028757    324.086270         Clothing   
1                     2  403.353907    806.707815      Electronics   
2                     3  354.477600   1063.432799            Books   
3                     7  352.407717   2466.854021       Home Decor   
4                     2  124.276524    248.553049          Grocery   
...                 ...         ...           ...              ...   
293906                5  194.792597    973.962984            Books   
293907                1  285.137301    285.137301      Electronics   
293908                3   60.701761    182.105285         Clothing   
293909                1  120.834784    120.834784       Home Decor   
293910                7  340.319059   2382.233417       Home Decor   

        Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
0                Nike       Shorts  Excellent        Same-Day     Debit Card   
1             Samsung       Tablet  Excellent        Standard    Credit Card   
2       Penguin Books   Children's    Average        Same-Day    Credit Card   
3          Home Depot        Tools  Excellent        Standard         PayPal   
4              Nestle    Chocolate        Bad        Standard           Cash   
...               ...          ...        ...             ...            ...   
293906  Penguin Books      Fiction        Bad        Same-Day           Cash   
293907          Apple       Laptop  Excellent        Same-Day           Cash   
293908         Adidas       Jacket    Average         Express           Cash   
293909           IKEA    Furniture       Good        Standard           Cash   
293910     Home Depot  Decorations    Average        Same-Day           Cash   

       Order_Status  Ratings            products  
0           Shipped        5      Cycling shorts  
1        Processing        4          Lenovo Tab  
2        Processing        2    Sports equipment  
3        Processing        4       Utility knife  
4           Shipped        1   Chocolate cookies  
...             ...      ...                 ...  
293906   Processing        1  Historical fiction  
293907   Processing        5             LG Gram  
293908      Shipped        2               Parka  
293909      Shipped        4            TV stand  
293910      Shipped        2              Clocks  

[293911 rows x 30 columns]
"""