import random

val_trans = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

suit_trans = {
    1: "Hearts",
    2: "Diamonds",
    3: "Clubs",
    4: "Spades",
    "Hearts": 1,
    "Diamonds": 2,
    "Clubs": 3,
    "Spades": 4
}

def draw_card():
    return (random.randint(1,13),random.randint(1,4))

def display_cards(cards):
    print("Your cards: " + str([(val_trans[card[0]], suit_trans[card[1]]) for card in cards]))

def calc_score(cards):
    score = 0
    for card in cards:
        if card[0] == 1:
            score += 11
        elif card[0] >= 10:
            score += 10
        else:
            score += card[0]
    for card in cards:
        if score >= 22 and card[0] == 1:
            score -= 10
    return score

def display_score(score):
    print("Your score: " + str(score))

def game():
    cards = [draw_card() for i in range(2)]
    display_cards(cards)
    score = calc_score(cards)
    display_score(score)
    if score == 21:
        print("Blackjack!")
        return score
    next = input("Hit or Stay? (h/s): ")
    while next != 's':
        if next == 'h':
            cards.append(draw_card())
            display_cards(cards)
            score = calc_score(cards)
            display_score(score)
            if score > 22:
                break
        else:
            print("Invalid input!")
        next = input("Hit or Stay? (h/s): ")
    if score > 22:
        print("Bust!")
    return score

def main():
    score = game()
    print("Final score: " + str(score))

if __name__ == "__main__":
    main()