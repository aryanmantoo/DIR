import pandas as pd
import json

# Load input JSON data into a pandas DataFrame
with open("input.json") as f:
    input_data = json.load(f)

df = pd.json_normalize(input_data)

# Transform input data into desired format
df["full_name"] = df["first_name"] + " " + df["last_name"]
output_data = df[[ "full_name", "email"]].to_dict(orient="records")

# Write output JSON data to file
with open("output.json", "w") as f:
    json.dump(output_data, f)

print("Data converted and written to output.json.")
