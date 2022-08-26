import re

pattern = r"(?P<day>(\d{2}))(?P<between>(.|/|-))(?P<month>[A-Z][a-z]{2})(?P=between)(?P<year>(\d{4}))"

dates = input()
valid_matches = [i.groupdict() for i in re.finditer(pattern, dates)]
print("\n".join(
    f"Day: {match['day']}, Month: {match['month']}, Year: {match['year']}" for match in
    valid_matches))
