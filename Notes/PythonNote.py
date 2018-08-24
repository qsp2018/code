
# assign values to specific rows
df.loc[df.ID == 103, ['FirstName', 'LastName']] = 'Matt', 'Jones'

# locate rows with conditions
df[(df.a1 >= 1) & (df.a2.isin([2,3]))]
pd.isnull(df)

# Add an additional column from group by result
df['a5'] = df.groupby(['a1', 'a2', 'a3'])['a4'].transform('sum')

# cumsum for a groupby column
df['cum'] = df.groupby(['a1', 'a2'])['a3'].cumsum()

# ungroup a groupby summary to a dataframe 
df.groupby(['a1','a2'])['a3'].mean().reset_index()

# normalize a column 
df.groupby('indx').transform(lambda x: (x - x.mean()) / x.std())

# normlized to percentage
df.groupby(['a1','a2'])['a4'].transform(lambda x: x / x.sum())

# sort by column
df.sort(['A', 'B'], ascending=[1, 0]) # or sort_values

# plot line
import matplotlib.pyplot as plt
plt.plot(df.a, df.b, '--ro')
# plt.axis([0, 6, 0, 20])
plt.show()

# loop rows in data frame
for index, row in df.iterrows():
    print index, row.a1

# convert x to integer
int(x)

# list/array 
my_list = []
my_list.append(12)
# add another list
my_list.extend([1,2,3,4])
my_list.remove(2)

# polynomial regression
import matplotlib.pyplot as plt
z = np.polyfit(df.a1, df.a2, 7)
f7 = np.poly1d(z)
plt.plot(df.a1, df.a2, 'o',
        df.a1, f7(df.a1), '--')
plt.legend(['data', 'degree 7'], loc='best')
plt.show()