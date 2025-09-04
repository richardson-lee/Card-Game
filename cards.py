import random


def draw_cards(deck, num_cards):
    n = max(0, min(num_cards, len(deck)))      # clamp request to what’s left
    hand = [deck.pop() for _ in range(n)]      # draw n cards from the end
    return hand, deck


def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(s, r) for s in suits for r in ranks]  # 52 (suit, rank) tuples
    random.shuffle(deck)                           # in-place shuffle
    return deck


def show_card(card):
    # tuple unpacking: ('♣', 'A') -> suit='♣', rank='A'
    suit, rank = card
    top = "+-------+"
    line1 = f"|{rank:<2}     |"  # left-aligned rank, width 2 (A→"A ", 10→"10")
    line2 = "|       |"
    line3 = f"|   {suit}   |"
    line4 = "|       |"
    # right-aligned rank, width 2 (A→" A", 10→"10")
    line5 = f"|     {rank:>2}|"
    print("\n".join([top, line1, line2, line3, line4, line5, top]))


# --- program starts running here ---
deck = create_deck()

while deck:  # truthy while: runs while list is non-empty
    resp = input(
        f"{len(deck)} cards left. How many to draw? (Enter=1, q=quit): ").strip().lower()

    if resp in ("q", "quit", "0"):
        break

    try:
        num = 1 if resp == "" else int(resp)  # default to 1 on blank
    except ValueError:
        print("Not a number — drawing 1.")
        num = 1

    hand, deck = draw_cards(deck, num)

    for card in hand:
        show_card(card)

print("We are out of cards!" if not deck else f"{len(deck)} cards remain.")
