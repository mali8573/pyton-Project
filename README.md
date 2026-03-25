# 🚀 TaskMaster - Enterprise Task Management System

**TaskMaster** is a robust, Django-based task management solution designed to streamline multi-team workflows. The system features hierarchical user management, real-time task tracking, and strict permission isolation.

## 🌟 Key Features
* **Hierarchical Role System:** Supports 3 distinct access levels:
    * **Super Admin:** Organization-wide management, team creation, and global task oversight.
    * **Admin (Team Lead):** Manages team-specific tasks and assigns them to workers.
    * **Worker:** Views team assignments and updates personal task progress.
* **Task Lifecycle Management:** Comprehensive tracking from "New" to "Active" and "Finished".
* **Built-in Security & Permissions:** Ensures data integrity by exposing information only to authorized users based on their roles and teams.
* **Modern UI/UX:** Clean, dark-mode professional interface built with custom CSS and smooth transitions.

## 🛠 Tech Stack
* **Backend:** Python & Django Framework.
* **Database:** SQLite (Easily scalable to PostgreSQL/MySQL).
* **Frontend:** Django Templates, Custom CSS3, JavaScript.
* **Authentication:** Integrated Django Auth System with custom profile extensions.

## 📁 Project Architecture
The system follows a modular design to separate business logic from the presentation layer:
* `models.py`: Core entities including Task, Worker, Team, and Role.
* `views.py`: Logic handling, permission-based QuerySet filtering, and form processing.
* `forms.py`: Custom Django forms with advanced validation (e.g., future-date verification).
* `templates/`: Responsive UI including custom-designed error pages (403, 404).

## 💡 Engineering Insights: Solving the Hierarchy Challenge
A significant technical challenge was implementing a multi-level permission system. I addressed this by:
1.  Extending the default Django User model using a `OneToOneField` to a `Worker` model.
2.  Customizing form `__init__` methods to dynamically filter team members based on the logged-in Admin's team.
3.  Implementing granular logic in the Views to ensure cross-team data isolation while allowing Super Admins full visibility.

---

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone [your-repository-link]
  

2. Install dependencies:
   ```bash
   pip install django
   Run migrations and start the server:


3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
