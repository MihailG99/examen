import pandas as pd
import numpy as np
import sqlite3


with sqlite3.connect('db.sqlite3') as conn:
    df = pd.read_sql('select * from users_users', conn)


# print(df)


df['full_name']= df['first_name'] + ' ' + df['last_name']
df.to_csv('users.csv')
print(df)
print(df['number_of_login'].mean())
print(df['number_of_login'].std())