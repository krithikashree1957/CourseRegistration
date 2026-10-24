# Course Registration System — CI/CD Assignment

## Project Overview

The Course Registration System is a Flask-based web application developed and maintained using Git, Docker, Jenkins, and automated testing with pytest. The project demonstrates version-controlled development, continuous integration, Docker image publishing, and deployment of multiple application versions.

## Author and Repositories

- **Author:** Krithika Shree K
- **GitHub Repository:** https://github.com/krithikashree1957/CourseRegistration
- **Docker Hub Repository:** https://hub.docker.com/r/krithika2013/course-registration/tags

## Technology Stack

- Python 3.12
- Flask
- HTML
- pytest
- Git and GitHub
- Docker
- Jenkins
- PowerShell

## Application Versions

### V1 — Course Management

- Displays available courses.
- Allows users to add courses.
- Provides the initial version of the Course Registration System.

**Local URL:** http://localhost:5000

**Docker Image:** `krithika2013/course-registration:v1`

### V2 — Student Course Registration

- Retains the course management functionality.
- Allows students to register for available courses.
- Displays current registrations, including registration ID, student name, and course.
- Includes automated tests for the application's functionality.

**Local URL:** http://localhost:5002

**Docker Image:** `krithika2013/course-registration:v2`

### V3 — View All Registrations

- Introduces a dedicated page to view student registrations.
- Displays registration IDs, student names, and course names in a table.
- Provides a link to return to the main course registration page.
- Includes a dedicated route at `/registrations`.

**Local URL:** http://localhost:5003/registrations

**Docker Image:** `krithika2013/course-registration:v3`

## Automated Testing

The project uses pytest to verify application functionality.

The test suite covers:

- Home page loading
- Adding a course
- Health endpoint
- Student registration
- Viewing all registrations

**Latest recorded V3 test result:** 5 tests passed.

Run the tests from the project directory using:

```powershell
python -m pytest -v
```

## Docker

Docker images are built with version-specific tags to distinguish V1, V2, and V3.

Pull an image using:

```powershell
docker pull krithika2013/course-registration:v1
docker pull krithika2013/course-registration:v2
docker pull krithika2013/course-registration:v3
```

Run V1, V2, or V3 individually using the appropriate image and port mapping:

```powershell
docker run -d --name course-registration-v1 -p 5001:5000 krithika2013/course-registration:v1
docker run -d --name course-registration-v2 -p 5002:5000 krithika2013/course-registration:v2
docker run -d --name course-registration-v3 -p 5003:5000 krithika2013/course-registration:v3
```

If a container with the same name already exists, remove or rename that container before running the command again. Ensure the required host ports are available.

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates the following tasks:

1. Checks out the source code from GitHub.
2. Installs Python dependencies.
3. Runs automated tests using pytest.
4. Builds the Docker image with the appropriate version tag.
5. Authenticates with Docker Hub using Jenkins credentials.
6. Pushes the versioned Docker image to Docker Hub.

The pipeline should be configured to use the corresponding Git branch and Docker tag for each version.

## Project Structure

```text
CourseRegistration/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── templates/
│   ├── index.html
│   └── registrations.html
└── README.md
```

## How to Run Locally

1. Clone the repository:

   ```powershell
   git clone https://github.com/krithikashree1957/CourseRegistration.git
   cd CourseRegistration
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Run the application:

   ```powershell
   python app.py
   ```

4. Open http://localhost:5000 in a browser.

5. Run automated tests:

   ```powershell
   python -m pytest -v
   ```

## Conclusion

This project demonstrates incremental application development across three versions, automated testing, source control, containerization, and a Jenkins-based CI/CD workflow. The GitHub repository provides access to the source code, while Docker Hub provides the published versioned images for evaluation.

---

**Author:** Krithika Shree K