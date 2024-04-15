exappco/
│
├── app/                      # Dossier principal de l'application Flask
│   ├── __init__.py           # Initialise l'application et intègre les modules
│   ├── app.py                # Point d'entrée de l'application, pourrait contenir la création de l'app
│   ├── requirements.txt      # Dépendances de l'application
│   │
│   ├── auth/                 # Module pour l'authentification
│   │   ├── __init__.py       # Initialise le blueprint pour l'authentification
│   │   ├── forms.py          # Formulaires relatifs à l'authentification (login, etc.)
│   │   └── views.py          # Vues pour l'authentification
│   │
│   ├── calendar/             # Module pour la gestion de calendrier
│   │   ├── __init__.py       # Initialise le blueprint pour le calendrier
│   │   ├── forms.py          # Formulaires relatifs à la gestion de calendrier
│   │   └── views.py          # Vues pour la gestion de calendrier
│   │
│   ├── templates/            # Templates HTML pour les vues
│   │   ├── auth/             # Templates pour l'authentification
│   │   │   └── login.html    # Template pour la page de login
│   │   │
│   │   ├── calendar/         # Templates pour le calendrier
│   │       └── calendar.html # Template pour la page du calendrier
│   │
│   └── static/               # Dossier pour les fichiers statiques (CSS, JS, images)
│
├── Dockerfile                # Fichier Docker pour construire l'image de l'application
└── docker-compose.yml        # Fichier Docker Compose pour orchestrer les conteneurs
