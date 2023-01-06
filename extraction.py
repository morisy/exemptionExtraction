import csv
from eyecite import clean_text, get_citations

# Path to the input CSV file
input_file = 'input.csv'

# Path to the output CSV file
output_file = 'output.csv'

# Read the input CSV file
with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create a CSV writer for the output file
    with open(output_file, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['citation1', 'citation2', 'citation3', 'citation4', 'citation5', 'citation6', 'citation7', 'citation8'])
        writer.writeheader()

        # Iterate over the rows in the input CSV
        for row in reader:
            # Extract the legal citations in the rejection text
#            c = clean_text(row['rejection_text'], ['inline_whitespace', 'html'])
            citations = get_citations(row['rejection_text'])

            # Add the citations to the row as separate columns
            row['citation1'] = citations[0] if len(citations) > 0 else ''
            row['citation2'] = citations[1] if len(citations) > 1 else ''
            row['citation3'] = citations[2] if len(citations) > 2 else ''
            row['citation4'] = citations[3] if len(citations) > 3 else ''
            row['citation5'] = citations[4] if len(citations) > 4 else ''
            row['citation6'] = citations[5] if len(citations) > 5 else ''
            row['citation7'] = citations[6] if len(citations) > 6 else ''
            row['citation8'] = citations[7] if len(citations) > 7 else ''

            # Write the row to the output CSV file
            writer.writerow(row)