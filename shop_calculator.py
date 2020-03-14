number_of_items = int(input("Number of items: "))
item_cost = [0]*number_of_items

i = 0
while i != number_of_items:
    item_cost[i] = int(input("Print of item: "))
    i = i + 1
total_cost = sum(item_cost)
print("Total price for",i, "item is $",total_cost)