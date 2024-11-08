import os
import re

# Directory containing the data files
directory = 'raw/DepEPFedRev' # change the directory where you run it from no need to run it anymore

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Extract year from filename
        year = filename.split('.')[0]  # Assumes filename format is "YYYY.txt"
        
        # Read data from each file
        with open(os.path.join(directory, filename), 'r') as file:
            data = file.read()
        
        # Initialize result list with dynamic header based on year
        result = [f"Department of Environmental Protection {year} Revenues, {int(year) - 2} Actual, {int(year) - 1} Estimated, {year} Estimated"]

        # Process each line
        for line in data.splitlines():
            # Use regex to capture the name and the three numbers (or dashes for missing values)
            match = re.match(r'(.+?)\s+([\d,]+|------)\s+([\d,]+|------)\s+([\d,]+|------)', line)
            
            if match:
                # Extract values
                name = match.group(1).strip()
                values = [match.group(i).replace(',', '') if match.group(i) != '------' else '' for i in range(2, 5)]
                
                # Join name and values with commas and add to result
                formatted_line = f"{name}, {values[0]}, {values[1]}, {values[2]}"
                result.append(formatted_line)

        # Remove all periods in the result data
        result = [re.sub(r'\.', '', line) for line in result]

        # Write the result to an output file with the year in the filename
        output_filename = f"data/DepEPFedRev/revenues_{year}.csv"
        with open(output_filename, 'w') as file:
            file.write('\n'.join(result))

        print(f"Data from {filename} reformatted and saved to {output_filename}")
