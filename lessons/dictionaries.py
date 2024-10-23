"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}


# len evaluates to number of key-value entries
print(len(ice_cream))

# Adding stuff to a dictionary using subscription notation
ice_cream["mint"] = 10

# Access values by their key using subscription
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# Reassign values by their key using assignment
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using the pop method
ice_cream.pop("strawberry")

# Test if a key is in the dictionary
print("Americone Dream" in ice_cream)
# would return False because its not in the dictionary

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}:{tally}")
