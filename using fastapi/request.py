import requests
import requests

url = " http://127.0.0.1:8000_json"

input_file = ("input.json", open("path/to/input.json", "rb"), "application/json")
output_file = ("output.json", open("path/to/output.json", "wb"), "application/json")

response = requests.post(url, files={"input_files": input_file, "output_files": output_file})

print(response.json())

