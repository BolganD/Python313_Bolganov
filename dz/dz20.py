import re
numbers = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 499 456-45-78'
find_n = r'[+]?7\s?[(]?\d{3}?[)]?\s?\d{3}?\s?[-]?\d{2}?\s?[-]?\d{2}?'
print(re.findall(find_n, numbers))