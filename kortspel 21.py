import random


class Card:
    # Klassen representerar ett enskilt kort i kortleken.
    def __init__(self, number, suit):
        # Kortet har tre attribut: number (nummer), suit (färg) och value (värde).
        self.number = number
        self.suit = suit
        self.value = number

    def __str__(self):
        # Metoden __str__ används för att returnera en textrepresentation av kortet.
        return f"{self.number} of {self.suit}"


def create_deck():
    # Skapar en standardkortlek med 52 kort. Fyra färger i en lista och en lista som skapar en kortlek och blandar den innan den returneras.
    colours = ["Hearts", "Spades", "Clubs", "Diamonds"]
    deck = []
    for suit in colours:
        for number in range(1, 14):
            card = Card(number, suit)
            deck.append(card)  # Lägger till korten till vår deck
    random.shuffle(deck)  # Blandar leken innan vi returnerar
    return deck


def draw_cards(deck, num_cards, is_computer=False):
    # En funktion som drar ett antal kort från vår deck.
    # Vi sätter is_computer=False så att vi kan kontrollera att det är spelaren som drar kort.
    drawn_cards = random.sample(deck,
                                num_cards)  # Med random.sample drar vi num_cards slumpmässiga kort från kortleken.
    for card in drawn_cards:
        if card.number == 1:
            if not is_computer:
                ace_choice = input("What value would you like the Ace to have, 1/14: ")
                if ace_choice == "1":
                    card.value = 1
                elif ace_choice == "14":
                    card.value = 14
        deck.remove(
            card)  # Allt ovan gör så att användaren får en fråga om ess ska vara värt 1 eller 14 poäng, sedan tas korten bort från leken.
    return drawn_cards


def points_in_hand(hand):
    points = 0
    # Räknar poängen för given hand.
    # Summerar kortens värde baserat på value-attributen vid __init__; value blir samma som number.
    for card in hand:
        points += card.value
    return points


def get_card_name(card):
    # Sätter namn på alla värden i kortleken och returnerar deras namn som sträng.
    # Kort som ess och kung får speciella namn.
    if card.number == 1:
        return f"Ace of {card.suit}"
    elif card.number == 11:
        return f"Jack of {card.suit}"
    elif card.number == 12:
        return f"Queen of {card.suit}"
    elif card.number == 13:
        return f"King of {card.suit}"
    else:
        return f"{card.number} of {card.suit}"


def ask_draw_card(drawn_hand, deck):
    print("|  Cardgame-21  |".center(25))
    # Denna kod hanterar spelarens val att dra ett nytt kort.
    while True:
        print("Your hand is:")
        for card in drawn_hand:
            print("-", get_card_name(card))
        # Här visar vi spelarens nuvarande hand och drar automatiskt ett kort i början och visar det.
        ask_card = input("Would you like to draw another card, y/n : ")
        if ask_card.lower() == "y":
            drawn_cards = draw_cards(deck, 1)
            print(f"You drew {get_card_name(drawn_cards[0])}")
            print("-" * 25)
            for card in drawn_cards:
                drawn_hand.append(card)
            if points_in_hand(drawn_hand) > 21:
                print("You went over 21 points")
                return
        elif ask_card.lower() == "n":
            print("No card drawn")
            return
        else:
            print("Wrong input, no card drawn")


def main():
    number_wins = 0
    number_losses = 0
    # För att räkna statistik under spelets gång sätter vi två räknare.
    while True:
        deck = create_deck()  # En ny kortlek skapas med hjälp av vår funktion.
        drawn_hand = draw_cards(deck, 1)  # Spelaren drar ett kort, och vi sätter det i drawn_hand.
        ask_draw_card(drawn_hand,
                      deck)  # Funktionen kallas för att låta spelaren välja om de vill dra fler kort eller gå över 21 poäng.
        print("-" * 25)

        computer_hand = draw_cards(deck, 1, True)  # Datorn drar sitt kort och lägger det i sin hand.
        # När vi sätter is_computer=True kommer datorn automatiskt att sätta essets värde till 1 poäng, så att spelaren inte kan välja vad datorn ska ha för poäng.
        print(f"Computer drew {get_card_name(computer_hand[0])}")
        points = points_in_hand(drawn_hand)
        computer_points = points_in_hand(computer_hand)
        # Beräknar poängen för båda spelarna med points_in_hand-funktionen.

        while computer_points < 15:
            drawn_cards = draw_cards(deck, 1, True)
            computer_hand.append(drawn_cards[0])
            # Datorn drar kort tills dess att den har kommit till eller över 15 poäng.
            print(f"Computer drew {get_card_name(drawn_cards[0])}")
            computer_points = points_in_hand(computer_hand)

        print("-" * 25)
        print("Your points: ", points)
        print("Computer's points: ", computer_points)
        # Visar poängen för båda spelarna.

        if points > 21:
            if computer_points > points:
                print("You won!!")
                number_wins += 1
            else:
                print("The computer won, you lost...")
                number_losses += 1
        elif computer_points > 21:
            print("You won!!!")
            number_wins += 1
        elif points > computer_points:
            print("You won!!")
            number_wins += 1
        elif points <= computer_points:
            print("You lost...")
            number_losses += 1
        # Allt ovan är logik och räknare för när spelaren vinner eller förlorar.

        yes_no = input("Would you like to play again? y/n: ")
        if yes_no == "n":
            break

    # Ifall användaren vill avsluta spelet, bryts loopen och resultaten visas med number_wins och number_losses.
    print("-" * 25)
    print(f"You won {number_wins} times!")
    print(f"The computer won {number_losses} times!")


if __name__ == "__main__":
    main()
