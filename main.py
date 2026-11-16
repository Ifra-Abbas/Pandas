# 05-11-2026 Thursday
import pandas as pd

print(pd.__version__)

# Series: A pandas 1-dimensional labeled array that can hold any type of data
# Think of it like a single column in a spreadsheet.
data=[10,20,30,40,50,60,70,80,90,100]
series=pd.Series(data) # series is a constructor that takes a list as an argument and returns a Series object
print(series)

data=[10,20,30,40,50,60,70,80,90,100]
series=pd.Series(data,index=['a','b','c','d','e','f','g','h','i','j']) #index = lable
print(series)
print(series.loc['a']) # loc is used to access a specific element in the series by its label
print(series.iloc[3]) # iloc is used to access a specific element in the series by its integer position

# filter by value

print(series[series>50])

# lets use dictionary to create a series

calories={'day1':420,'day2':380,'day3':390,'day4':400,'day5':450}
series=pd.Series(calories)
print(series)
print(series.loc['day1'])
series.loc["day5"] +=400
print(series)

# Data Frames: A tabular data structure rows and columns (2-dimenstional)
# similar to the spreadsheet.

data={"Name":["Jimin","Jungkook","Taehyung","Jin","J-Hope","RM","SUGA"],
      "Age":[24,24,25,27,27,26,28],
      "City":["Seoul","Busan","Incheon","Daegu","Daejeon","Gwangju","Suwon"]}
dataframe=pd.DataFrame(data,index=
                       ["BTS Member 1","BTS Member 2","BTS Member 3","BTS Member 4",
                        "BTS Member 5","BTS Member 6","BTS Member 7"]) # Converting dictionary to DataFrame
print(dataframe)
# print the data of specific row using loc and iloc
print(dataframe.loc["BTS Member 1"])
print(dataframe.iloc[3])

# adding a new column to the DataFrame
dataframe["job"]=["Singer","Singer","Singer","Singer","Singer","Rapper","Rapper"]
# adding a new row to the DataFrame
new_row=pd.DataFrame({"Name":["Ifra"],"Age":[24],"City":["Gwangju"],"job":["Engineer"]},index=["BTS Member 8"])
dataframe=pd.concat([dataframe,new_row])


# 16-11-2026 Monday
# Importing (CSV+JSON)

# #CSV: Comma Separated Values
df=pd.read_csv("pokemon.csv")
print(df.to_string()) # to_string() is used to print the entire DataFrame without truncation

# JSON: JavaScript Object Notation
df=pd.read_json("data.json")
print(df)

# Selection

df=pd.read_csv("pokemon.csv")

# Selecting by column
print(df["Name"])
print(df["Type 1"].to_string()) 
print(df["Type 1"])
print(df[["Name","Type 1","Type 2"]])# passes the list of columns

# Selection by row
print(df.loc[0])
df=pd.read_csv("pokemon.csv",index_col="Name")
print(df)

print(df.loc["Pikachu"])
print(df.loc["Pikachu",["Attack","Defense"]])
print(df.loc["Pikachu":"Nidoran♀"])

print(df.iloc[0:22])
print(df.iloc[0:22:4])
print(df.iloc[0:22:4 , 0:3]) # first 3 columns
print(df.iloc[20:80:2,4:6])

Pokemon=input("Enter any name of the pokemon:")

try:
    print(df.loc[Pokemon])

except KeyError:
    print("Pokemon Not Found")
      

