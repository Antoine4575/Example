import csv
from prefect import task, Flow, flow

@task()
def extract(path):
    with open(path,'r') as f : 
        test = f.readline().strip()
    data = [int(i) for i in test.split(',')]
    return data

@task()
def transform(data): 
    tdata = [i+1 for i in data]
    return tdata

@task()
def load(data, path):
    with open(path, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
    pass


@flow
def my_function():
    data= extract('./values.csv')
    tdata=transform(data)
    load(tdata,'./tvalues.csv')

my_function()
# my_function.visualize()
# my_function.run()

    
# data= extract('./values.csv')
# tdata=transform(data)
# load(tdata,'./tvalues.csv')