import csv
import matplotlib.pyplot as plt

def read_file(csv_file):
    # Open the CSV file for reading.
    with open(csv_file, encoding="latin-1") as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        data = list(csv_reader)  
    return data

def execute(data):
    lessthan_1L=0
    oneLakh_to_tenLakh =0
    tenLakh_to_oneCr=0
    oneCr_to_tenCr=0
    morethan_tenCr=0
    
    for row in data :
        capital = int(float(row['AUTHORIZED_CAP']))
        
        if  capital <= 100000:
            lessthan_1L += 1

        elif 100000 < capital <= 1000000:
            oneLakh_to_tenLakh += 1

        elif 1000000 < capital <= 10000000:
            tenLakh_to_oneCr += 1

        elif 10000000 < capital <= 100000000:
            oneCr_to_tenCr += 1

        else:  # capital > 100000000
            morethan_tenCr += 1    
        
    count=[lessthan_1L,oneLakh_to_tenLakh,tenLakh_to_oneCr,oneCr_to_tenCr,morethan_tenCr]
    print(count)
    return count


def plot(count):
    range_perbin=['<=1L','1L to 10L','10L to 1Cr','1Cr to 10Cr','>10Cr']

    # Plot histogram
    plt.hist(range_perbin,bins=5,weights=count,ec='red')
    plt.xlabel('Capital_Range')
    plt.ylabel('Count')
    plt.title('Histogram of Authorized Cap')
    plt.show()

data = read_file('Company Master - Maharashtra/Maharashtra.csv')
count = execute(data)
plot(count)
