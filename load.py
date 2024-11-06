import re

# Read data from input.txt
with open('raw/og.txt', 'r') as file:
    data = file.read()

# Initialize result list to store formatted rows
result = ["Department of Environmental Protection 2021 Revenues, 2019 Actual, 2020 Estimated, 2021 Estimated"]

# Process each line
for line in data.splitlines():
    # Use regex to capture the name and the three numbers (or dashes for missing values)
    match = re.match(r'(.+?)\s+([\d,]+|------)\s+([\d,]+|------)\s+([\d,]+|------)', line)
    
    if match:
        # Extract values
        name = match.group(1).strip()
        values = [match.group(i).replace(',', '') if match.group(i) != '------' else '' for i in range(2, 5)]
        
        # Join name and values with commas and add to result
        formatted_line = f"{name.strip()}, {values[0]}, {values[1]}, {values[2]}"
        result.append(formatted_line)

# remove all the periods in the result data
result = [re.sub(r'\.', '', line) for line in result]

# Write the result to output.txt
with open('output.txt', 'w') as file:
    file.write('\n'.join(result))

print("Data reformatted and saved to output.txt")
