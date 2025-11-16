Backend (Flask)
---------------
1. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\Activate.ps1

2. Install requirements:
   pip install -r requirements.txt

3. Run the backend:
   python app.py

API Endpoint:
POST /api/login
Body: { "username": "user", "password": "pass" }
