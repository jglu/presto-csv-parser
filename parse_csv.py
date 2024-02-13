from glob import glob
import csv
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__))) # cd to script dir
filenames = glob("./input/*.csv") # returns a list

sum = 0

with open('results.txt', 'w') as results_file:
    for filename in filenames:
        year_sum = 0
        with open(filename, 'r') as csv_file:
            input_reader = csv.reader(csv_file)

            next(input_reader) # skip header line
            # loop through all lines
            for line in input_reader:
                try: 
                    amount = line[4] # get amount only

                    # amount is in pattern "-$x.xx" or "$x.xx"
                    # if it starts with $, then add it. if $, then minus it.
                    if amount.startswith('$'):
                        price = float(amount[1:])
                        sum = round(sum - price, 2) # fix floating point issues
                        year_sum = round(year_sum - price, 2)
                    else:
                        price = float(amount[2:])
                        sum = round(sum + price, 2)
                        year_sum = round(year_sum + price, 2)
                    print(year_sum)
                except IndexError:
                    print("index error. continuing to next file")
                    continue
        output_line = "In this year, I've spent $" + str(year_sum) + ".\n"
        results_file.write(output_line)
    output_line = "In total, I've spent $" + str(sum) + ".\n"
    results_file.write(output_line)