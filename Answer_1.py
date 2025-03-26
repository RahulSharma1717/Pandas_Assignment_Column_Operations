# Create a new data frame customer id, name, email, phone and address.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
new_df = df[['Customer_ID', 'Name', 'Email', 'Phone', 'Address']]
print(new_df)


"""Output:
        Customer_ID                 Name                     Email  \
0             37249  Michelle Harrington         Ebony39@gmail.com   
1             69749          Kelsey Hill          Mark36@gmail.com   
2             30192         Scott Jensen         Shane85@gmail.com   
3             62101        Joseph Miller          Mary34@gmail.com   
4             27901        Debra Coleman       Charles30@gmail.com   
...             ...                  ...                       ...   
293906        12104         Meagan Ellis      Courtney60@gmail.com   
293907        69772          Mathew Beck      Jennifer71@gmail.com   
293908        28449           Daniel Lee  Christopher100@gmail.com   
293909        45477       Patrick Wilson       Rebecca65@gmail.com   
293910        53626       Dustin Merritt       William14@gmail.com   

             Phone                       Address  
0       1414786801             3959 Amanda Burgs  
1       6852899987            82072 Dawn Centers  
2       8362160449             4133 Young Canyon  
3       2776751724   8148 Thomas Creek Suite 100  
4       9098267635     5813 Lori Ports Suite 269  
...            ...                           ...  
293906  7466353743        389 Todd Path Apt. 159  
293907  5754304957             52809 Mark Forges  
293908  9382530370  407 Aaron Crossing Suite 495  
293909  9373222023               3204 Baird Port  
293910  9518926645           143 Amanda Crescent  

[293911 rows x 5 columns]
"""
