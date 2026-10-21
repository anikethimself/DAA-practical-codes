def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0

    return total_value


n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = float(input(f"Enter weight of item {i+1}: "))
    value = float(input(f"Enter value of item {i+1}: "))
    items.append((weight, value))

capacity = float(input("Enter knapsack capacity: "))

max_value = fractional_knapsack(capacity, items)

print("Maximum value in Knapsack:", max_value)