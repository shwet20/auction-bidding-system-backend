# Auction Bidding System Backend

This project is an Auction Bidding System backend built using Python and Django REST Framework (DRF). The system is divided into two main microservices: User Management and Authentication, and Auction Management and Bidding. The project ensures secure user management, auction creation, and bidding process management.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

### User Management and Authentication
- **Admin Access**: Admin can access all user data and perform CRUD operations on users.
- **Admin Authentication**: Admin authentication using a static API secret across the project.
- **User Registration and Login**: Users can register and log in. User login is token-based, which can later be used for placing bids.
- **Token-Based Authentication**: Ensures secure access to user-specific functionalities.

### Auction Management and Bidding
- **CRUD Operations on Auctions**: Admin can create, read, update, and delete auctions.
- **Auction Details**: Each auction includes start time, end time, start price, item name, and the user ID of the user who won the auction.
- **View Active Auctions**: Normal users can view all ongoing auctions.
- **View All Auctions**: Admin can view the status of all auctions at any time.
- **Auction Completion**: Automatically determines the winner based on the highest bid once the auction ends.
- **Bidding System**: Users can place bids on active auctions.

## Technologies Used

- **Python**: The core programming language used for development.
- **Django**: High-level Python web framework for rapid development.
- **Django REST Framework (DRF)**: Toolkit for building Web APIs.
- **SQLite**: Default database for development (can be replaced with PostgreSQL, MySQL, etc. for production).
- **JWT Authentication**: For secure user authentication.

## Installation

### Prerequisites

- Python 
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/auction-bidding-system-backend.git
    cd auction-bidding-system-backend
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (for accessing the admin panel):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

### Admin Panel

- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Use the superuser credentials created during installation to log in.

### Authentication

- Admin authentication via static API secret (for endpoints requiring admin access)
- User authentication via JWT tokens
