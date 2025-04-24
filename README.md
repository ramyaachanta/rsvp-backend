
# RSVP Backend 🔧

This is the backend service for the **RSVP Manager** web application. It powers the RSVP submission flow, supports bulk submissions, provides RSVP stats, and manages data persistence using Flask and PostgreSQL.

---

## 🚀 Features

- ✅ Add or update individual RSVP entries
- 📥 Bulk RSVP submission
- 📊 Retrieve RSVP counts (Yes/No/Total)
- 👥 List all RSVPs or only confirmed attendees
- ❌ Delete RSVP entries by ID
- 🔄 CORS enabled for seamless frontend integration

---

## 🛠️ Tech Stack

- **Backend Framework:** Flask (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Environment Management:** `os.getenv` for secure credentials
- **CORS Support:** Flask-CORS

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ramyaachanta/rsvp-backend.git
   cd rsvp-backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   - Update your PostgreSQL credentials in the environment or directly in the `app.config` line:
     ```python
     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost:5432/rsvp_db"
     ```

5. **Initialize the database**
   ```bash
   python app.py
   ```
   On first run, the tables will be created automatically via `db.create_all()`.

6. **Run the server**
   ```bash
   python app.py
   ```

---

## 📁 Folder Structure

```
rsvp-backend/
├── app.py               # Main application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📬 API Endpoints

### `POST /api/rsvp`
Add or update an RSVP entry  
**Payload:**
```json
{
  "id": "player1",
  "name": "John Doe",
  "status": "Yes"
}
```

### `POST /api/rsvp/bulk`
Submit multiple RSVP entries at once  
**Payload:**
```json
{
  "entries": [
    {"id": "p1", "name": "Alice", "status": "Yes"},
    {"id": "p2", "name": "Bob", "status": "No"}
  ]
}
```

### `GET /api/rsvp`
Fetch all RSVPs

### `GET /api/rsvp/confirmed`
Fetch only confirmed (Yes) RSVPs

### `GET /api/rsvp/counts`
Get RSVP statistics (total, confirmed, declined)

### `DELETE /api/rsvp/<id>`
Delete RSVP by ID

---

## 🧠 Notes

- Status must be one of: `"Yes"`, `"No"`, or `"Maybe"`
- Player `id` must be unique
- CORS is enabled for local development with frontend

---

## 📬 Contact

For any questions or suggestions:

**Ramya Sri Achanta**  
📧 [ramyaachanta@gmail.com](mailto:ramyaachanta@gmail.com)  
🌐 [Portfolio](https://ramyaachanta.github.io/Portfolio/)  
🔗 [LinkedIn](https://www.linkedin.com/in/ramyaachanta)

---

## 📄 License

This project is licensed under the MIT License.
