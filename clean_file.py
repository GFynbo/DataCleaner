#
# Tatiana Diaz-Gallegos
# todg@bu.edu
# © 2018
# Senior Design
#

import pandas as pd
import os
import re

def main():
    ''' this is the main function to take a csv and strip it of the necessary info '''

    # files must be in working directory
    files = []
    for x in os.walk(os.getcwd()):
        for i in os.listdir(x[0]):
            if os.path.isfile(os.path.join(x[0], i)) and 'Ref' in i:
                files.append(i)

                filename = i.rstrip('.csv')

                # grab and clean the files
                full_filename = filename + ".csv"
                df = pd.read_csv(x[0] + "/" + full_filename)
                keep_cols = ["Date/Time", "Electricity:Facility [kW](Hourly)", "Fans:Electricity [kW](Hourly)", "Cooling:Electricity [kW](Hourly)",
                             "Heating:Electricity [kW](Hourly)", "InteriorLights:Electricity [kW](Hourly)", "InteriorEquipment:Electricity [kW](Hourly)"]
                new_df = df[keep_cols].copy()

                # clean up the date/time field
                new_df['Date/Time'] = new_df['Date/Time'].str.replace(' ', '')
                new_df['Date/Time'] = new_df['Date/Time'].str.replace('/', '')
                new_df['Date/Time'] = new_df['Date/Time'].str.replace(':', '')

                # clean up file name and base it on current directory
                filename = filename.replace('RefBldg', '')
                filename = filename.replace('New', '')
                filename = re.sub('4_.*?_U', '4_U', filename)
                path = x[0].split('/')
                path = path[-1]
                filename = filename + "_cleaned.csv"
                filename = re.sub('U.*?.csv', path + '.csv', filename)
                new_df.to_csv(filename, index=False)

    print("Cleaned files: " + str(files))

if __name__ == '__main__':
    # run the main function
    main()