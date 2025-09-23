# Full-Stack To-Do List Application

This is a complete full-stack web application featuring a modern frontend, a robust backend, and a fully containerized deployment environment using Docker. The application allows users to create, view, update, and delete tasks in a clean, responsive interface.

---

## Live Demo

**Check out the live application hosted on Render:**

**[https://simple-to-do-list-manager-kp87.onrender.com](https://simple-to-do-list-manager-kp87.onrender.com)**

*Note: The free tier on Render may cause the backend to "spin down" after 15 minutes of inactivity. The first request might take 30-60 seconds to "wake up" the service.*

---

## Application Preview

![Screenshot of the To-Do List Application](https://github.com/user-attachments/assets/3fbe6585-0f80-41cb-8972-272706b7a901)


---

## Features

*   **Modern Frontend:** A clean, responsive user interface built with **React**.
*   **Robust Backend:** A powerful and fast API built with **Python** and **FastAPI**.
*   **Persistent Storage:** Tasks are saved in a `tasks.json` file, with data persistence handled by Docker volumes for local development.
*   **Containerized:** The entire application stack is containerized with **Docker** and orchestrated with **Docker Compose** for easy, reproducible deployments.
*   **Secure:** Built with security in mind, leveraging modern framework features to protect against common vulnerabilities like XSS and invalid data injection.
*   **Tested:** Includes a complete test suite for the backend API using **Pytest**.

---

## Tech Stack

*   **Frontend:** React (Web GUI)
*   **Backend:** Python 3.9, FastAPI, Pydantic, Uvicorn
*   **Web Server/Proxy:** Nginx
*   **Containerization:** Docker & Docker Compose
*   **Testing:** Pytest, Node.js (for security script)
*   **Deployment:** Render

---

## Project Structure

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


---

## Local Development Setup

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   **Docker & Docker Compose:** The only essential requirement.
    *   [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   **Node.js & npm:** Required *only* for running the security test script.
    *   [Install Node.js](https://nodejs.org/)
*   **Git:** For cloning the repository.
    *   [Install Git](https://git-scm.com/downloads)

### Installation & Running

Running this application locally is incredibly simple thanks to Docker.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ms584/Simple-To-Do-List-Manager.git
    cd Simple-To-Do-List-Manager
    ```

2.  **Build and run the containers:**
    This single command builds the images, creates the containers, and starts the application.
    ```bash
    docker compose up --build
    ```
    *   Add the `-d` flag (`docker compose up --build -d`) to run the containers in the background.

3.  **Access the application:**
    Once the containers are running, open your web browser and navigate to:
    > **`http://localhost`**

To stop the application, press `Ctrl+C` in the terminal. If running in the background, use `docker compose down`.

---

## Testing

The project includes a full suite of tests for the backend API and a security scanning script.

### Backend API Tests (Pytest)

The most reliable way to run tests is inside the Docker container to ensure the environment is identical to production.

1.  **Ensure the application is running:**
    ```bash
    docker compose up -d
    ```

2.  **Execute the tests inside the backend container:**
    ```bash
    docker compose exec backend pytest
    ```

### Security Vulnerability Scan

This script tests the API for common vulnerabilities like XSS and malformed JSON payloads.

1.  **Ensure the application is running:**
    ```bash
    docker compose up -d
    ```

2.  **Install script dependencies (first time only):**
    ```bash
    npm install
    ```

3.  **Run the security test:**
    ```bash
    node scripts/comprehensive-security-test.js
    ```

---

## Deployment

This application was deployed using **Render's** free tier. The process leverages the containerized nature of the project for a smooth deployment.

1.  **Push to GitHub:** Ensure your latest code is on the `main` branch of your GitHub repository.
2.  **Deploy the Backend on Render:**
    *   Create a new **Web Service**.
    *   Set the **Environment** to **Docker**.
    *   Set the **Root Directory** to `backend`.
    *   Render will build the `Dockerfile` and deploy the service, providing a public URL (e.g., `https://my-backend.onrender.com`).
3.  **Deploy the Frontend on Render:**
    *   Create a new **Static Site**.
    *   Set the **Root Directory** to `frontend`.
    *   Set the **Build Command** to `npm run build` and the **Publish Directory** to `build`.
    *   Add an **Environment Variable** with the key `REACT_APP_API_URL` and the value set to your backend's URL with `/api` appended (e.g., `https://my-backend.onrender.com/api`).
    *   Render will deploy the static site, giving you the final public URL.

---

## License

This project is open source and available under the [MIT License](LICENSE).