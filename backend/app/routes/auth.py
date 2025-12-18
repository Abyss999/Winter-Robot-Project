from app.imports import *

auth_bp = Blueprint('auth', __name__)


@auth_bp.post("/register")
def register_user():
    data = request.get_json() or {}
    email_raw = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email_raw or not password:
        return jsonify({"error": "Email and password are required"}), 400 # change this later on 
    
    # inserts the user into the database when database is implemented 

@auth_bp.post("/verify-email")
def verify_email():
    data = request.get_json() or {}
    email_raw = (data.get("email") or "").strip().lower()
    token = (data.dget("token") or "").strip()

    if not email_raw or not token:
        return jsonify({"error": "Email and token are required"}), 400
    
@auth_bp.post("/login")
def login_user():
    data = request.get_json() or {}
    email_raw = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    if not email_raw or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    # checks the user credentials when database is implemented

@auth_bp.post("/forgot-password")
def forgot_password():
    data = request.get_json() or {}
    email_raw = (data.get("email") or "").strip().lower()
    if not email_raw:
        return jsonify({"error": "Email is required"}), 400
    
    # sends a password reset email when email service is implemented

@auth_bp.post("/reset-password")
def reset_password():
    data = request.get_json() or {}
    email_raw = (data.get("email") or "").strip().lower()
    if not email_raw:
        return jsonify({"error": "Email is required"}), 400
    
    # sends a password reset email when email service is implemented

@auth_bp.post("/logout")
def logout_user():
    # handles user logout when session management is implemented
    return jsonify({"message": "User logged out successfully"}), 200