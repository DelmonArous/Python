import pandas as pd
import numpy as np

# Directory to files
sourcepath = np.array(['C:/Users/delmo/PycharmProjects/pythonFiles_Olga/conc.xlsx'],
                      dtype = object)
destpath = np.array(['C:/Users/delmo/PycharmProjects/pythonFiles_Olga/conc_sort.xlsx'],
                    dtype = object)

for i in np.arange(0, len(sourcepath)):

    # Read Excel .xlsx file
    df = pd.read_excel(sourcepath[i], sheet_name = 'Sheet 1', header = 0)
    row, col = df.shape

    # Split first column into three separate columns 'Group', 'MouseID' and 'Day'
    df['Group'], df['Day'] = df['Group'].str.split(' ').str[0], df['Group'].str.split(' ').str[1]
    df['Day'] = df['Day'].str[1:].astype(int)
    df['Group'], df['MouseID'] = df['Group'].str.split('-').str[0].astype(int), df['Group'].str.split('-').str[1].astype(int)

    # Sort dataframe by column 'Day', 'Group' and 'MouseID'
    df = df.sort_values(by = ['Day', 'Group', 'MouseID'], ascending = [True, True, True])

    # Combine column 'Group', 'MouseID' and 'Day'
    df['LP'] = df['Group'].astype(str) + '-' + df['MouseID'].astype(str) + ' d' + df['Day'].astype(str)

    # Delete columns 'Group', 'MouseID' and 'Day'
    df = df.drop(columns = ['Group', 'MouseID', 'Day'])

    # Reorder columns of dataframe
    df = df.iloc[:, np.concatenate((np.array([-1]), np.arange(0, col-1, 1)))]

    # Write to Excel .xlsx file
    df.to_excel(destpath[i], index = False)
