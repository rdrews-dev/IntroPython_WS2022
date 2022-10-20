import pandas

files = ["file1.csv", "file2.csv", "more_data.csv", "old_data.csv", "unknown.csv"]

result = pandas.DataFrame()

for file in files:
    data = pandas.read_csv(file)
    result = pandas.concat([result, data])

print(result)    
