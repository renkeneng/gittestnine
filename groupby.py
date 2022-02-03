# print('hello word')
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'data1' : ['a', 'b', 'c', 'd', 'a'],
# 'data2' : ['one', 'one', 'one', 'two', 'one'],
# 'num1' : [1,2,3,4,5],
# 'num2' : [6,7,8,9,10]})

# df
# print(df)
# grouped = df['num1'].groupby(df['data1'])
# grouped
# # # print(grouped)
# a=grouped.mean()
# # print(a)
# b=grouped.sum()
# # print(b)

# group2 = df['num2'].groupby([df['data1'], df['data2']])
# mean_group2 = group2.mean()
# # print(mean_group2)

# city = np.array(['beijing', 'shenzhen', 'shenzhen', 'beijing', 'beijing'])
# years = np.array([2019, 2020, 2019, 2020, 2020])
# a=df['num1'].groupby([city, years]).mean()
# print(a)

# for num,data in df.groupby('data1'):
#     print(num)
#     print(data)

# for (d1, d2), num in df.groupby(['data1', 'data2']):
#     print(d1, d2)
#     print(num)

# a=dict(list(df.groupby(['data1', 'data2'])))
# print(a['a', 'one'])

# grouped = df.groupby(df.dtypes, axis=1)
# a=list(grouped)[0]
# print(a)

# import pandas as pd
# import numpy as np
# people = pd.DataFrame(np.random.randn(5, 5),
# columns = ['a', 'b', 'c', 'd', 'e'],
# index = ['1', '2', '3', '4', '5'])
# people.iloc[2:4, 2:5] = np.nan
# a = people
# print(a)

# color = {'a':'red', 'b':'red', 'c':'blue',
# 'd':'blue', 'e':'red', 'f':'prange'}
# df_series = pd.Series(color)
# people.groupby(df_series, axis=1).count()
# df_col = people.groupby(color, axis=1).count()
# print(df_col)
# print(df_col.mean())
# print(df_col.sum())

import pandas as pd
import numpy as np
# cities = pd.DataFrame(np.random.randn(5, 5),
# columns = ['a', 'b', 'c', 'd', 'e'],
# index = ['shenzhen', 'guangzhou', 'beijing', 'nanjing', 'haerbin'])
# cities.iloc[2:4, 2:4] = np.nan
# print(cities)
# df_len = [len(x) for x in cities.index]  #求各个城市的字母长度
# a=cities.groupby(df_len).count()  #分组后求一下数量
# b = cities.groupby(len).count()
# # print(a)
# # print(b)
# key_list = ['one', 'one', 'one', 'two', 'two']
# a=cities.groupby([len, key_list]).sum()
# print(a)

columns = pd.MultiIndex.from_arrays([['Asian', 'Asian', 'Asian', 'America', 'America'],
['China', 'Japan', 'Singapore', 'United States', 'Canada']],
names=['continent', 'country'] )
hier_df = pd.DataFrame(np.random.randn(4,5), columns=columns)
print(hier_df)

names = ['continent', 'country']
group_hi = hier_df.groupby(level="continent", axis=1)
print(group_hi.mean())

group_hi = hier_df.groupby(level="country", axis=1)
print(group_hi.mean())

#git is a distributed version control syestem
#git is free software
#git has a mutable index called stage.
#git tracks changes.
#Creating a new branch is quick.
#Creating a new branch is queck AND simple.
#
