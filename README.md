# Ionots - Project Assignment and Progress Tracking System

The goal of the project was to develop a backend system to manage project assignments, track progress, and calculate scores based on task completion. This system allows candidates to view, accept, and track their assigned projects in real time.

## 1. Project Assignment
### Backend:
- Created models for projects and tasks, where each project is assigned to a user.
- Implemented the ability to view, accept, and track the status of projects.
- The project statuses include "Pending", "Accepted", and "Completed".
- Users can see detailed project descriptions, deadlines, and their current status.

### Frontend:
- Designed user-friendly pages using Tailwind CSS to display projects with their details.
- Added functionality to accept or view project details, with a clear status indicator.

### The Projects Page
![127 0 0 1_8000_projects_](https://github.com/user-attachments/assets/239e5018-4937-4f49-8501-6425060ec06d)


## 2. Progress Tracking and Scoring System
### Backend:

- Implemented a system to track the progress of a project based on the completion of its tasks.
- Each task has a "Completed" or "Pending" status, and when all tasks are completed, the project status is updated to "Completed".
- The progress percentage is dynamically calculated and displayed on the frontend.
- Added a scoring mechanism based on task completion to track performance.

### Frontend:

- Displayed project progress with a percentage bar showing the completion status of tasks.
- Used conditional styling to show completed tasks in green.
- Displayed total score and the score obtained based on completed tasks.

### The Progress Page of a Project
![127 0 0 1_8000_projects_3_progress_](https://github.com/user-attachments/assets/a5b98c53-d0c4-4149-acb9-ba8cb82b9134)

### The Project page
![127 0 0 1_8000_projects_3_](https://github.com/user-attachments/assets/ac51fc2c-6ae2-4b19-a617-198e5ae1d632)

## Future Improvements:
- **Task Deadlines:** Add deadlines for individual tasks to further enhance project management.
- **Role-based Access Control:** Implement permissions to ensure that only authorized users can create new projects. This will help maintain control over who has the ability to initiate projects within the system.
- **Ownership-based Task Management:** Restrict task creation to the user who initially created the project. This ensures that only the project owner can manage and add tasks, preserving the integrity of the project’s structure and tasks.
