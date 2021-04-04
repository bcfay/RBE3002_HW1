import pandas as pd
cleaned = []

with open("RBE3002_D21_Homework_1 - NMEA0183_Data.txt", "r") as file:
    for line in file:
        #print (line)
        if line.__contains__("IIGGA"):
            cleaned.append(line)


print(cleaned)

df = pd.DataFrame(cleaned)

# saving the dataframe
df.to_csv('cleaned.csv')