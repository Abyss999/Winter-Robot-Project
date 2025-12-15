from app.routes.stream import stream_bp
from app.routes.users import users_bp
from app.routes.admin import admin_bp
from app.routes.auth import auth_bp
from app.routes.robot import robot_bp

blueprints_with_prefixes = {
    stream_bp: '/stream',
    users_bp: '/users',
    admin_bp: '/admin',
    auth_bp: '/auth',
    robot_bp: '/robot',
}
