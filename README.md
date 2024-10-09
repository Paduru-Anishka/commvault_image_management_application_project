# commvault_image_management_application_project 

Image Management Application

A simple cloud-based web application that allows users to upload, list, and download images from an AWS S3 bucket. The app is built using Flask and interacts with AWS services via Boto3.

Features

Upload Images: Users can upload images to the S3 bucket through a user-friendly interface.

List Images: Users can view a list of uploaded images stored in the S3 bucket.

Download Images: Users can download images from the S3 bucket.


Prerequisites

AWS Account: Ensure you have an AWS account.

Python 3.x installed on your machine.

AWS CLI configured with your credentials:

aws configure


Setup Instructions

1. Clone the Repository:

git clone <repository-url>
cd image-management-app


2. Install Dependencies: Install the required Python libraries by running:

pip install Flask boto3


3. Configure AWS S3:

Create an S3 bucket in your AWS account.

Update the BUCKET_NAME variable in the code with your S3 bucket name.



4. Run the Application: Start the Flask server by running the following command:

python app.py


5. Access the Application:

Visit http://localhost:5000/ to upload images.

Visit /list to view and download the uploaded images.




Project Structure

.
├── app.py              # Main Flask application
├── templates
│   ├── upload.html     # HTML page for image upload
│   └── list.html       # HTML page for listing and downloading images
└── README.md           # Project documentation

AWS Permissions

Make sure your AWS credentials have appropriate permissions to:

Upload files to the S3 bucket

List objects in the S3 bucket

Download files from the S3 bucket



---
