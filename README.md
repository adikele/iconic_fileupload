# iconic_fileupload
A programming assignment for file uploads using Django Rest Framework

# Current status:
This program provides a dockerized container for uploading files.
Uploaded files can be seen in the media folder.
Post Endpoint:
http://127.0.0.1:8000/document/upload_iconic/

# ToDo:
1. Create account fields for users and organizations.
2. Create session-based authentication for users.
3. Associate the file uploading process with a (logged-in) user.
4. Provide functionality for downloading files.

# Description of Assignment:
A web application that provides a REST API for logged-in users to upload and download any kind of files. The users must be able to login and logout (use either token or session authentication). There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script or via the admin interface instead. Each user and file must belong to an organization. Once uploaded, the file must belong to the same organization as the user who uploaded it. 
Users should see and be able to download any of the uploaded files from any organization. Write an endpoint for listing all the files that belong to one organization, and also an endpoint for listing all the file downloads done by one user. Include timestamps when the file was uploaded and when the user downloaded a file. There could also be endpoints for listing all the organizations and all users for convenience. Keep track of how many times each file has been downloaded, and also how many total file downloads each organization has (number of all file downloads from that organization). Include the number of downloads when listing files and organizations. 
Use Docker, Docker Compose, Django and Django REST Framework (https://www.django-rest-framework.org/). You can use a database of your choice. Implementing a simple UI with React is a bonus.

