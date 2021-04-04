import numpy
import pandas as pd

def p2(file_name):
    df = pd.read_csv(file_name, header=None)
    #print(df.head(5))  # print first 5 rows of the dataframe

    mean = df.mean()
    var = df.var()

    mean_val = numpy.round(mean.get(0), 2)
    var_val = numpy.round(var.get(0), 2)

    print("( " + str(mean_val) + ", " + str(var_val) + ")")






file_name = "/home/bcfay/PycharmProjects/FayBrianC/data/hw1_p2_data.csv"

p2(file_name)