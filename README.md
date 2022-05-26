# Read-CSVs-into-DataFrames
Multiple CSV into a target folder; read them and store them in a concatenated DataFrame

-----------
## Usage

Iterate through n number of CSV files contained within a directory (folder/ path) consisting of different types of files, and work with the contents of these files.

### Method 1: Using Glob module
* set path of source directory into a variable (remember to change from \ to  /): path = "C:/path_to_folder/"
* in order to locate all CSV files (whose names may be unknown), the glob module is invoked and its glob method is called. This will return all CSV files' list located within the path: glob.glob(path, '*.csv'
* perform an iteration over these files using a for-loop, reading content into a dataframe using pandas' read_csv() method: read_csv(file_contents)

### Method 2: Using OS module
* set path of source directory into a variable (remember to change from \ to  /): path = "C:/path_to_folder/"
* locate all files (whose names may be unknown), the os module is invoked and its listdir() method is called. This will return all files' list located within the path: os.listdir(path)
* perform an iteration over these files using a for-loop, reading content into a dataframe using pandas' read_csv() method: read_csv(file_contents)

