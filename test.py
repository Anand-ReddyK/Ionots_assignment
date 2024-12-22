from django.contrib.auth.models import User
from core.models import Project

# Create sample users
user1 = User.objects.create_user(username='john_doe', email='john@example.com', password='password')
user2 = User.objects.create_user(username='jane_doe', email='jane@example.com', password='password')

# Create some sample projects
project1 = Project.objects.create(
    title='Project 1',
    description='Description for project 1',
    assigned_to=user1,
    status='Pending',
    deadline='2024-12-30 12:00:00'
)

project2 = Project.objects.create(
    title='Project 2',
    description='Description for project 2',
    assigned_to=user1,
    status='Accepted',
    deadline='2024-12-25 15:00:00'
)

project3 = Project.objects.create(
    title='Project 3',
    description='Description for project 3',
    assigned_to=user2,
    status='Completed',
    deadline='2024-12-20 18:00:00'
)

print('Sample projects created successfully.')
