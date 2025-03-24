🌦️ WeatherApp - Django Weather Application
WeatherApp Screenshot <!-- You'll add your screenshot here -->

A modern weather application built with Django that provides real-time weather information for any location worldwide. Features user authentication, weather data visualization, and a responsive design.

✨ Features
Real-time Weather Data: Get current weather conditions for any city

User Authentication: Secure login and registration system

Beautiful UI: Modern, responsive design with Bootstrap 5

Weather Icons: Visual representation of weather conditions

Detailed Metrics: Temperature, humidity, wind speed, and conditions

🛠️ Technologies Used
Backend: Django 5.1

Frontend: Bootstrap 5, Font Awesome

Weather API: WeatherAPI.com

Database: SQLite (default)

🚀 Installation & Setup
Prerequisites
Python 3.8+

pip package manager

Git (optional)

Step-by-Step Installation
Clone the repository

bash
Copy
git clone https://github.com/Meer-Rind/WeatherApp.git
cd WeatherApp
Create and activate virtual environment

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies

bash
Copy
pip install -r requirements.txt
Set up environment variables
Create a .env file in the project root with:

Copy
SECRET_KEY=your-django-secret-key
WEATHER_API_KEY=your-weatherapi-key
Apply migrations


**python manage.py migrate**
Create superuser (optional)


**python manage.py createsuperuser**
Run the development server


**python manage.py runserver**
Access the application
Open your browser and visit:

Copy
http://127.0.0.1:8000/
📸 Screenshots

welcome page ![Screenshot from 2025-03-24 16-58-25](https://github.com/user-attachments/assets/d23f3aad-1cab-4e6c-8915-8770cb6334b9)

Login Pag![Screenshot from 2025-03-24 17-00-33](https://github.com/user-attachments/assets/7905ab22-d7e6-4d7d-a3f3-9b96a740c489)
e	Weather![Screenshot from 2025-03-24 17-01-40](https://github.com/user-attachments/assets/b3417a4b-65bd-4f2a-9d95-cef1bb28eb6d)

Register Page![Screenshot from 2025-03-24 17-00-28](https://github.com/user-attachments/assets/e8996c06-3f63-49ad-b67c-198e60b4954c)

🌐 API Usage
This application uses WeatherAPI.com to fetch weather data. You'll need to:

Sign up for a free account at WeatherAPI.com

Get your API key

Add it to your .env file as WEATHER_API_KEY

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Meer-Rind
GitHub
