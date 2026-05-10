# AI Resume Builder

A full-stack AI-powered resume builder with React frontend and FastAPI backend.

## Project Structure

```
AI-Resume-Builder/
├── frontend/          # React + Vite + Tailwind CSS
│   ├── src/
│   │   ├── components/
│   │   ├── pages/     # Landing, Login, Dashboard, etc.
│   │   ├── hooks/     # useAuth
│   │   ├── lib/       # supabaseClient
│   │   └── services/  # API service
│   ├── .env           # Frontend environment variables
│   └── package.json
└── backend/           # FastAPI
    ├── main.py        # FastAPI app with routes
    ├── skill_gap.py   # Skill gap analysis logic
    ├── jd_matcher.py  # JD matching logic
    ├── resume_engine.py # PDF/DOCX generation
    ├── llm_service.py # Groq API integration
    ├── .env           # Backend environment variables
    └── requirements.txt
```

## Features

- **Resume Builder**: Create professional resumes with PDF/DOCX export
- **Skill Gap Analysis**: Analyze resume against job requirements
- **JD Matcher**: Match resumes with job descriptions and suggest projects
- **AI Learning Roadmap**: Generate personalized learning plans using Groq API
- **Authentication**: Supabase-based user authentication

## Setup Instructions

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Supabase account (for authentication)
- Groq API key (for AI features)

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables in `.env`:
   ```
   VITE_SUPABASE_URL=your_supabase_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. Start development server:
   ```bash
   npm run dev
   ```

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_service_key
   SUPABASE_JWT_SECRET=your_supabase_jwt_secret
   GROQ_API_KEY=your_groq_api_key
   FRONTEND_URL=http://localhost:5173
   ```

4. Start FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Health Check
- `GET /health` - Check server status

### Resume Operations
- `POST /api/resume/create` - Create a new resume
- `POST /api/resume/download-pdf` - Download resume as PDF
- `POST /api/resume/download-docx` - Download resume as DOCX
- `GET /api/resumes/me` - Get user's resumes

### Analysis Features
- `POST /api/skill-gap/analyze` - Analyze skill gaps
- `POST /api/jd-matcher/analyze` - Match with job descriptions

## Design System

### Colors
- **Charcoal**: `#272727` - Primary text
- **Olive**: `#7d9b76` - Primary brand color
- **Cream**: `#f5f5e9` - Background

### Typography
- **Font**: Montserrat (Google Fonts)
- **Weights**: 400, 500, 600, 700, 800

### Components
- **Navbar**: Fixed, blurred background, dark theme
- **Cards**: White background, rounded corners, subtle shadow
- **Buttons**: Olive background, rounded, Montserrat font

## Development Notes

- All backend files are complete and runnable
- Frontend uses placeholder pages that will be implemented next
- Authentication uses Supabase JWT tokens
- File uploads are limited to PDF/DOCX under 10MB
- AI features use Groq's llama3-8b-8192 model

## Next Steps

1. Implement individual page components (starting with Landing)
2. Add authentication UI components
3. Implement resume form and preview
4. Add skill gap analysis UI
5. Add JD matcher interface
6. Connect all frontend components to backend APIs

## Technologies Used

### Frontend
- React 19
- Vite
- Tailwind CSS
- React Router
- Axios
- Supabase JS

### Backend
- FastAPI
- Python 3.8+
- ReportLab (PDF generation)
- python-docx (DOCX generation)
- pdfminer.six (PDF text extraction)
- Groq API (AI features)
- Supabase Py (database/auth)
- 🔒 CSRF token protection
- 🔒 Secure session cookies
- 🔒 File upload validation (MIME type & size limits)
- 🔒 Environment-based configuration
- 🔒 XSS & clickjacking prevention headers

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Backend Framework** | Django | 5.2.7 |
| **Language** | Python | 3.8 – 3.12 |
| **Database** | SQLite3 | (bundled) |
| **NLP Engine** | spaCy | 3.8.11 |
| **PDF Generation** | ReportLab | 4.4.4 |
| **Document Processing** | python-docx | 1.2.0 |
| **PDF Extraction** | pdfminer.six | 20250506 |
| **AI Integration** | OpenAI | 2.7.1 |
| **Environment** | python-dotenv | 1.2.1 |
| **Frontend** | HTML5, CSS3, JavaScript | - |
| **ORM** | Django ORM | built-in |

---

## 🐍 Python Version

**Required:** Python **3.8 or higher**  
**Tested on:** Python 3.8, 3.9, 3.10, 3.11, 3.12

To check your Python version:
```bash
python --version
# or
python3 --version
```

---

## 📁 Folder Structure

```
AI-Resume-Builder/
│
├── � backend/                     # Backend Django application
│   ├── 📂 resume_app/              # Main Django application
│   │   ├── migrations/             # Database migrations
│   │   │   └── (migration files)
│   │   ├── __init__.py
│   │   ├── models.py               # Database models
│   │   ├── views.py                # View functions & logic
│   │   ├── forms.py                # Django forms
│   │   ├── urls.py                 # App URL routing
│   │   ├── apps.py                 # App configuration
│   │   ├── admin.py                # Django admin setup
│   │   ├── utils.py                # Helper functions
│   │   └── tests.py                # Unit tests
│   │
│   ├── 📂 resume_builder/          # Django project configuration
│   │   ├── __init__.py
│   │   ├── settings.py             # Django settings (config, middleware, apps)
│   │   ├── urls.py                 # Root URL routing
│   │   ├── wsgi.py                 # WSGI application entry point
│   │   └── asgi.py                 # ASGI application entry point
│   │
│   ├── manage.py                   # Django management script
│   ├── requirements.txt            # Project dependencies
│   └── db.sqlite3                  # SQLite database
│
├── 📂 frontend/                    # Frontend assets
│   ├── 📂 templates/               # HTML templates
│   │   └── 📂 resume_app/
│   │       ├── base.html           # Base template (navbar, layout)
│   │       ├── landing.html        # Landing page
│   │       ├── home.html           # User dashboard
│   │       ├── login.html          # Login page
│   │       ├── signup.html         # Signup page
│   │       ├── forgot_password.html        # Password recovery
│   │       ├── verify_otp.html     # OTP verification
│   │       ├── reset_password.html # Password reset form
│   │       ├── skill_gap.html      # Skill gap analysis form
│   │       ├── enhance_skill_gap_result.html # Skill gap results
│   │       ├── jd_analyzer.html    # JD analyzer form
│   │       ├── jd_analysis_result.html # JD analysis results
│   │       ├── create_resume.html  # Resume creation form
│   │       ├── edit_resume.html    # Resume editing
│   │       ├── resume_preview.html # Resume preview
│   │       └── chat.html           # AI chat assistant
│   │
│   └── 📂 static/                  # Static files (CSS, JS, images)
│       └── 📂 resume_app/
│           └── style.css           # Global stylesheet
│
├── 📄 README.md                    # Project documentation (this file)
├── 📄 CLAUDE.md                    # Security and coding rules
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore                   # Git ignore rules
└── 📂 venv/                        # Python virtual environment (created locally)
```

---

## 📦 Installation & Setup

### Prerequisites
- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Builder.git
cd AI-Resume-Builder
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal after activation.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

This installs all required packages including:
- Django 5.2.7
- spaCy with English language model
- ReportLab (PDF generation)
- python-docx (DOCX support)
- OpenAI integration
- And other dependencies

### Step 4: Set Up Environment Variables

Copy `.env.example` to `.env` in the **project root**:

```bash
# On Windows
copy .env.example .env

# On macOS/Linux
cp .env.example .env
```

Edit `.env` with your configuration:

```env
DJANGO_SECRET_KEY=your-strong-secret-key-here
DJANGO_DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
OPENAI_API_KEY=your-openai-api-key-here
```

⚠️ **Important:**
- Never commit `.env` to version control
- Generate a strong SECRET_KEY (use Django's key generator or online tools)
- Set `DJANGO_DEBUG=False` in production
- Keep `OPENAI_API_KEY` secret

### Step 5: Apply Database Migrations

```bash
cd backend
python manage.py migrate
cd ..
```

This sets up the SQLite database with required tables.

### Step 6: Create a Superuser (Optional)

To access the Django admin panel:

```bash
cd backend
python manage.py createsuperuser
cd ..
```

Follow the prompts to create an admin account.

---

## ⚙️ Configuration

### `.env` File Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `DJANGO_SECRET_KEY` | Secret key for Django | `your-secret-key-xyz` |
| `DJANGO_DEBUG` | Debug mode (False in production) | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `OPENAI_API_KEY` | OpenAI API key for AI features | `sk-...` |

### Django Settings (`resume_builder/settings.py`)

Key configurations:
- **Database:** SQLite3 (`db.sqlite3`)
- **Static Files:** Located in `resume_app/static/`
- **Templates:** Located in `resume_app/templates/`
- **Security Headers:** Enabled (CSP, HSTS, X-Frame-Options, etc.)
- **Session Config:** Secure cookies, CSRF protection enabled

---

## 🚀 Running the Project

### Start the Development Server

Navigate to the backend folder and start the development server:

```bash
cd backend
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Access the Application

Open your browser and navigate to:
- **Home Page:** `http://127.0.0.1:8000/`
- **Landing Page:** `http://127.0.0.1:8000/landing`
- **Admin Panel:** `http://127.0.0.1:8000/admin` (requires superuser login)

### Common Commands

```bash
# Navigate to backend folder first
cd backend

# Run development server on a specific port
python manage.py runserver 8080

# Create database tables (after model changes)
python manage.py makemigrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic --noinput

# Interactive Python shell with Django context
python manage.py shell

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

---

## 📂 Project Modules

### Models (`resume_app/models.py`)
- **UserAccount** — User profiles (name, email, userid, password, phone)
- **Resume** — Saved resume data (name, email, education, experience, skills)
- **Skill** — Skill database (name, category)
- **JobRole** — Job role definitions
- **JobRoleSkill** — Mapping between job roles and required skills
- **Project** — Project recommendations
- **InterviewQuestion** — Interview questions per job role

### Views (`resume_app/views.py`)

#### Authentication
- `landing_page` — Public landing page
- `login_page` — User login
- `signup_page` — User registration
- `logout_user` — User logout
- `forgot_password` — Password reset request
- `verify_otp` — OTP verification
- `reset_password` — Password reset form

#### Resume Management
- `home` — User dashboard
- `create_resume` — Build resume from form
- `resume_preview` — Preview resume
- `edit_resume` — Edit uploaded resume
- `download_resume_pdf` — Export as PDF
- `download_resume_docx` — Export as DOCX

#### Analysis & Recommendations
- `skill_gap_form` — Skill gap analysis form
- `enhanced_skill_gap_analysis` — Skill gap results with recommendations
- `jd_analyzer_form` — Job description analyzer form
- `jd_analyzer_result` — JD analysis and project suggestions

#### AI Features
- `chat_assistant` — AI-powered chat endpoint

### Forms (`resume_app/forms.py`)
- **ResumeForm** — Django ModelForm for resume creation

### Utilities (`resume_app/utils.py`)
- Helper functions for resume processing
- File extraction utilities

---

## 🔐 Security Features

This project follows **OWASP Top 10** and **CLAUDE.md** security guidelines:

✅ **Authentication & Passwords**
- Bcrypt password hashing (Django's `make_password`)
- Secure password verification (`check_password`)
- Minimum 8-character password requirement

✅ **File Upload Safety**
- MIME type validation
- File size limits (10MB max)
- Allowed extensions: `.pdf`, `.docx` only

✅ **CSRF Protection**
- CSRF tokens on all forms
- Selective `@csrf_exempt` for JSON APIs only

✅ **HTTP Security Headers**
- `X-Frame-Options: DENY` — Clickjacking prevention
- `X-Content-Type-Options: nosniff` — MIME type sniffing prevention
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Strict-Transport-Security` — HTTPS enforcement
- `Content-Security-Policy` — XSS prevention

✅ **Environment & Configuration**
- Secrets in `.env` (never in code)
- `DEBUG=False` in production
- Secure session and CSRF cookies
- Strong SECRET_KEY requirement

✅ **Input Validation**
- Form validation on signup (email, userid)
- Resume file validation
- OTP verification

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** changes: `git commit -m 'Add feature'`
4. **Push** to branch: `git push origin feature/your-feature`
5. **Open** a Pull Request

### Code Standards
- Follow **PEP 8** for Python code
- Use meaningful variable and function names
- Add docstrings to functions
- Test changes before submitting

---

## 📝 License

This project is licensed under the **MIT License**. See LICENSE file for details.

---

## 📞 Support

For issues, questions, or suggestions:
- 🐛 Open an **Issue** on GitHub
- 💬 Check existing issues for solutions
- 📧 Contact the maintainers

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [spaCy NLP Guide](https://spacy.io/usage)
- [ReportLab Tutorial](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [OpenAI API Guide](https://platform.openai.com/docs)

---

**Made with ❤️ by the AI Resume Builder Team**