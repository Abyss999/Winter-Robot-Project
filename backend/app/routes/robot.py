from app.imports import * 

robot_bp = Blueprint('robot', __name__)

@robot_bp.route('/health', methods=["GET"]) # checks the health the a robot 
def get_health(robot_id: int): # if robot offline, we can email admins or notify them in some way
    return jsonify({'status': f'Robot {robot_id} is operational'}), 200

@robot_bp.route('/status', methods=['GET']) # gets the status of the robot
def get_status(robot_id: int):
    # status = get_robot_status_from_db(robot_id) # placeholder for actual DB call
    # status = {
    #     'battery_level': 85,
    #     'position': {'x': 10, 'y': 20}, # can be direction, etc 
    #     'current_task': 'idle'
    # }
    return jsonify({'robot_id': robot_id, 'status': status}), 200


@robot_bp.route('/move', methods=['POST']) # moves the robot 
def move_robot(direction: str):
    data = request.get_json()
    direction = data.get('direction')
    if direction not in ['forward', 'backward', 'left', 'right']:
        return jsonify({'error': 'Invalid direction'}), 400
    
    # CURRENT_DIRECTION = direction # get from the database
    

@robot_bp.route('stop', methods=['POST']) # stops the robot
def stop_robot(robot_id: int):
    # stop_robot_in_db(robot_id) # placeholder for actual DB call
    return jsonify({'status': f'Robot {robot_id} has been stopped'}), 200



