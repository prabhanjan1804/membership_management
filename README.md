#In Testing phase for security protocols

##Membership Management System

A Django-based web portal for managing memberships within the student-run organization Studentische Selbstverwaltung ‘StuSta’ e.V.. Designed with role-based access, real-time filtering, data export, and administrative functionality tailored for the Vorstand.

⸻

🚀 Features

👥 Member Directory
	•	Full list of members with details: name, birthdate, email, address, and membership status
	•	Client-side search bar for real-time filtering by name or email
	•	One-click export of member list to CSV
	•	Print-friendly layout for documentation

🔐 Role-Based Access (RBAC)
	•	Authentication using Django’s built-in user system
	•	Conditional interface elements based on user group
	•	Vorstand users see additional sidebar with quick navigation to:
	•	Approve new members (view pending)
	•	View/manage users, groups, permissions
	•	Access log entries and content types

⚙️ Extensibility
	•	Modular Django structure with template inheritance
	•	URLs and views ready for expansion (e.g. approval logic, renewal reminders)
	•	Custom permission logic can be easily added using decorators or middleware

⸻

🛠 Setup Instructions
	1.	Clone the Repository

git clone https://github.com/prabhanjan1804/membership_management.git
cd membership_management

	2.	Create a Virtual Environment

python3 -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

	3.	Install Dependencies

pip install -r requirements.txt

	4.	Apply Migrations & Create Superuser

python manage.py migrate
python manage.py createsuperuser

	5.	Run the Server

python manage.py runserver

Visit http://127.0.0.1:8000/members/ to access the member list.

⸻

🧪 Development Notes
	•	Tested with Python 3.13 and Django 5.2
	•	Uses Django’s built-in Group model for role segregation
	•	Simple inline styles; can be upgraded to Tailwind or Bootstrap
	•	Dark mode was implemented and later removed — can be re-enabled via version control

⸻

📁 Project Structure

membership_management/
├── members/
│   ├── templates/
│   │   └── member_list.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── templates/
│   └── base.html
├── static/
│   ├── css/style.css
│   └── images/logo.png
├── manage.py
└── README.md



🙌 Credits

Created by Prabhanjan Kulkarni (Leiter des Informationsausschusses) for Studentische Selbstverwaltung 'StuSta' e.V.
