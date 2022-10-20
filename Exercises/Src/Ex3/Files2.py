import pandas
import glob

files = glob.glob("*.csv")

result = pandas.DataFrame()

for file in files:
    data = pandas.read_csv(file)
    result = pandas.concat([result, data])

print(result)
