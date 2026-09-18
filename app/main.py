import json

with open("data/jobs.json", "r") as file:
    jobs = json.load(file)

for job in jobs:
    print(f'{job["company"]} - {job["role"]}')
    print(f'Status: {job["status"]}')
    print()