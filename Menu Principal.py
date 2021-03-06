import csv
MY_FILE = "Data/Datos.csv"

def parse(raw_file,delimiter):
    """Analiza un archivo CSV y devuelve un objeto JSON-line"""

    #Open CSV file

    opened_file =  open(raw_file)

    #Read CSV file

    csv_data = csv.reader(opened_file, delimiter=delimiter)

    ###Build a data structure to return parsed_data

    #Setup an empty list

    parsed_data = []

    # Skip over the first line of the file for the headers

    fields = next(csv_data)

    # Iterate over each row of the csv file, zip together field -> value

    for row in csv_data:
        parsed_data.append(dict(zip(fields,row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data


def main():
    #Call our parse function and give it the needed parameters
    new_data = parse(MY_FILE,",")

    #Let's see what the data looks like!
    print(new_data)

main()

