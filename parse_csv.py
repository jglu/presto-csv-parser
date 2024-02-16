from glob import glob
import csv
import os 
import re

os.chdir(os.path.dirname(os.path.abspath(__file__))) # cd to script dir
filenames = glob("./input/*.csv") 

year_pattern = '[2][0][0-2][0-9]' # outputs year in results.txt

with open('results.txt', 'w') as results_file:
    sum = 0
    for filename in filenames:
        year_sum = 0
        with open(filename, 'r') as csv_file:
            input_reader = csv.reader(csv_file)
            next(input_reader) # skip header line
            # loop through all lines
            for line in input_reader:
                try: 
                    amount = line[4] # get amount only
                    # amount is in pattern "$x.xx" or "-$x.xx"
                    #   if it starts with $, then it is given credit.
                    #   if it starts with -$, then it is cost.
                    if amount.startswith('$'):
                        price = float(amount[1:])
                        sum = round(sum - price, 2) # fix floating point issues
                        year_sum = round(year_sum - price, 2)
                    else:
                        price = float(amount[2:])
                        sum = round(sum + price, 2)
                        year_sum = round(year_sum + price, 2)
                except IndexError:
                    print("index error. skipping to next line.")
                    continue
        year = re.search(year_pattern, filename).group()
        output_line = "In " + year + ", I've spent $" + str(year_sum) + ".\n"
        results_file.write(output_line)
    output_line = "In total, I've spent $" + str(sum) + ".\n"
    results_file.write(output_line)
