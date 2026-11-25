'''
this code is used to convert the elnino34_sst.data file
to t csv file for easy reading.
'''


import pandas as pd

rows = []
with open("elnino34_sst.data", "r") as f:
    for line in f:
        parts = line.split()
        # Keep only data rows: 4-digit Year + 12 monthly values (13 columns)
        if len(parts) == 13 and parts[0].isdigit() and len(parts[0]) == 4:
            rows.append([int(parts[0])] + [float(x) for x in parts[1:]])

columns = ["Year", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

df = pd.DataFrame(rows, columns=columns)

# Replace standard missing-value flags (e.g., -99.99) with empty/NaN cells
df = df.replace([-99.99, -999.0, -999.9], pd.NA)

df.to_csv("elnino34_sst_converted.csv", index=False)
print(f"Saved {len(df)} years ({df['Year'].min()}–{df['Year'].max()}) to elnino34_sst_converted.csv")