import pytest as pytest
from unittest.mock import Mock
from elevator_control.functions import determine_direction, determine_elevator_suitability, find_best_elevator


@pytest.mark.parametrize("current_floor_number, requested_floor_number, expected_direction", [
    (3, 5, 'UP'),
    (5, 3, 'DOWN'),
    (3, 3, 'IDLE')
])
def test_determine_direction(current_floor_number, requested_floor_number, expected_direction):
    """Test that the determine_direction function returns the correct direction for each request. The first parameter
    is the current floor number, the second parameter is the requested floor number, and the third parameter is the
    expected direction"""

    assert determine_direction(current_floor_number, requested_floor_number) == expected_direction


def test_determine_elevator_suitability():
    """Test that the determine_elevator_suitability function returns the correct information for each elevator.
    There are 4 elevators, and the current floor is 6. The elevators are on floors 8, 5, 3, and 7. The function should
    return the distance from the elevator to the current floor, the current floor number, and the direction the elevator
    needs to travel to get to the current floor"""

    current_floor_number = 6

    elevators = [Mock(current_floor=Mock(number=8)),
                 Mock(current_floor=Mock(number=5)),
                 Mock(current_floor=Mock(number=3)),
                 Mock(current_floor=Mock(number=7))]
    expected_info = {
        elevators[0]: {"distance": 2, "current_floor": 8, "required_direction": "DOWN"},
        elevators[1]: {"distance": 1, "current_floor": 5, "required_direction": "UP"},
        elevators[2]: {"distance": 3, "current_floor": 3, "required_direction": "UP"},
        elevators[3]: {"distance": 1, "current_floor": 7, "required_direction": "DOWN"},
    }

    elevator_info = determine_elevator_suitability(current_floor_number, elevators)
    assert elevator_info == expected_info


def test_find_best_elevator():
    """Test that the find_best_elevator function returns the most suitable elevator from a list of eligible elevators"""

    elevators = [Mock() for _ in range(4)]
    elevator_info = {
        elevators[0]: {"distance": 1, "current_floor": 7, "required_direction": "DOWN"},
        elevators[1]: {"distance": 3, "current_floor": 3, "required_direction": "UP"},
        elevators[2]: {"distance": 1, "current_floor": 5, "required_direction": "UP"},
        elevators[3]: {"distance": 2, "current_floor": 8, "required_direction": "DOWN"},
    }

    requested_direction = "DOWN"
    expected_elevator = elevators[0]
    assert find_best_elevator(elevator_info, requested_direction) == expected_elevator
