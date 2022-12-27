import random

class User:
    """
    Users 
    - May click on an add at random.
    
    Private attributes:
    __probability --  Stores the users probability of clicking an ad.

    Methods:
    show_ad() -- Returns true if the user clicked the ad.
    """
    def __init__(self):
        self.__probability = random.uniform(0, 1)

    def show_ad(self):
        """
        Method returns True if it clicks on the add, False otherwise
        (probability that it clicks on the add is self.__probability)
        """
        return random.uniform(0, 1) <= self.__probability


class Auction:
    """
    The Auction is a game, involving a set of Bidders on one side, 
    and a set of Users on the other. Each round represents an event 
    in which a User navigates to a website with a space for an ad. 
    When this happens, the Bidder s will place bids, and the winner 
    gets to show their ad to the User. 
    
    The User may click on the ad, or not click, and the 
    winning Bidder gets to observe the User's behavior. 
    This is a second price sealed-bid Auction.
    """
    def __init__(self, users, bidders):
        """            
        Key arguments:
        users --  A list of all User objects.
        bidders -- A list of all Bidder objects. 
        
        Private attribute:
        __balances -- A dictionary of bidder balances.
        """
        self.users = users
        self.bidders = bidders
        self.balances = {}
        for bidder in bidders:
            self.balances[bidder] = 0

    def execute_round(self):
        """
        Execute all steps in a single round of an Auction.
            - choose a user at random (from our users list)
            - collect bids from all the bidders in our bidders list
            - find the highest bidder (deal with ties if necessary)
            - find the winning price (second highest bid, or the highest 
            if more than 1 bidder bid the highest price)
            - see if user clicks on add or not
            - notify all bidders about this round's results
            - update the balance of the bidder
        """
        # List used for bids to find the highest bidder
        bids = []
        
        # User chosen at random from the list of users provided
        current_userid = random.randint(0, len(self.users) - 1)
        current_user = self.users[current_userid]
        
        # Append a bid for each bidder from the list for current user
        for bidder in self.bidders:
            bids.append(bidder.bid(current_userid))
            
        # Find duplicate max values 
        highest_bid = max(bids)
        # Finds the max bid in the list and returns the index(es)
        indices = [i for i, x in enumerate(bids) if x == highest_bid]     
        # If max value is a tie, pick the winner at random
        winning_bidder_index = indices[0]
        if len(indices) > 1:
            winning_bidder_index = random.choice(indices)
            
        # Store the 2nd price and whether the user clicked the ad
        winning_price = 0
        if len(bids) > 1:
            winning_price = sorted(bids)[-2]
        else:
            winning_price = bids[0]
        clicked_ad = current_user.show_ad()
        
        # Notify winners and losing bidder from the list 
        for i in range(len(self.bidders)):
            if i == winning_bidder_index:
                winning_bidder = self.bidders[i]
                winning_bidder.notify(True, winning_price, clicked_ad)
                self.balances[winning_bidder] -= winning_price
                if clicked_ad:
                    self.balances[winning_bidder] += 1
            else:
                bidder = self.bidders[i]
                bidder.notify(False, winning_price, None)
