deck = input().split()
count = int(input())

half = int(len(deck)) // 2
left_sum = []
right_sum = []

for i in range(count):
    current_deck = []
    left_sum = deck[0:half]
    right_sum = deck[half::]
    for j in range(len(left_sum)):
        current_deck.append(left_sum[j])
        current_deck.append(right_sum[j])
    deck = current_deck
print(deck)


