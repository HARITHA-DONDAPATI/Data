# Data.py
import pandas as pd
data = {
    'Name': ['Mike', 'Karen', 'Roby', 'James'],
    'Dept': ['IT', 'HR', 'IT', 'CEO'],
    'Salary': [55000, 35000, 95000, 121000]
}
df = pd.DataFrame(data)
print(df)
output:
    Name Dept  Salary
0   Mike   IT   55000
1  Karen   HR   35000
2   Roby   IT   95000
3  James  CEO  121000
