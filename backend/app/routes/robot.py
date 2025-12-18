from app.imports import * 

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/health', methods=["GET"]) # checks the health the a robot 
def get_health(robot_id: int): # if robot offline, we can email admins or notify them in some way
    return jsonify({'status': f'Robot {robot_id} is operational'}), 200

@robot_bp.route('/move', methods=['POST']) # moves the robot 
def move_robot(direction: str):
    data = request.get_json()
    direction = data.get('direction')
    if direction not in ['forward', 'backward', 'left', 'right']:
        return jsonify({'error': 'Invalid direction'}), 400
    

    

