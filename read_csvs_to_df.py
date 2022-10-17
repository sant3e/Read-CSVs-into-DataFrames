# Method 1, using glob:
import glob
import pandas as pd

# specify path to csv files
path = "C:/folder_location/"

# csv files in the path
files = glob.glob(path + "/*.csv")

# define an empty list to store content
data_frame = pd.DataFrame()
content = []

# checking all csv files in the specified path
for filename in files:
    df = pd.read_csv(filename, index_col=None, encoding="ISO-8859-1")
    content.append(df)
    
# converting content to dataframe
data_frame = pd.concat(content)
print(data_frame)


# Method 2, using os:
import pandas as pd
import os
path = "C:/folder_location/"
  
# specifying an empty list for content
df_list = []
for file in os.listdir(path):
      
    # reading content into data frame
    df = pd.read_csv(file)
    df_list.append(df)
  
final_content = df.append(df for df in df_list)
print(final_content)
