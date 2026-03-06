for x in range(3):  # Outer loop
    for y in range(2):  # inner loop
        for z in range(2):   # inner loop
            print(f"({x}, {y}, {z})")

# Use case of nested loop

#1 - Crossing or Combining Data (Pairing the data)

colors = ['Red','Blue','Orange']
sizes = ['XL','L','M']

for color in colors:
    for size in sizes:
        print(f"{color} Size - {size}")


# Navigate Hierarchy 

years = [2026, 2027]
months = ["Jan", "Feb"]
days = range(1, 6)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")

# Navigate through tables and columns
tables = [2026, 2027]
columns = ["Jan", "Feb"]
rows = range(1, 6)

for t in tables:
    for c in columns:
        for r in rows:
            print(f"report_{y}_{m}_{d}.csv")


# To retrieve data from multiple tables for e.g. we have 100 tables and we need to check same query for each
# SELECT count(*) FROM customers where id IS NULL

tables = ['customers','orders','products','prices','employees','reports']
columns = ['id','create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} where {c} IS NULL;')
