# Google Cloud Summit 2026 — Conference Website

> A single-day technical conference informational site built with **Python + Flask** on the server and vanilla **HTML / CSS / JavaScript** on the front end.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Quick-Start (5 minutes)](#quick-start)
4. [Running the App](#running-the-app)
5. [Features & Functionality](#features--functionality)
6. [Pages & Routes](#pages--routes)
7. [Customising the Data](#customising-the-data)
8. [Customising the Design](#customising-the-design)
9. [Extending the App](#extending-the-app)
10. [Troubleshooting](#troubleshooting)

---

## Project Structure

```
conference-site/
├── app.py               ← Flask application — routes, API, error handlers
├── data.py              ← All conference data (talks, speakers, schedule, event info)
├── requirements.txt     ← Python dependencies
├── templates/
│   ├── index.html       ← Home page (hero, schedule, talks grid, speakers)
│   ├── talk.html        ← Individual talk detail page
│   └── 404.html         ← Custom 404 error page
└── static/
    ├── css/
    │   └── style.css    ← Complete dark-theme stylesheet
    └── js/
        └── main.js      ← Live search, filter, scroll animations
```

---

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python      | 3.9 +   |
| pip         | any     |

No Node.js, no bundlers, no build step required.

---

## Quick-Start

### 1 — Clone / navigate to the project directory

```powershell
cd C:\Users\gabys\.gemini\antigravity\scratch\conference-site
```

### 2 — Create a virtual environment (recommended)

```powershell
python -m venv venv
venv\Scripts\activate      # Windows PowerShell
# OR
source venv/bin/activate   # macOS / Linux
```

### 3 — Install dependencies

```powershell
pip install -r requirements.txt
```

### 4 — Run the development server

```powershell
python app.py
```

### 5 — Open in browser

```
http://127.0.0.1:5000
```

---

## Running the App

### Development mode (default)

```powershell
python app.py
```

Flask runs with `debug=True` on port **5000**. Hot-reload is active — saving any `.py` file automatically restarts the server.

### Custom port

```powershell
flask run --port 8080
```

### Production (Gunicorn, Linux/macOS only)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## Features & Functionality

| Feature | Description |
|---------|-------------|
| **Home page** | Hero banner with event date, location, and time. Live "today" date display. |
| **Stats bar** | Quick-glance numbers: 8 talks, 10 speakers, 2 categories, 1 day. |
| **Visual timeline** | Full day schedule from 09:00 to 18:30 with colour-coded sessions, breaks, and a 60-minute lunch break. |
| **Talk cards grid** | All 8 talks displayed as interactive cards with category badge, time, room, description, and speakers. |
| **Live search** | Type in the search box to instantly filter talks by **title**, **speaker name**, or **description**. No page reload. |
| **Category filter** | Click "Infrastructure & DevOps" or "AI & Data" pill to filter both the cards grid and the timeline. |
| **Keyboard shortcut** | Press `/` anywhere on the page to jump the cursor into the search box. Press `Esc` to exit. |
| **Talk detail pages** | Each talk has its own page (`/talk/<ID>`) with full description and speaker profiles. |
| **Speaker grid** | All 10 speakers displayed with avatar, title, company, and LinkedIn link. |
| **JSON search API** | `GET /api/search?q=<query>&category=<1|2>` — returns filtered talks as JSON. |
| **Custom 404 page** | Friendly error page for invalid routes. |
| **Fully responsive** | Works on desktop, tablet, and mobile. |
| **Scroll animations** | Cards and stats fade in as they enter the viewport. |

---

## Pages & Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page (hero + schedule + talks + speakers) |
| `/talk/<talk_id>` | GET | Individual talk detail (e.g. `/talk/T001`) |
| `/api/search` | GET | JSON search/filter API |

### API Usage Example

```
GET /api/search
GET /api/search?q=kubernetes
GET /api/search?category=2
GET /api/search?q=vertex&category=2
```

**Response:**

```json
{
  "count": 2,
  "results": [
    {
      "id": "T002",
      "title": "Vertex AI in Production: ...",
      "category": 2,
      "category_name": "AI & Data",
      "time_start": "10:00",
      "time_end": "10:45",
      "room": "Hall A",
      "description": "...",
      "speakers": [
        {
          "id": "sp3",
          "name": "Yuna Kim",
          "title": "ML Engineer",
          "company": "DeepMind",
          "linkedin": "https://www.linkedin.com/in/yunakim",
          "avatar_initials": "YK",
          "avatar_color": "#FBBC04"
        }
      ]
    }
  ]
}
```

---

## Customising the Data

All conference content lives in **`data.py`**. No database required — everything is plain Python dicts and lists.

### Change event details

Edit the `EVENT` dict at the top of `data.py`:

```python
EVENT = {
    "name": "Your Conference Name",
    "tagline": "Your tagline here",
    "date": "Wednesday, September 15, 2027",
    "location": "ExCeL London, London, UK",
    "address": "Royal Victoria Dock, 1 Western Gateway, London E16 1XL",
    ...
}
```

### Add or edit a speaker

Add a new dict to the `SPEAKERS` list:

```python
{
    "id": "sp11",                          # must be unique
    "first_name": "Alice",
    "last_name": "Wong",
    "title": "Staff Engineer",
    "company": "Google",
    "linkedin": "https://www.linkedin.com/in/alicewong",
    "avatar_initials": "AW",
    "avatar_color": "#009688",             # any hex colour
},
```

### Add or edit a talk

Add a new dict to the `TALKS` list:

```python
{
    "id": "T009",                          # must be unique
    "title": "Cloud Spanner Deep Dive",
    "category": 1,                         # 1 = Infrastructure & DevOps, 2 = AI & Data
    "speaker_ids": ["sp1"],                # list of speaker ids (1 or 2)
    "time_start": "17:15",
    "time_end": "18:00",
    "duration_min": 45,
    "description": "Full description...",
    "room": "Hall A",
},
```

Then add the corresponding entry in `SCHEDULE`:

```python
{"type": "session", "talk_id": "T009", "time_start": "17:15", "time_end": "18:00"},
```

### Add a new category

Edit the `CATEGORIES` dict:

```python
CATEGORIES = {
    1: "Infrastructure & DevOps",
    2: "AI & Data",
    3: "Databases & Analytics",   # new category
}
```

> **Important:** If you add a category, also update `style.css` to add `.cat-badge.cat-3`, `.connector-dot.cat-3`, and `.cat-border-3` rules (copy the existing `cat-1` or `cat-2` blocks and change the colour).

---

## Customising the Design

All styles are in **`static/css/style.css`**.

### Change the colour palette

Edit the CSS custom properties at the top of the file under `:root { ... }`:

```css
:root {
  --blue:   #4285F4;   /* Primary brand blue */
  --green:  #34A853;   /* Secondary brand green */
  --yellow: #FBBC04;   /* Accent yellow */
  --red:    #EA4335;   /* Accent red */

  --bg-0:   #09090f;   /* Darkest background */
  --bg-1:   #111118;
  --bg-2:   #17171f;
  --bg-3:   #1e1e28;
  ...
}
```

### Change the font

The site uses **Google Sans** (loaded from Google Fonts). To swap:

1. Replace the `<link>` tags in the `<head>` of each template.
2. Update `font-family` in the `body` rule in `style.css`.

---

## Extending the App

### Add a registration form

1. Create a `POST /register` route in `app.py`.
2. Add a form to `index.html`.
3. Optionally store registrations in a SQLite database using `sqlite3` (built-in) or Flask-SQLAlchemy.

### Add a database

Replace the Python dicts in `data.py` with SQLAlchemy models:

```bash
pip install flask-sqlalchemy
```

### Add authentication (speaker portal)

Use `flask-login` and `flask-bcrypt` for a simple admin login.

### Deploy to Google Cloud Run

```bash
# Build a container image
gcloud builds submit --tag gcr.io/YOUR_PROJECT/conference-site

# Deploy
gcloud run deploy conference-site \
  --image gcr.io/YOUR_PROJECT/conference-site \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` (ensure your venv is activated) |
| `Address already in use` on port 5000 | Change port: `python app.py` uses 5000; edit `app.py` last line to `port=5001` or kill the process using the port |
| Fonts not loading | Check your internet connection — fonts are loaded from `fonts.googleapis.com` |
| Search not filtering | Open browser DevTools console for JS errors; check that `static/js/main.js` is loading (Network tab) |
| Changes to `data.py` not showing | Flask dev server auto-reloads on `.py` changes — wait ~1 second or hard-refresh the browser (`Ctrl+Shift+R`) |

---

## Tech Stack Summary

| Layer | Technology |
|-------|-----------|
| Server | Python 3.9+, Flask 3 |
| Templating | Jinja2 (bundled with Flask) |
| Styling | Vanilla CSS (dark glassmorphism, CSS custom properties) |
| Typography | Google Fonts — Google Sans, Roboto Mono |
| JavaScript | Vanilla ES6+ (no frameworks, no bundler) |
| Data | Python dicts/lists in `data.py` (no database) |

---

*Built for Google Cloud Summit 2026 — © 2026*
