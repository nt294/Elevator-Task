from django.http import JsonResponse, Http404, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .functions import determine_direction, determine_elevator_suitability, find_best_elevator
from .models import Floor, ControlPanel, Elevator
import json


def get_all_floors(request):
    if request.method == 'GET':
        floors = Floor.objects.all()
        floor_list = list(floors.values())
        return JsonResponse({"floors": floor_list})
    else:
        return HttpResponseNotAllowed(['GET'])


def get_all_elevator_info(request):
    if request.method == 'GET':
        return JsonResponse({'elevator_info': retrieve_elevator_info()})
    else:
        return HttpResponseNotAllowed(['GET'])


def control_panels_by_floor(request, floor_id):
    if request.method == 'GET':
        try:
            floor = Floor.objects.get(pk=floor_id)
        except Floor.DoesNotExist:
            raise Http404("Floor not found")

        control_panels = floor.control_panels.all()
        control_panel_list = list(control_panels.values())
        return JsonResponse({"control_panels": control_panel_list})
    else:
        return HttpResponseNotAllowed(['GET'])


@csrf_exempt
def request_elevator(request):
    if request.method == 'POST':
        # Parse the JSON data from the request
        data = json.loads(request.body)

        # Get the selected floor number and control panel ID
        requested_floor_number = data.get('requested_floor_number')
        current_floor_number = data.get('current_floor_number')
        control_panel_id = data.get('control_panel_id')

        # Get the control panel object
        control_panel = ControlPanel.objects.get(id=control_panel_id)

        # Determine the appropriate elevator based on the control panel and selected floor
        return_dict = determine_elevator(control_panel, requested_floor_number)
        selected_elevator = return_dict['elevator']
        direction = return_dict['direction']

        # Now update the database
        update_elevator_status(elevator=selected_elevator, new_floor_number=current_floor_number, direction=direction)

        response_data = {
            'elevator_number': selected_elevator.number,
            'elevator_current_floor': selected_elevator.current_floor.number,
            'elevator_info': retrieve_elevator_info(),
            'direction': direction,
        }
        return JsonResponse(response_data)
    else:
        return HttpResponseNotAllowed(['POST'])


def retrieve_elevator_info():
    """Helper function to retrieve all elevator information from the database
    and return it as a list of dictionaries"""
    elevators = Elevator.objects.all()
    elevator_info = []

    for elevator in elevators:
        elevator_info.append({
            'id': elevator.id,
            'number': elevator.number,
            'current_floor': elevator.current_floor.number,
            'status': elevator.direction
        })

    return elevator_info


def determine_elevator(control_panel, requested_floor):
    """Helper function to determine the best elevator to send to a requested floor"""
    current_floor = control_panel.location_floor

    requested_direction = determine_direction(current_floor.number, requested_floor)

    eligible_elevators = Elevator.objects.filter(serviced_floors__number=requested_floor, direction='IDLE')
    if not eligible_elevators.exists():
        return None

    elevator_info = determine_elevator_suitability(current_floor.number, eligible_elevators)

    chosen_elevator = find_best_elevator(elevator_info, requested_direction)

    return {'elevator': chosen_elevator, 'direction': requested_direction}


def update_elevator_status(elevator, new_floor_number, direction):
    """Helper function to update the elevator's status in the database. This currently updates the values
    immediately rather than simulating the elevator's movement"""

    elevator.direction = direction

    # Then set the elevator's floor to the new floor
    elevator.current_floor = Floor.objects.get(number=new_floor_number)

    elevator.direction = 'IDLE'

    elevator.save()
