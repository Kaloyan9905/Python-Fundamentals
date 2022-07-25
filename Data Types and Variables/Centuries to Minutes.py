input_line = int(input())
centuries = input_line * 100
years = int(centuries * 365.2422)
days = 24 * years
hours = days * 60
print(f'{input_line} centuries = {centuries} years = {years} days = {days} hours = {hours} minutes')