regex_pattern = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"

import re
print(str(bool(re.match(regex_pattern, input()))))