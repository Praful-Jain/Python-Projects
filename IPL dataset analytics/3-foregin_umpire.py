import csv
import matplotlib.pyplot as plt

def read_file(csv_file):

    # Open the CSV file for reading.
    with open(csv_file) as file:
        # Create a CSV reader object.       
        csv_reader = csv.DictReader(file)    
        umpire_reader = list(csv_reader)  
    return umpire_reader

def execute(umpire_reader):
    # Dictionary to store foreign umpires history
    umpire_origin = {}
    
    for row in umpire_reader :
        if row[' country'] != ' India' :
            umpire_origin[row[' country']] = umpire_origin.get(row[' country'] , 0) + 1
            
    for i in umpire_origin:
        print(i," : ",umpire_origin[i])
    return umpire_origin

def plot(umpire_origin):
    # Plotting the bar graph
    plt.bar(umpire_origin.keys(),umpire_origin.values())
    plt.xlabel('Country')
    plt.xticks(rotation=90)     #To print the labels vertically on the x-axis in Matplotlib,
    plt.ylabel('Count')
    plt.title('Empires origin')
    plt.show()
    
    
umpire_reader = read_file('IPL dataset analytics/umpires.csv')
umpire_origin = execute(umpire_reader)
plot(umpire_origin)
