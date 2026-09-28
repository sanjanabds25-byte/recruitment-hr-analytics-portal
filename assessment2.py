# Recruitment & HR Analytics Portal - Assessment 2

candidates = []
applications = []
interviews = []


# ---------------- ADD CANDIDATE ----------------
def add_candidate():
    candidate_id = len(candidates) + 1

    name = input("Enter candidate name: ")
    email = input("Enter email: ")
    skills = input("Enter skills: ")

    while True:
        try:
            experience = int(input("Enter experience in years: "))
            if experience >= 0:
                break
            print("Experience cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")

    candidate = {
        "id": candidate_id,
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    }

    candidates.append(candidate)
    print("Candidate added successfully!")


# ---------------- VIEW CANDIDATES ----------------
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


# ---------------- SEARCH CANDIDATE ----------------
def search_candidate():
    if not candidates:
        print("No candidates found.")
        return

    keyword = input("Enter candidate name or skill to search: ").lower()

    found = False

    for c in candidates:
        if keyword in c["name"].lower() or keyword in c["skills"].lower():
            print("\nCandidate Found")
            print("ID:", c["id"])
            print("Name:", c["name"])
            print("Email:", c["email"])
            print("Skills:", c["skills"])
            print("Experience:", c["experience"], "years")
            found = True

    if not found:
        print("No matching candidate found.")


# ---------------- UPDATE CANDIDATE ----------------
def update_candidate():
    if not candidates:
        print("No candidates found.")
        return

    try:
        candidate_id = int(input("Enter candidate ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for c in candidates:
        if c["id"] == candidate_id:

            print("Enter new details:")

            c["name"] = input("Enter new name: ")
            c["email"] = input("Enter new email: ")
            c["skills"] = input("Enter new skills: ")

            try:
                c["experience"] = int(
                    input("Enter new experience in years: ")
                )
            except ValueError:
                print("Invalid experience. Previous value retained.")

            print("Candidate updated successfully!")
            return

    print("Candidate not found.")


# ---------------- DELETE CANDIDATE ----------------
def delete_candidate():
    if not candidates:
        print("No candidates found.")
        return

    try:
        candidate_id = int(input("Enter candidate ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for c in candidates:
        if c["id"] == candidate_id:
            candidates.remove(c)
            print("Candidate deleted successfully!")
            return

    print("Candidate not found.")


# ---------------- ADD APPLICATION ----------------
def add_application():
    if not candidates:
        print("Please add a candidate first.")
        return

    try:
        candidate_id = int(input("Enter candidate ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    candidate_exists = False

    for c in candidates:
        if c["id"] == candidate_id:
            candidate_exists = True
            break

    if not candidate_exists:
        print("Candidate not found.")
        return

    job = input("Enter job position: ")

    application = {
        "candidate_id": candidate_id,
        "job": job,
        "status": "Applied"
    }

    applications.append(application)
    print("Application added successfully!")


# ---------------- VIEW APPLICATIONS ----------------
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


# ---------------- UPDATE APPLICATION STATUS ----------------
def update_application_status():
    if not applications:
        print("No applications found.")
        return

    try:
        candidate_id = int(input("Enter candidate ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for a in applications:
        if a["candidate_id"] == candidate_id:

            print("\n1. Applied")
            print("2. Shortlisted")
            print("3. Rejected")
            print("4. Selected")

            choice = input("Enter new status: ")

            status = {
                "1": "Applied",
                "2": "Shortlisted",
                "3": "Rejected",
                "4": "Selected"
            }

            if choice in status:
                a["status"] = status[choice]
                print("Application status updated!")
            else:
                print("Invalid choice.")

            return

    print("Application not found.")


# ---------------- SCHEDULE INTERVIEW ----------------
def schedule_interview():
    if not applications:
        print("Please add an application first.")
        return

    try:
        candidate_id = int(input("Enter candidate ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    date = input("Enter interview date: ")
    time = input("Enter interview time: ")

    interview = {
        "candidate_id": candidate_id,
        "date": date,
        "time": time
    }

    interviews.append(interview)
    print("Interview scheduled successfully!")


# ---------------- VIEW INTERVIEWS ----------------
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


# ---------------- HR ANALYTICS ----------------
def hr_analytics():
    print("\n===== HR ANALYTICS =====")

    print("Total Candidates:", len(candidates))
    print("Total Applications:", len(applications))
    print("Total Interviews:", len(interviews))

    selected = 0
    shortlisted = 0
    rejected = 0

    for a in applications:
        if a["status"] == "Selected":
            selected += 1
        elif a["status"] == "Shortlisted":
            shortlisted += 1
        elif a["status"] == "Rejected":
            rejected += 1

    print("Selected Candidates:", selected)
    print("Shortlisted Candidates:", shortlisted)
    print("Rejected Applications:", rejected)


# ---------------- MAIN MENU ----------------
def main():

    while True:

        print("\n========================================")
        print(" Recruitment & HR Analytics Portal")
        print("========================================")

        print("1. Add Candidate")
        print("2. View Candidates")
        print("3. Search Candidate")
        print("4. Update Candidate")
        print("5. Delete Candidate")
        print("6. Add Job Application")
        print("7. View Applications")
        print("8. Update Application Status")
        print("9. Schedule Interview")
        print("10. View Interviews")
        print("11. HR Analytics")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_candidate()

        elif choice == "2":
            view_candidates()

        elif choice == "3":
            search_candidate()

        elif choice == "4":
            update_candidate()

        elif choice == "5":
            delete_candidate()

        elif choice == "6":
            add_application()

        elif choice == "7":
            view_applications()

        elif choice == "8":
            update_application_status()

        elif choice == "9":
            schedule_interview()

        elif choice == "10":
            view_interviews()

        elif choice == "11":
            hr_analytics()

        elif choice == "12":
            print("Thank you for using the HR Analytics Portal!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
