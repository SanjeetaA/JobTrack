#job class

class Job:
    def __init__(self, company, role, location, status):
        self.company = company
        self.role = role
        self.location = location
        self.status = status


    def display(self):
        print(f"{self.company} - {self.role}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")



    def update_status(self, new_status):
        allowed_statuses = ["Applied", "Interview Scheduled", "Selected", "Rejected"]

        if new_status in allowed_statuses:
            self.status = new_status
            print("Status updated successfully.")
        else:
            print("Invalid Status.")


    def show_details(self):
        print(f"{self.company} - {self.role}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")


job1 = Job("Google", "Python Intern", "Noida", "Applied")
job2 = Job("Microsoft", "Backend Intern", "Gurgaon", "Interview Scheduled")



#internship job class

class InternshipJob(Job):

    def __init__(self, company, role, location, status, stipend, duration):
        super().__init__(company, role, location, status)
        self.stipend = stipend
        self.duration = duration

    def show_internship_details(self):
        self.display()
        print(f"Stipend: {self.stipend}")
        print(f"Duration: {self.duration}")


    def show_details(self):
        print(f"{self.company} - {self.role}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")
        print(f"Stipend: {self.stipend}")
        print(f"Duration: {self.duration}")




internship1 = InternshipJob(
    "Microsoft",
    "Backend Intern",
    "Gurgaon",
    "Applied",
    25000,
    "6 months"
)


#list

jobs = [job1,internship1]

for job in jobs:
    job.show_details()
    print()



#CALLING FUNCTIONS





