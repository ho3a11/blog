Django Blog Project

This is a Django-based blog project that allows users to create, view, edit, and delete blog posts. It includes features such as user authentication, pagination, and comment functionality.

Installation

Clone the repository:


     https://github.com/ho3a11/blog.git
   
Navigate to the project directory:


     cd blog
   
Create a virtual environment:

     python3 -m venv venv
   
Activate the virtual environment:
For macOS/Linux:


     source venv/bin/activate
For Windows:


     .\venv\Scripts\activate
Install the project dependencies:


     pip install -r requirements.txt
Apply the database migrations:


     python manage.py migrate
Create a superuser (admin) account:


     python manage.py createsuperuser
Start the development server:


     python manage.py runserver
Open your web browser and navigate to http://localhost:8000 to access the blog.

Docker

Alternatively, you can use Docker to run the project in a containerized environment. Follow these steps:

Install Docker on your machine by following the instructions in the official Docker documentation.

Build the Docker image:



     docker-compose build  .
Run the Docker container:



     docker-compose up
     
Open your web browser and navigate to http://localhost:8000 to access the blog.

Usage
To create a new blog post, click on the "New Post" button on the homepage and fill in the required details.

To view a blog post, click on its title on the homepage or in the post list.

To edit a blog post, click on the "Edit" button on the post detail page and make the desired changes.

To delete a blog post, click on the "Delete" button on the post detail page and confirm the deletion.

To add comments to a blog post, scroll to the bottom of the post detail page and enter your comment in the provided form.

Configuration

The project settings can be found in the settings.py file. You can modify settings such as the database configuration, static files, and email settings according to your needs.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License

This project is licensed under the MIT License.

Acknowledgements

The project uses the Django framework and various Django packages for its functionality.

Feel free to customize this README file based on your specific project requirements and add any additional sections or information that you find relevant.
