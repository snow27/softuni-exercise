import re

regex = r'(=|/)([A-Z][a-zA-Z]{2,})\1'
line = input()
matches = re.finditer(regex, line)
valid_destinations = []
lengths_sum = 0
for match in matches:
    valid_destinations.append(match.group(2))
    lengths_sum += len(match.group(2))
string_valid = ', '.join(valid_destinations)

print(f'Destinations: {string_valid}')
print(f"Travel Points: {lengths_sum}")

