import glob
import pandas as pd

path = "C:/Users/tdiacon/Documents/glassdoor-scraper/src/output/"

files = glob.glob(path + "/*.csv")
data_frame = pd.DataFrame()
content = []

for filename in files:
    df = pd.read_csv(filename, index_col=None, encoding="ISO-8859-1")
    content.append(df)

data_frame = pd.concat(content)
