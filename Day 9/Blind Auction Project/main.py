from art import logo
print(logo)
bidders={}
more_bidders=True
while more_bidders:
    name=input("What is your name? ")
    bid=input("What is your bid amount? ")
    bidders[name]=bid
    more=input("Do you have more bidders type yes or no").lower()
    if more=="no":
        break
    print("\n"*18)
max_value=max(bidders.values())
max_key=[key for key, val in bidders.items() if val==max_value]
print(f"The winner of the bid is {max_key[0]} with the value of {max_value}")
print(bidders)



