
import pandas as pd

# Read txt file
df = pd.read_csv("Pasted text.txt")

# Save as csv
df.to_csv("medical_examination.csv", index=False)

print("CSV file created successfully!")
