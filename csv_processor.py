import csv

def get_average_score(filename):
    scores = []
    
    # TODO: 
    # 1. Open the file using 'with open'
    # 2. Initialize csv.reader
    # 3. Skip the header row using next()
    # 4. Loop through rows, convert the 'score' column to float, and append to scores
    # 5. Use try-except to handle the "invalid" data
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        
        for row in reader:
            pass # replace pass with code

    return pass # replace pass with code

if __name__ == "__main__":
    print(f"Average: {get_average_score('data.csv')}")
