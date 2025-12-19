from app.imports import *
import datetime


class Robot(db.Model):
    __tablename__ = 'robots'

    robot_id = db.Column(db.Integer, primary_key=True)
    last_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    stream_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_controlled = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
        return {
            'robot_id': self.robot_id,
            'last_user_id': self.last_user_id,
            'stream_url': self.stream_url,
            'created_at': self.created_at.isoformat(),
            'last_controlled': self.last_controlled.isoformat()
        }