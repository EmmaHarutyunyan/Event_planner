# Event Planner Project

Event Planner is a Django-based web application designed for event management. The platform allows users to plan and book events, manage their bookings, and view event categories such as weddings, corporate events, and private parties. Users can explore different event packages, make reservations, and track their booking history. The application features user authentication, a personalized dashboard, and a responsive design for an enhanced user experience.

## Pages Overview

### 1. User Dashboard Page
The **User Dashboard** allows authenticated users to view their account details, confirm bookings, and track recent bookings. Users can also edit their profiles and navigate to their booking history.

### 2. Base Layout
The **Base Layout** is the main structure of the site, featuring a navigation bar with links to essential pages such as the user dashboard, login/signup, and event search. It also includes a search bar for users to search events.

### 3. Login Page
The **Login Page** allows users to log in to their accounts by providing their username and password. If the credentials are incorrect, an error message is shown. Users can also access the signup page if they don't have an account.

### 4. Home Page
The **Home Page** provides an overview of the event planning services, showcasing the categories and packages available for booking. The page includes:
- A welcome section with a brief description of the platform.
- A category listing section that allows users to explore events by category.
- A countdown timer for the next big event.
- A booking section to reserve spots for upcoming events.

### 5. Event Details Page
The **Event Details Page** allows users to view the event details, including category, date, time, and booking status. Users can explore available packages for the event with detailed descriptions and benefits, and make a booking by selecting the date, time, and package.

### 6. Bookings History Page
The **Bookings History Page** displays the user's previous bookings with relevant details such as event title, date, and status. Users can also access more information about each booking.

### 7. Search Results Page
The **Search Results Page** displays events matching the user's search query. It shows the following:
- A list of events with their image, title, description, date, time, location, and ticket price.
- A link to view more details about each event.
If no events are found matching the query, a message is shown stating that no events were found.

## Features
- User authentication (login, signup)
- Dashboard for users to manage their bookings and profiles
- Search functionality to find events based on various criteria
- Ability to view and manage user profiles and bookings
- Event categories, detailed event descriptions, and booking packages
- Fully responsive design with animations for enhanced user experience

## Requirements
- Django
- Python 3.x
- Additional Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/EmmaHarutyunyan/Event_planner.git
    ```

2. Navigate to the project folder:

    ```bash
    cd event-planner
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of your project and add the following lines:

    ```bash
    SECRET_KEY='your-secret-key-here'
    ```

    - **SECRET_KEY**: You can generate a secret key using Django's `django.core.management.utils.get_random_secret_key()` function or by using an online generator.

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit the app in your browser at `http://127.0.0.1:8000/`.


## Below are some videos and screenshots from project.

https://github.com/user-attachments/assets/79236cee-2ccc-498a-9d13-1a7d41f8af08

https://github.com/user-attachments/assets/c176ed0b-3520-4f9d-ba7e-e9bf0012e8dc

https://github.com/user-attachments/assets/55e0073a-ff98-4ff4-936d-abb8cf64b4dc

![birthday_packages](https://github.com/user-attachments/assets/4d5b3e95-4751-42fe-9f0a-c64b03eea3c8)

![user_bookings](https://github.com/user-attachments/assets/b284b62d-24c9-4cdf-b0ba-2017c4f7c8be)

![event_packages](https://github.com/user-attachments/assets/5536e031-ee24-4e5e-9794-b47d9b6c847c)

