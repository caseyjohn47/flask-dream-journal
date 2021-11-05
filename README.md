# Flask Dream Journal
## Casey Lewis

This is my dream journal project for IMM 230: Dynamic Web Applications.

It is based on the Flask Mega-Tutorial by Miguel Grinberg.

## Progress Journal

### SESSION ONE (10/21)

So far, I have found this project fascinating. The combination of flask, python and Jinja2 can do some
amazing things that I had no idea about. It is able to accomplish so much with minimal lines of code.
This session I finished chapters 1-3 of the tutorial (startup, templates, and login).

### SESSION TWO (10/28)

Working with databases was very interesting. The article was super helpful for explaining how they work
and the pros + cons of different types of databases. This session I finished chapter 4 of the tutorial (databases).

### SESSION THREE (10/29)

Worked on login and registration functionalities. This was a lot more complicated and complex than anything
covered in the previous chapters. This session I finished chapter 5 of the tutorial (User Logins).

### SESSION FOUR (10/29)

Worked on submitting new entries for the dream journal. I am now able to submit a new entry using the form.
I did this using material from chapter 6 of the tutorial (Profile Page and Avatars).

### SESSION FIVE (11/1)

Finished functionality allowing the user to delete and edit notes. I learned how to do this using multiple
online resources rather than the Flask Mega Tutorial. This was interesting to learn how to manipulate the
database using different methods in the routes.db.

### SESSION SIX (11/2)

Implemented profile pages, an about me section for every user, and a community page.
Now, the user can open their own profile page and edit their about me. They can also go to the community page 
and view every user in the system.Lastly, they can click on any user on the community page and view their profile.
Every profile page includes the username, an about me section and their dream journal. This was a fun extension and
I felt that I learned a lot about the system while doing this. This also helped me prove to myself that I was
learning the material and not simply following a tutorial because I did this entirely on my own without any help from
online resources. With this, I have completed all of the functionality that I was planning to. Now, all I have left
to do is style the application and add my comments throughout the project.

## To Do List

- Add comments within the code detailing the project
- Style the application. It looks ugly right now

## Installing This Project

- Download the project
- Change your terminal working directory to the new project folder
- Create virtual environment: 'python3 -m venv venv'
- Activate the environment: 'source venv/bin/activate'
- Install the requirements: 'pip install -r requirements.txt'
- Initialize the database: 'flask db init'
- Run the first migration: 'flask db migrate -m "initialize"'
- Upgrade the database: 'flask db upgrade'
- Run the program: 'flask run'
