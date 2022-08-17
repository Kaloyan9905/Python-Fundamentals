class Party:
    def __init__(self):
        self.names_list = []


party = Party()
while True:
    name = input()
    if name == 'End':
        print(f"Going: {', '.join(party.names_list)}")
        print(f"Total: {len(party.names_list)}")
        break
    else:
        party.names_list.append(name)
