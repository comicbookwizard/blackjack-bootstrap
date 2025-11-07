import random
counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Possible card values in blackjack
random.shuffle(counts) # Randomizes order of array

def dealerTurn(d): # Dealer function, standing on 17
    """
    Simulates the dealer's turn in a game of blackjack.
    The dealer must hit until their count is at least 17.
    If the dealer's count exceeds 21, they bust and return 1000.
    Otherwise, the dealer's final count is returned.

    Args:
        d (int): The dealer's initial count.
    """
    while (d < 17):
        d += counts[random.randint(0, 12)] # Adds a random value from cards
    if (d > 21): # Bust condition
        return 1000
    else: # Return valid count
        return d
    
def hitTurn(p): # Player hit function
    """
    Simulates the player's hit action in a game of blackjack.
    The player receives an additional card, and their count is updated.
    If the player's count exceeds 21, they bust and return 1000.
    Otherwise, the player's updated count is returned.
    Args:
        p (int): The player's current count."""
    p += counts[random.randint(0, 12)] # Adds a random value from cards
    if (p > 21): # Bust condition
        return 1000
    else: # Return valid count
        return p
    
def recommendation(p, d):
    """
    Provides a recommendation for the player's next move in blackjack
    based on Monte Carlo simulations of hitting, doubling, or standing.
    The function simulates a large number of games to evaluate the outcomes
    of each action and returns the recommended action along with the
    corresponding values for hitting, doubling, and standing.

    Args:
        p (int): The player's current count.
        d (int): The dealer's visible card count.
    Returns:
        str: A recommendation string indicating the best action and
             the values for hitting, doubling, and standing.
    """
    hit = 0 # Initialize counters for each action
    double = 0
    stand = 0
    n = 1000000
    for i in range(n): # Monte Carlo simulation loop
        standTurn = p # Player's count if they stand
        hitAndDouble = hitTurn(p) # Player's count if they hit or double
        dealer = dealerTurn(d) # Dealer's final count
        if (hitAndDouble == 1000): # If player busts on hit/double
            hit -= 1 # Decrease hit and double counters
            double -= 2
        else: # If the player doesn't bust, compare with dealer's count
            if (dealer == 1000): # If dealer busts
                hit += 1 # Increase hit and double counters
                double += 2
            else: # Compare counts
                if (dealer > hitAndDouble): # If dealer wins
                    hit -= 1 # Decrease hit and double counters
                    double -= 2
                else: # If player wins
                    hit += 1 # Increase hit and double counters
                    double += 2
        if (dealer == 1000): # If dealer busts on stand
            stand += 1 # Increase stand counter
        else:
            if (dealer > standTurn): # If dealer wins on stand
                stand -= 1 # Decrease stand counter
            else: # If player wins on stand
                stand += 1 # Increase stand counter
                
    turns = {'Hit': hit, 'Double': double, 'Stand': stand} # Store results in a dictionary
    best_action = max(turns, key=turns.get) # Get action with highest value
    return f'Player Recommendation: {best_action}. Values of [hit, double, stand]: [{turns["Hit"]}, {turns["Double"]}, {turns["Stand"]}]' # Format return string

playerCount = int(input("What is the total count of the player? ")) # Takes user input
dealerCount = int(input("What is the dealer show card value? "))
print(recommendation(playerCount, dealerCount)) # Prints recommendation based on input
