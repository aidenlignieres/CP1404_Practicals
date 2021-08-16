item_count = int(input("Number of items: "))
total_cost = 0

while item_count < 0:
    print("invalid number of items!")
    item_count = int(input("Number of items: "))

for i in range(item_count):
    item_cost = float(input("Price of item: "))
    total_cost += item_cost

if total_cost > 100:
    discount = total_cost * 0.1
    total_cost = total_cost - discount

print(f"Total price for {item_count} items is ${total_cost:.2f}")
