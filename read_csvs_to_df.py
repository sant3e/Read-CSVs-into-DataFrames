import glob
import pandas as pd

# specify path to csv files
path = "C:/Users/tdiacon/Documents/glassdoor-scraper/src/output/"

# csv files in the path
files = glob.glob(path + "/*.csv")

# define an empty list to sore content
data_frame = pd.DataFrame()
content = []

# checking all csv files in the specified path
for filename in files:
    df = pd.read_csv(filename, index_col=None, encoding="ISO-8859-1")
    content.append(df)
    
# converting content to dataframe
data_frame = pd.concat(content)
