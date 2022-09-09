symbols = ['@', '#', '$', '^']


def valid_ticket_by_chars(ticket):
    if len(ticket) == 20:
        return True
    return False


def valid_ticket_by_contains(ticket):
    for symbol in symbols:
        if symbol in ticket:
            return True
    return False


def repetition_of_symbols(ticket):
    left = ticket[:10]
    right = ticket[10::]
    for symbol in symbols:
        if symbol * 6 in left and symbol * 6 in right:
            right_count = right.count(symbol)
            left_count = left.count(symbol)
            res = min(right_count, left_count)
            print(f"ticket \"{ticket}\" - {res}{symbol}")
            return True
    else:
        print(f"ticket \"{ticket}\" - no match")
        return False


def jackpot(ticket):
    for symbol in symbols:
        if ticket.count(symbol) == 20:
            print(f"ticket \"{ticket}\" - 10{symbol} Jackpot!")
            return True
    return False


data = [i.strip() for i in input().split(", ")]

for word in data:
    if not valid_ticket_by_chars(word):
        print("invalid ticket")
        continue
    if jackpot(word):
        continue
    if repetition_of_symbols(word):
        continue
    if valid_ticket_by_contains(word):
        continue
