import pandas
data = pandas.read_csv('names.txt')

columns = ['Last', 'First', 'Salary']

data.columns = columns

print(data)
