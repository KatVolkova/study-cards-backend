Return to the [project name README.md](README.md).
# Testing

## Index


## Python Validator Testing

- All created python files were checked with the [Code Insitute validator - CI Python Linter](https://pep8ci.herokuapp.com/#). <br>

### Manual Testing (Backend)

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| User Registration | POST to `/api/auth/registration/` with valid data | 201 Created, user account created in DB | As expected |
| User Registration (Invalid) | POST to `/api/auth/registration/` with invalid data | 400 Bad Request with validation errors | As expected |
| User Login | POST to `/api/auth/login/` with correct credentials | 200 OK, returns Token | As expected |
| User Login (Invalid) | POST to `/api/auth/login/` with wrong password | 400 Bad Request with error message | As expected |
| Flashcard Create | POST to `/api/flashcards/` with Token | 201 Created, flashcard saved in DB linked to user | As expected |
| Flashcard Read | GET `/api/flashcards/` with Token | 200 OK, returns user’s flashcards | As expected |
| Flashcard Update | PUT `/api/flashcards/<id>/` with Token | 200 OK, updates flashcard | As expected |
| Flashcard Delete | DELETE `/api/flashcards/<id>/` with Token | 204 No Content, flashcard deleted | As expected |
| Review History Save | POST `/api/review-history/` with review data | 201 Created, record saved in DB | As expected |
| Review History Read | GET `/api/review-history/` | 200 OK, list of user’s past review sessions | As expected |
| Unauthorized Access | Try to POST/GET without token | 401 Unauthorized error | As expected |


## Bugs

| **Bug Number** | **Description**                                         | **Cause**                                              | **Solution**                                           |
|----------------|----------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| 1              | Registration form failed when missing email field        | Email was marked as required in backend but validation was unclear | Improved serializer error handling and clarified form validation rules |
| 2              | Login form accepted incorrect credentials silently       | Backend did not return proper error response for wrong credentials | Added error catching and displayed clear authentication error messages |
| 3              | Flashcards API allowed unauthenticated access             | Missing permission classes on flashcard endpoints       | Applied `IsAuthenticated` permission to FlashcardViewSet to restrict access |