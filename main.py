import csv

restock_items = []

# Read the stock data
with open("stock.csv", "r") as file:
    reader = csv.DictReader(file)

    for item in reader:
        current = int(item["current_quantity"])
        threshold = int(item["reorder_threshold"])

        if current < threshold:
            restock_items.append(item)

# Print the report
print("\n===== RESTOCK NEEDED REPORT =====")

if restock_items:
    for item in restock_items:
        print(
            f"Item: {item['item_name']}"
            f" | Current Quantity: {item['current_quantity']}"
            f" | Reorder Threshold: {item['reorder_threshold']}"
        )
else:
    print("No items need restocking.")

# Save the report as a CSV file
with open("restock_report.csv", "w", newline="") as file:
    fieldnames = ["item_name", "current_quantity", "reorder_threshold"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for item in restock_items:
        writer.writerow(item)

print("\nRestock report has been saved to 'restock_report.csv'.")