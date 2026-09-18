from app.jobs import Job


def test_job_creation():
    job = Job("Google", "Python Intern", "Noida", "Applied")

    assert job.company == "Google"
    assert job.role == "Python Intern"
    assert job.location == "Noida"
    assert job.status == "Applied"