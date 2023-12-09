''' set current main working directory ''' 
import os as __os
import sys as __sys

# current path
__CURRENT = __os.getenv('PATH_BASE')
if not __CURRENT:
    __os.environ['PATH_BASE'] = '/Users/ant/Documents' 
    __sys.path.append(__os.getenv('PATH_BASE'))


''' import modules '''
import csv
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from Data_science.libs import constants as c
from prefect import task, Flow, flow


''' start defining the flow '''

@flow
def my_function():
    print(c.id_client)
    
my_function()

# my_function.visualize()
# my_function.run()
    
# data= extract('./values.csv')
# tdata=transform(data)
# load(tdata,'./tvalues.csv')