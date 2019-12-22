import random


class Time(object):
    """
    represents the time of the day. Attributes: hour, ,minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes*60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

    # 18.1
    def __cmp__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return cmp(t1, t2)


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def cmp(x, y):
    """
    Replacement for built-in function cmp that was removed in Python 3

    Compare the two objects x and y and return an integer according to
    the outcome. The return value  is negative if x < y, zero if x == y
    and strictly positive if x > y.
    """

    return (x > y) - (x < y)


class Card(object):
    """
    represents a standard playing card
    """
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1

        # suits are the same check rank
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1

        return 0


queen_of_diamonds = Card(1, 12)
print(queen_of_diamonds)
card1 = Card(2, 11)
print(card1)
print(type(Card))


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_cards(self):
        return self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def dead_hands(self, number_of_hands, number_of_cards_per_hand):
        list_of_hands = []
        it = number_of_hands
        itt = number_of_cards_per_hand
        for i in range(number_of_hands):
            h = Hand('new hand')
            for j in range(number_of_cards_per_hand):
                h.add_card(self.pop_card())
            list_of_hands.append(h)
        return list_of_hands


deck = Deck()
# print(deck)


class Hand(Deck):
    """represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label


hand = Hand('new hand')
print(hand.cards)
print(hand.label)
card = deck.pop_card()
hand.add_card(card)
# print(hand)
p = deck.dead_hands(4, 5)



