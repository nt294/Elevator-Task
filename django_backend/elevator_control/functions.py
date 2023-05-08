def determine_direction(current_floor_number, requested_floor_number):
    if requested_floor_number > current_floor_number:
        return 'UP'
    elif requested_floor_number < current_floor_number:
        return 'DOWN'
    else:
        return 'IDLE'


def determine_elevator_suitability(current_floor_number, eligible_elevators):
    elevator_info = {}
    for elevator in eligible_elevators:
        distance = abs(elevator.current_floor.number - current_floor_number)
        if elevator.current_floor.number > current_floor_number:
            required_direction = 'DOWN'
        elif elevator.current_floor.number < current_floor_number:
            required_direction = 'UP'
        else:
            required_direction = 'IDLE'

        elevator_info[elevator] = {
            "distance": distance,
            "current_floor": elevator.current_floor.number,
            "required_direction": required_direction
        }
    return elevator_info


def find_best_elevator(elevator_info, requested_direction):
    chosen_elevator = None
    min_distance = float('inf')

    # Prioritise elevators already on the user's floor with the correct direction or in idle state
    for elevator, info in elevator_info.items():
        if info['distance'] == 0 and (info['required_direction'] == requested_direction
                                      or info['required_direction'] == 'IDLE'):
            return elevator

    # Find the closest elevator with the correct direction
    for elevator, info in elevator_info.items():
        if info['required_direction'] == requested_direction and (info['distance'] < min_distance):
            chosen_elevator = elevator
            min_distance = info['distance']

    # If no elevator with the correct direction is found, find the closest elevator regardless of direction
    if chosen_elevator is None:
        min_distance = float('inf')
        for elevator, info in elevator_info.items():
            if info['distance'] < min_distance:
                chosen_elevator = elevator
                min_distance = info['distance']

    return chosen_elevator
