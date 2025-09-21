# Full-Stack To-Do List Application

This is a complete full-stack web application featuring a modern frontend, a robust backend, and a fully containerized deployment environment using Docker. The application allows users to create, view, update, and delete tasks.

 

## Features

*   **Modern Frontend:** A clean, responsive user interface built with **React**.
*   **Robust Backend:** A powerful and fast API built with **Python** and **FastAPI**.
*   **Persistent Storage:** Tasks are saved in a `tasks.json` file, with data persistence handled by Docker volumes.
*   **Containerized:** The entire application stack is containerized with **Docker** and orchestrated with **Docker Compose** for easy, reproducible deployments.
*   **Secure:** Built with security in mind, leveraging modern framework features to protect against common vulnerabilities like XSS and invalid data injection.
*   **Tested:** Includes a complete test suite for the backend API using **Pytest**.

## Tech Stack

*   **Frontend:** React (Web GUI)
*   **Backend:** Python 3.9, FastAPI, Pydantic, Uvicorn
*   **Web Server/Proxy:** Nginx
*   **Containerization:** Docker & Docker Compose
*   **Testing:** Pytest, Node.js (for security script)

### Project Structure

The project is organized into a clean, modern monorepo structure with clear separation between the frontend, backend, data, and utility scripts.

```
simple_todolist_finalmini/
│
├── .gitignore               # Specifies files/folders for Git to ignore.
├── README.md                # This documentation file.
├── docker-compose.yml       # The master file to run the entire application stack.
├── package.json             # Dependencies for local utility scripts (e.g., security test).
├── package-lock.json        # Locks dependency versions for local scripts.
│
├── backend/
│   ├── Dockerfile           # Blueprint to build the Python backend container.
│   ├── __init__.py          # Marks the folder as a Python package.
│   ├── main.py              # The FastAPI application source code.
│   ├── pyproject.toml       # Project metadata and build configuration for Python.
│   ├── requirements.txt     # A list of Python libraries for the backend.
│   └── tests/
│       ├── __init__.py      # Marks the tests folder as a sub-package.
│       └── test_todo.py     # The Pytest suite for the backend API.
│
├── backend-data/
│   └── tasks.json           # Persistent data storage for the to-do tasks.
│
├── frontend/
│   ├── Dockerfile           # Blueprint to build the React frontend and Nginx server.
│   ├── nginx.conf           # Configuration for the Nginx web server and proxy.
│   ├── package.json         # Dependencies (React, etc.) for the frontend app.
│   ├── public/
│   │   ├── index.html       # The main HTML shell for the React app.
│   │   └── ... (favicon and icon files)
│   └── src/
│       ├── App.js           # The main React component with UI and logic.
│       └── index.js         # The entry point for the React application.
│
└── scripts/
    └── comprehensive-security-test.js # Utility script for security testing.
```

### Key Components

*   **`docker-compose.yml`**: The master file for Docker Compose. It defines all services (`backend`, `frontend`), networks, and volumes. This is the entry point for running the entire application.
*   **`backend/`**: Contains the Python FastAPI application, including all API logic (`main.py`) and tests (`tests/`).
*   **`frontend/`**: Contains the React application, including all UI components (`src/`), static assets (`public/`), and the Nginx configuration (`nginx.conf`).
*   **`Dockerfile`s**: Each service directory (`backend`, `frontend`) contains a `Dockerfile` that defines the steps to build its respective container image.
*   **`backend-data/`**: A persistent volume mount for the application's data. The `tasks.json` file is stored here to ensure data is not lost when containers are stopped or rebuilt.
*   **`scripts/`**: Contains utility and testing scripts, such as the comprehensive security scan.
*   **`.gitignore`**: Specifies intentionally untracked files (like `node_modules` and `.venv`) to exclude from Git version control.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have the following software installed on your machine:

1.  **Docker & Docker Compose:** This is the only essential requirement to run the entire application stack.
    *   [Install Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
2.  **Node.js & npm:** Required only for running the security test script.
    *   [Install Node.js](https://nodejs.org/)
3.  **Git:** For cloning the repository.
    *   [Install Git](https://git-scm.com/downloads)

### Installation & Running the Application

Running this application is incredibly simple thanks to Docker.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ms584/Simple-To-Do-List-Manager.git
    cd Simple-To-Do-List-Manager
    ```

2.  **Build and run the containers:**
    This single command will build the frontend and backend images, create the necessary containers and networks, and start the application.
    ```bash
    docker compose up --build
    ```
    *   Add the `-d` flag (`docker compose up --build -d`) to run the containers in the background.

3.  **Access the application:**
    Once the containers are running, open your web browser and navigate to:
    > **`http://localhost`**

To stop the application, press `Ctrl+C` in the terminal where it is running. If it's running in the background, use the command `docker compose down`.

---

## Testing

The project includes a full suite of tests for the backend API and a security scanning script.

### Backend API Tests (Pytest)

These tests verify the core functionality of the API endpoints (GET, POST, PUT, DELETE). The most reliable way to run these is inside the Docker container to ensure the environment is identical to production.

1.  **Ensure the application is running:**
    ```bash
    docker compose up -d
    ```

2.  **Execute the tests inside the backend container:**
    ```bash
    docker compose exec backend pytest
    ```
    You should see all tests pass successfully.

### Security Vulnerability Scan

This project includes a Node.js script that tests the API for common vulnerabilities such as XSS, DOM manipulation, NoSQL injection, and malformed JSON payloads.

1.  **Ensure the application is running:**
    ```bash
    docker compose up -d
    ```

2.  **Install the script's dependencies:**
    (You only need to do this once)
    ```bash
    npm install
    ```

3.  **Run the security test script:**
    ```bash
    node scripts/comprehensive-security-test.js
    ```
    The script will output its results to the console, demonstrating the application's resilience to these common attacks.

---

## Deployment

This application is designed for easy deployment to any cloud hosting provider that supports Docker.

1.  **Provision a Server:** Get a cloud server (VPS) from a provider like DigitalOcean, Linode, Vultr, etc. A basic server running **Ubuntu 22.04 LTS** is recommended.

2.  **Install Tools on the Server:**
    Connect to your server via SSH and install Git and Docker.
    ```bash
    # Update package list
    sudo apt update
    # Install Git
    sudo apt install git -y
    # Install Docker (follow the official Docker guide for Ubuntu)
    ```

3.  **Clone Your Repository:**
    On the server, clone your project from GitHub.
    ```bash
    git clone https://github.com/ms584/Simple-To-Do-List-Manager.git
    cd Simple-To-Do-List-Manager
    ```

4.  **Run the Application:**
    Use Docker Compose to build and run your application in detached mode.
    ```bash
    docker compose up --build -d
    ```

5.  **Access Your Live Site:**
    Your To-Do List application is now live and accessible to anyone in the world via your server's public IP address:
    > **`http://<your_server_ip_address>`**