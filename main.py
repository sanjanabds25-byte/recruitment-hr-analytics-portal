# Recruitment & HR Analytics Portal

candidates = []
applications = []
interviews = []


# Add Candidate
def add_candidate():
    candidate_id = len(candidates) + 1
    name = input("Enter candidate name: ")
    email = input("Enter email: ")
    skills = input("Enter skills: ")
    experience = int(input("Enter experience in years: "))

    candidate = {
        "id": candidate_id,
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    }

    candidates.append(candidate)
    print("Candidate added successfully!")


# View Candidates
def view_candidates():
    if not candidates:
        print("No candidates found.")
        return

    print("\n--- Candidate List ---")
    for c in candidates:
        print("ID:", c["id"])
        print("Name:", c["name"])
        print("Email:", c["email"])
        print("Skills:", c["skills"])
        print("Experience:", c["experience"], "years")
        print("----------------------")


# Add Job Application
def add_application():
    if not candidates:
        print("Please add a candidate first.")
        return

    candidate_id = int(input("Enter candidate ID: "))
    job = input("Enter job position: ")

    application = {
        "candidate_id": candidate_id,
        "job": job,
        "status": "Applied"
    }

    applications.append(application)
    print("Application added successfully!")


# View Applications
def view_applications():
    if not applications:
        print("No applications found.")
        return

    print("\n--- Application List ---")
    for a in applications:
        print("Candidate ID:", a["candidate_id"])
        print("Job:", a["job"])
        print("Status:", a["status"])
        print("------------------------")


# Schedule Interview
def schedule_interview():
    if not applications:
        print("Please add an application first.")
        return

    candidate_id = int(input("Enter candidate ID: "))
    date = input("Enter interview date: ")
    time = input("Enter interview time: ")

    interview = {
        "candidate_id": candidate_id,
        "date": date,
        "time": time
    }

    interviews.append(interview)
    print("Interview scheduled successfully!")


# View Interviews
def view_interviews():
    if not interviews:
        print("No interviews scheduled.")
        return

    print("\n--- Interview Schedule ---")
    for i in interviews:
        print("Candidate ID:", i["candidate_id"])
        print("Date:", i["date"])
        print("Time:", i["time"])
        print("--------------------------")


# Main Menu
def main():
    while True:
        print("\n===== Recruitment & HR Analytics Portal =====")
        print("1. Add Candidate")
        print("2. View Candidates")
        print("3. Add Job Application")
        print("4. View Applications")
        print("5. Schedule Interview")
        print("6. View Interviews")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            add_application()
        elif choice == "4":
            view_applications()
        elif choice == "5":
            schedule_interview()
        elif choice == "6":
            view_interviews()
        elif choice == "7":
            print("Thank you for using the HR Analytics Portal!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
