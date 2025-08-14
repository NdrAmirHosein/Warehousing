# Simple Warehousing App

A lightweight warehousing management system built with **Django**, using **PostgreSQL** as the database backend.  
The application follows the **Class-Based View (CBV)** pattern for clean and maintainable code.

## Features
- Easy PostgreSQL integration — just update the database settings in `settings.py`.
- Manage:
  - Utilities
  - Warehouses
  - Products
  - Types of Usage
  - And more...
- Clean architecture with Class-Based Views for scalability.

## Setup
1. **Clone the repository**:

   git clone <your-repo-url>
   cd <your-project-folder>

2. **Configure the database:**
    
    Open settings.py and update your PostgreSQL credentials.

3. **Apply migrations:**
    python manage.py migrate

4. **Run the development server:**
    python manage.py runserver

## Notes
  - Sensitive files and credentials have been removed to protect proprietary information.
  - Configured for local development by default — you can adapt it for production.

Thank You For Your Time