class Job:
    ALLOWED_STATUSES = [
        "Applied",
        "Interview Scheduled",
        "Selected",
        "Rejected"
    ]

    def __init__(self, company, role, location, status):
        self.company = company
        self.role = role
        self.location = location
        self.status = status

    def show_details(self):
        print(f"{self.company} - {self.role}")
        print(f"Location: {self.location}")
        print(f"Status: {self.status}")

    def update_status(self, new_status):
        if new_status in self.ALLOWED_STATUSES:
            self.status = new_status
            print("Status updated successfully.")
        else:
            print("Invalid Status.")


class InternshipJob(Job):

    def __init__(self, company, role, location, status, stipend, duration):
        super().__init__(company, role, location, status)
        self.stipend = stipend
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Stipend: {self.stipend}")
        print(f"Duration: {self.duration}")