from app.imports import * 

stream_bp = Blueprint('stream', __name__)

@stream_bp.route("/robot/<int:robot_id>/stream", methods=["GET"])
def stream_robot_feed(robot_id: int):
    # implment the streaming logic later on
    return jsonify({"message": f"Streaming feed for robot {robot_id}"}),