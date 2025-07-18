# 📘 Design & Setup Guide – Paragraph Word Search API 

A RESTful API to submit paragraphs, tokenize and index words, and search for paragraphs containing specific words. Built using Django REST Framework, PostgreSQL, JWT Authentication, and Docker.

---

## 📐 Design Overview

### 🧱 Architecture

- **Users**: Custom user model with `UUID`, `name`, `email`, `dob`, `created_at`, `modified_at`
- **Authentication**: JWT-based login and token verification (via SimpleJWT)
- **Paragraphs**:
  - Input text is split into paragraphs using **two newline characters**
  - Each paragraph is saved with a UUID and linked to the user
- **Word Indexing**:
  - Tokenize by whitespace
  - Lowercase all words
  - Map and store `word → paragraph` in the `WordIndex` table
- **Search**:
  - Returns top 10 most recent paragraphs where a word appears
- **Docs**:
  - Postman collection (`CodeMonk_Assignment.postman_collection.json`)
---

## 🐳 How to Run (Docker)
Running the Project with Docker
The entire app is containerized using Docker and docker-compose so you don’t need to install PostgreSQL or manage a virtualenv manually.

### ⚙️ Prerequisites

- Docker
- Docker Compose

---

### 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/Dhanush0724/CodeMonk_Assignment-.git
cd CodeMonk_Assignment-

```

### 📦 Step 2: Build & Start Docker Containers

In your terminal, run:

```bash
docker-compose build
docker-compose up
```

This will:
🐳 Build the Django app Docker image
🐘 Start a PostgreSQL container
🚀 Launch your app at: http://localhost:8000/

### 📦 Step 3: Run Migrations
Open a new terminal window and run:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
## 🚀 API Endpoints

| Method | Endpoint               | Description                          |
|--------|------------------------|--------------------------------------|
| POST   | `/api/register/`       | Register a new user                  |
| POST   | `/api/login/`          | Login and get JWT tokens             |
| POST   | `/api/paragraphs/`     | Submit multiple paragraphs           |
| GET    | `/api/search/?word=x`  | Search top 10 paragraphs for word    |

## 📘 Postman Support

Import CodeMonk_Assignment.postman_collection.json into Postman
✅ Steps to follow:
1. Register a user using `/api/register/`
2. Login using `/api/login/` to get an access token
3. Use the access token in the `Authorization` header for all protected routes:
   `Authorization: Bearer <your_access_token>`
4. Submit paragraphs using `/api/paragraphs/`
5. Search for a word using `/api/search/?word=example`

⚠️ If you get a 401 Unauthorized error, your token has likely expired — login again to get a new one.


# Includes:

  Register
  
  Login (JWT)
  
  Submit Paragraphs
  
  Search Words


### ✅ Final Submission Checklist

 Dockerized application
 
 JWT-based authentication
 
 Full-text indexing and word search
 
 Postman documentation
 
 .env for config
 
 README with complete setup instructions
