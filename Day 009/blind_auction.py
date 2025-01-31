from blind_auction_art import logo

print(logo)


def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_auction = True
while continue_auction:
    name = input("What is your name?: ")
    new_bid = int(input("What is your bid?: $"))
    bids[name] = new_bid
    should_continue = input("Are there any more bidders? 'yes' or 'no': \n").lower()
    if should_continue == "no":
        continue_auction = False
        find_highest_bid(bids)
    elif should_continue == "yes":
        print("\n" * 100)
