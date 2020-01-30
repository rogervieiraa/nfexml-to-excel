import csv

# content need to be an array
def write_csv(content):
    with open('nfe.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        for line in content:
             writer.writerow(line)

    return True