import json

with open("jobs.json", "r") as file:
    jobs = json.load(file)

for job in jobs:
    print(job["company"])
    print(job["role"])
    print(job["status"])
    print()

print(jobs)


companies = ["Google","Microsoft", "Amazon", "Facebook", "Apple"]

#ALL JOB DETAILS

jobs = [ 
{
    "company": "Google",
    "role": "Python Intern",
    "location": "Noida",
    "status": "Applied"
},
{
    "company": "Microsoft",
    "role": "Python Intern",
    "location": "Noida",
    "status": "Applied"
},
{
    "company": "Amazon",
    "role": "Python Intern",
    "location": "Noida",
    "status": "Applied"
},
{
    "company": "Facebook",
    "role": "Python Intern",
    "location": "Noida",
    "status": "Applied"
},
{
    "company": "Apple",
    "role": "Python Intern",
    "location": "Noida",
    "status": "Interview Scheduled"
}
]

#1PRINTS ALL COMPANY NAMES

def show_companies(companies):
    for company in companies:
     print(company)
     print();





#2PRINTS DEF FUN TO SHOW ALL JOBS DETAILS

def show_jobs(jobs):
    for job in jobs:
        print(job["company"])
        print(job["role"])
        print(job["location"])
        print(job["status"])
        print()





#3PRINTS ALL JOBS WITH STATUS

def show_jobs_status(jobs):
    for job in jobs:
        print(f'{job["company"]} - {job["role"]}')

        if job["status"] == "Interview Scheduled":
            print("Interview has been scheduled.")
        elif job["status"] == "Selected":
            print("you have been selected for the role.")
        elif job["status"] == "Rejected":
            print("you have been rejected for the role.")
        else:
            print("Application Submitted")
        print()



