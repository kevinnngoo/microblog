# Microblog

A full-featured Flask web application following Miguel Grinberg's Flask Mega-Tutorial. This project demonstrates modern Flask development practices with real-time features, internationalization, and production-ready deployment.

## 🚀 Features

### Core Functionality
- **User Authentication** - Registration, login, logout, password reset
- **User Profiles** - Customizable profiles with Gravatar avatars
- **Social Features** - Follow/unfollow users, personalized timeline
- **Blog Posts** - Create, view, and manage blog posts with pagination
- **Private Messaging** - Real-time private messaging system with notifications
- **Full-Text Search** - Elasticsearch-powered search across posts
- **Post Translation** - Microsoft Translator integration for multilingual content

### Advanced Features
- **Real-time Notifications** - JavaScript polling for instant message notifications
- **Internationalization** - Multi-language support (English/Spanish)
- **User Discovery** - Hover-activated user popover cards
- **Responsive Design** - Bootstrap 5 mobile-first interface
- **Email Support** - Password reset and notification emails
- **Language Detection** - Automatic post language detection

## 🛠️ Technology Stack

- **Backend**: Flask 3.1.1, SQLAlchemy 3.1.1, Python 3.x
- **Frontend**: Bootstrap 5, JavaScript ES6+, Jinja2 templating
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Search**: Elasticsearch 9.0.2
- **Authentication**: Flask-Login, Werkzeug password hashing
- **Email**: Flask-Mail with SMTP support
- **Internationalization**: Flask-Babel
- **Deployment**: Docker, Vagrant, production scripts

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js (for frontend dependencies)
- Elasticsearch (optional, for search functionality)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/microblog.git
cd microblog
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Copy the environment template
cp .env-template .env

# Edit .env with your configuration
# At minimum, set:
# SECRET_KEY=your-secret-key-here
# MAIL_SERVER=your-smtp-server (optional)
# MS_TRANSLATOR_KEY=your-translator-key (optional)
# ELASTICSEARCH_URL=http://localhost:9200 (optional)
```

5. **Initialize the database**
```bash
flask db upgrade
```

6. **Run the application**
```bash
flask run
```

Visit `http://localhost:5000` to access the application.

## 🐳 Docker Deployment

### Quick Docker Setup
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run standalone
docker build -t microblog .
docker run -p 5000:5000 microblog
```

## 📱 Usage

### Getting Started
1. **Register** a new account or use the default admin account
2. **Complete your profile** with bio and avatar
3. **Create your first post** to share with followers
4. **Discover users** and start following interesting people
5. **Send private messages** to connect with other users
6. **Search posts** using the search bar in navigation

### Key Features Demo
- **Real-time Notifications**: Send a message to see live badge updates
- **Post Translation**: Click translate on posts in different languages
- **User Popovers**: Hover over usernames to see profile cards
- **Full-text Search**: Search for keywords across all posts
- **Responsive Design**: Try the app on mobile and desktop

## 🗂️ Project Structure

```
microblog/
├── app/                    # Main application package
│   ├── auth/              # Authentication blueprint
│   ├── main/              # Main application routes
│   ├── errors/            # Error handling
│   ├── templates/         # Jinja2 templates
│   ├── translations/      # Internationalization files
│   ├── models.py          # Database models
│   └── __init__.py        # Application factory
├── migrations/            # Database migration files
├── tests/                 # Unit tests
├── config.py             # Configuration settings
├── microblog.py          # Application entry point
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── docker-compose.yml   # Multi-service setup
```

## 🧪 Testing

```bash
# Run unit tests
python -m pytest

# Run with coverage
python -m pytest --cov=app
```

## 🌍 Internationalization

The application supports multiple languages:

```bash
# Extract strings for translation
flask translate init <language-code>

# Update translations
flask translate update

# Compile translations
flask translate compile
```

## 📈 Tutorial Progress

This project follows the Flask Mega-Tutorial chapters:

- ✅ **Chapter 1-10**: Core Flask application setup
- ✅ **Chapter 11-15**: Advanced features (email, search, etc.)
- ✅ **Chapter 16-20**: Production deployment features
- ✅ **Chapter 21**: User notifications and private messaging
- 🔄 **Chapter 22+**: Background jobs, APIs (future enhancements)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Miguel Grinberg** for the excellent Flask Mega-Tutorial
- **Flask Community** for the amazing framework and extensions
- **Bootstrap Team** for the responsive UI framework

## 📞 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com

---

**⭐ Star this repository if you found it helpful!**