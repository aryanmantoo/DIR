from fastapi import UploadFile, File
from typing import List
import json

async def convert_files(input_files: List[UploadFile], output_files: List[str]):
    for i, input_file in enumerate(input_files):
        # Load input JSON data into a dictionary
        input_data = json.load(input_file.file)

        # Transform input data into desired format
        output_data = {
            "id": input_data["id"],
            "full_name": f"{input_data['first_name']} {input_data['last_name']}",
            "email": input_data["email"]
        }

        # Write output JSON data to file
        with open(output_files[i], "w") as f:
            json.dump(output_data, f)

    # Return success message
    return {"message": f"Data converted successfully and written to {len(input_files)} files."}

File = lambda x: x  # dummy function to prevent syntax errors
