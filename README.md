# StudyCards Backend

The *StudyCards-backend* is the backend for the StudyCards application, built using Django Rest Framework. It has been designed for  ([StudyCards-frontend](https://study-cards-frontend-2200912dd99e.herokuapp.com/))<br>

# 📚 StudyCards - Backend Overview

The **StudyCards Backend** is a Django REST Framework application that powers the StudyCards flashcard learning platform.  
It provides a secure and scalable API for managing user accounts, flashcards, and review history.  
The backend handles user authentication, data validation, and database interactions, ensuring smooth functionality for all front-end operations.

---

## 🔧 Core Responsibilities
- **User Authentication**: Handles secure user registration, login, logout, and session management using tokens.
- **Flashcard Management**: Supports full CRUD (Create, Read, Update, Delete) operations for user-created flashcards.
- **Review Tracking**: Records users' review sessions, including scores and learning streaks, to help track progress over time.
- **API Provision**: Offers RESTful endpoints that are consumed by the StudyCards front-end.
- **Authorization**: Ensures users can only access and manipulate their own data.
- **Filtering and Pagination**: Provides filter options (e.g., by topic or status) and paginates flashcard/review history lists for efficiency.

---

## 🏛️ Main Components
- **Flashcard Model**: Stores flashcard questions, answers, topics, statuses, and timestamps.
- **ReviewHistory Model**: Tracks user review performance data such as score, total questions, correct answers, and streaks.
- **User Authentication**: Built with `dj-rest-auth`, `django-allauth`, and token-based authentication.
- **Custom Views**: ViewSets and API Views allow users to manage their flashcards and review history through intuitive endpoints.
- **Filtering**: Users can filter flashcards by topic or learning status, using `django-filters`.

---

## ⚙️ Technologies Used
- **Django** (Python Web Framework)
- **Django REST Framework** (API Layer)
- **PostgreSQL** (Production Database)
- **dj-rest-auth** (Authentication system)
- **django-cors-headers** (CORS support for front-end communication)
- **Heroku** (Deployment platform)
- **Gunicorn** and **Whitenoise** (for production server and static file management)


## Live Page
[StudyCards-backend]()

## Project Description

### Main goals


## Structure

The database schema was created with [dbdiagramm](https://dbdiagram.io/home)

## Database<br>
A PostgreSQL provided by Code Institute has been used as relational database.<br>

- **Relationships:**  
  - **User to Flashcard:** One-to-Many  
  - **User to ReviewSession:** One-to-Many  
  - **Flashcard to User:** Many-to-One  
  - **ReviewSession to User:** Many-to-One  

<br>

### 📚 Entity Relationship Overview

| **Entity**          | **Relation Type**         | **Description** |
|:--------------------|:---------------------------|:----------------|
| **User → Flashcard** | One user can create multiple flashcards. |
| **User → ReviewSession** | One user can have multiple review sessions recorded. |
| **Flashcard → User** | Each flashcard belongs to one user. |
| **ReviewSession → User** | Each review session is associated with one user. |

<br>

### 🔎 Additional Notes
- A user can **create, edit, and delete** their flashcards.
- A user can **review** flashcards and **record** performance via review sessions.
- Flashcards can be **filtered** by topic and learning status.
- ReviewSessions **track** the history of completed study sessions including score and streak.


A welcome message is displayed when you first enter the API site.

![Screenshot of welcome message](documentation/welcome_api.png)<br>

### Future Implementations

- **Spaced Repetition Algorithm:**  
  Implement intelligent flashcard scheduling based on the user's previous review performance using algorithms like SM-2 (used in Anki) to optimize memory retention.

- **User Statistics API:**  
  Provide additional API endpoints to deliver detailed analytics to users, such as learning streaks, mastery trends over time, flashcard creation rates, and review success percentages.

- **Decks and Flashcard Grouping:**  
  Allow users to create multiple decks (collections of flashcards) for better organization. Flashcards could be linked to decks through a ForeignKey, enabling deck-level filtering and review.


## API Endpoints

The endpoints provided by the StudyCards API are:

| Endpoint                            | HTTP Method | CRUD Operation |
|-------------------------------------|-------------|----------------|
| /api/auth/registration/             | POST        | Create (User Registration) |
| /api/auth/login/                    | POST        | Create (User Login) |
| /api/auth/logout/                   | POST        | Delete (User Logout) |
| /api/auth/user/                     | GET         | Read (Current User Details) |

| /api/flashcards/                    | GET         | Read (List Flashcards) |
|                                      | POST        | Create (Add New Flashcard) |
| /api/flashcards/\<int:id\>/          | GET         | Read (Flashcard Details) |
|                                      | PUT         | Update (Edit Flashcard) |
|                                      | DELETE      | Delete (Remove Flashcard) |

| /api/review-history/                | GET         | Read (List Review Sessions) |
|                                      | POST        | Create (Save Review Result) |
| /api/review-history/\<int:id\>/      | GET         | Read (Single Review Session) |
|                                      | PUT         | Update (Update Review Session) |
|                                      | DELETE      | Delete (Remove Review Session) |




## Testing

The app was tested regularly and deployed to Heroku to make sure both local and remote worked the same.

The manual tests were conducted to ensure that the API operates smoothly and behaves as intended.
<b>[Detailed manual testing is located here](/TESTING.md)</b>

### Browser Compatibility

  The tests were conducted using the following browser:

- Google Chrome

## Deployment

### Heroku

This site is deployed using Heroku and all the steps for a success deployment are on the following:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_.
2. Log in (or sign up) to Heroku.
3. Click on the _New_ button and select _Create new app_.
4. Give it a unique name and choose the region.
5. Click the Settings tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button.
6. Add all variables from env.py to _ConfigVars_ of Heroku.
7. Click the _Add_ button.
8. Click the Deploy tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button.
9. Search for the repository name on github and click the _Connect_ button.
10. Add in the setting.py the Heroku app URL into ALLOWED HOSTS.
11. Gather all static files of the project by using the command _python3 manage.py collectstatic_ in the terminal.
12. Make sure that DEBUG=FALSE in settings.py.
13. Create a _Procfile_ in the root directory and add web: gunicorn fv_api.wsgi.
13. In Heroku enable the automatic deploy or manually deploy the code from the main branch.

### Local deployment

1. Generate an env.py file in the root directory of the project.
2. Configure the environment variables within this file.
3. Create a virtual environment, if neccessary.
4. Install all required dependencies using _pip install_ command (into the .venv).
5. Add dependencies to the requirements.txt file using _pip3 freeze > requirements.txt_ command.

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [StudyCards-backend](https://github.com/KatVolkova/study-cards-backend)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1. Log in to GitHub.
2. Navigate to the repository for this project by selecting StudyCards-backend](https://github.com/KatVolkova/study-cards-backend)
3. In the top-right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

### Create PostgreSQL using Code Institute Database Maker
1. [CI Database Maker](https://dbs.ci-dbs.net/)
2. Input your email address
3. Paste the provided URL in as your DATABASE_URL value

## Credits

## Technologies Used

### Languages:
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Tools:
- [Git](https://git-scm.com/) Used in Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) Used to store file for the project.
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) Used for Agile sprint planning and task tracking.
- [Heroku](https://www.heroku.com) Used to deploy application.
- [Code Insitute Database Maker](https://dbs.ci-dbs.net/) PostgreSQL database.
- [Grammarly](https://app.grammarly.com/ ) - has been used for spell-checking 
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools?hl=de) Used to check the application for responsiveness and errors. 
- [VS Code](https://code.visualstudio.com/)

### Frameworks:  
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))

### Libraries and modules:
- [os](https://docs.python.org/3/library/os.html) Provides functions to interact with the operating system. 
- [datetime](https://docs.python.org/3/library/time.html) Supplies classes for manipulating dates and times.
- [Gunicorn](https://gunicorn.org/) Provides a way to serve Python web applications.
- [Pycopg 2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter for Python.
- [sqlparse](https://pypi.org/project/sqlparse/): A non-validating SQL parser for Python.
- [dj_database_url](https://pypi.org/project/dj-database-url/) Enables the ability to represent their database settings via a string.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/): Handle Cross-Origin Resource Sharing in Django.
- [django-filter](https://pypi.org/project/django-filter/): Provides filtering with URL parameters for querysets.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/): Used to handle user registration, login, and logout.
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html): JSON Web Token authentication for Django REST Framework.
- [oauthlib](https://oauthlib.readthedocs.io/en/latest/): A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/): JSON Web Token implementation in Python.
- [python3-openid](https://pypi.org/project/python3-openid/): A library for implementing OpenID in Python.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/): OAuth library that implements the client side of the OAuth protocol.
- [dj-database-url](https://pypi.org/project/dj-database-url/): A simple utility to allow using Database URLs in Django.
- [whitenoise](https://whitenoise.readthedocs.io/en/latest/): A Django middleware to serve static files.


### References

- [Stackoverflow](https://stackoverflow.com/) - used for general code advice
- [ChatGPT](https://openai.com/index/chatgpt/) - For general debugging along with other tools and coding advice