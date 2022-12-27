import random 

class Bidder:
    """
    Bidder
    - Will place a bid and keep a record of strategies used.
    
    Key attributes:
    num_users -- Int of the number of user objects in the game.
    num_rounds -- Int of bidding rounds to be played.
    
    Private attributes:
    __balance -- The balance updated each time the bidder wins a round.
    """
    def __init__(self, num_users, num_rounds):
        self.num_users = int(num_users)
        self.num_rounds = int(num_rounds)
        self.__balance = 0

    def bid(self, user_id):
        """Returns non negative amount of money each time a bid takes place"""
        return random.randint(self.__balance, self.__balance + 100)

    def notify(self, auction_winner, price, clicked = None):
        """
        Notifies the bidder winning bidder of what happened in the round.
        - If the auction_winner:
            - Pay the price (update our balance?)
            - If the user clicked: 
                - Increase the balance by a dollar
                
        Key arugments: 
        auction_winner -- Returns True when the bidder won a round. 
        price -- The price paid for the winning bid, subtracted from balance.
        clicked -- Whether the user clicked on bidders advertisement.
        """
        if auction_winner:
            self.__balance -= price
            if clicked:
                self.__balance += 1
        self.num_rounds -= 1

