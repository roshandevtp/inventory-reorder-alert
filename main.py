import csv

restock_items = []

# Read the stock data
with open("stock.csv", "r") as file:
    reader = csv.DictReader(file)

    for item in reader:
        current = int(item["current_quantity"])
        threshold = int(item["reorder_threshold"])

        if current < threshold:

            # Priority Level
            if current < (0.25 * threshold):
                priority = "Critical"
            else:
                priority = "Low"

            # Reorder Suggestion
            reorder = threshold - current

            restock_items.append({
                "item_name": item["item_name"],
                "current_quantity": current,
                "reorder_threshold": threshold,
                "priority": priority,
                "reorder_quantity": reorder
            })

# Simulated Email Alert
print("\nSubject: Stock Restock Alert\n")

print("Hello Warehouse Team,\n")

if restock_items:
    print("The following items need to be restocked:\n")

    for item in restock_items:
        print(f"Item: {item['item_name']}")
        print(f"Current Quantity : {item['current_quantity']}")
        print(f"Threshold        : {item['reorder_threshold']}")
        print(f"Priority         : {item['priority']}")
        print(f"Suggested Order  : {item['reorder_quantity']} units")
        print("-" * 35)
else:
    print("All items have sufficient stock.")

print("\nRegards,")
print("Inventory Management System")

# Saving report as CSV file
with open("restock_report.csv", "w", newline="") as file:
    fields = [
        "item_name",
        "current_quantity",
        "reorder_threshold",
        "priority",
        "reorder_quantity"
    ]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    for item in restock_items:
        writer.writerow(item)

print("\nReport saved as restock_report.csv")