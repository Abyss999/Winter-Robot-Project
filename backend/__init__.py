from app.imports import *

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class = 'config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class) # load config from config.py
    CORS( # enables cors (browser security)
        app,
        resources = {r"/auth/*": {"origins": app.config.get("FRONTEND_URL")}}, # only allow frontend url (mainly for auth)
        supports_credentials=True, # allow cookies
        expose_headers= ["Content-Type", "Authorization"], # expose these headers to the frontend
        allow_headers=["Content-Type", "Authorization"] # allow these headers from the frontend
        )
    uri = app.config.get("SQLALCHEMY_DATABASE_URI")
    if not uri:
        raise RuntimeError( 
            "Database URI not found. Please set the SQLALCHEMY_DATABASE_URI environment variable."
        ) 
    
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    db.init_app(app)

    # app.config["JWT_SECRET_KEY"] = app.config["JWT_ACCESS_SECRET"]
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = app.config["ACCESS_EXPIRES"]
    # jwt.init_app(app)

    try:
        from app.imports.route_imports import blueprints_with_prefixes
        for blueprint, prefix in blueprints_with_prefixes.items():
            app.register_blueprint(blueprint, url_prefix=prefix)
    except ImportError as e:
        raise RuntimeError("Failed to import blueprints. Ensure all route files are correct.") from e
    return app
