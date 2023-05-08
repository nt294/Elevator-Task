import {Box} from "@mui/material";
import 'react-awesome-button/dist/styles.css';
import {useState, useEffect, useContext} from "react";
import {ElevatorInfoContext} from "../../Context/ElevatorInfoContext";
import DisplayPanel from "./DisplayPanel/DisplayPanel";
import NumberPanel from "./NumberPanel/NumberPanel";

const controlPanelStyle = {
    marginLeft: '30px',
    marginTop: '30px',
    marginBottom: '0px',
    marginRight: '10px',
    border: '1px solid #000000',
    boxShadow: `
        -1px 1px #868686,
        -2px 2px #868686,
        -3px 3px #868686,
        -4px 4px #868686,
        -5px 5px #868686
    `,
    height: 'auto',
    width: '240px',
    margin: '40px',
    padding: '10px',
    backgroundColor: '#ccc',
    fontFamily: 'sans-serif'
};

function ControlPanel(props) {

    const {setElevatorInfo} = useContext(ElevatorInfoContext);
    const [panelText, setPanelText] = useState("");

    useEffect(() => {
        setPanelText("Currently on: Floor " + props.floorLocation);
    }, [props.floorLocation]);


    const handleFloorSelection = async (floorNumber) => {
        try {
            const response = await fetch("http://localhost:8000/elevator-control/request-elevator/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    current_floor_number: props.floorLocation,
                    requested_floor_number: floorNumber,
                    control_panel_id: props.id,

                }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error ${response.status}`);
            }

            const data = await response.json();
            const direction = data['direction']
            const directionString = direction === 'UP' ? ' ↑' : ' ↓'

            setElevatorInfo(data['elevator_info'])
            setPanelText("Please enter Elevator " + [data['elevator_number'] + directionString]);

        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <Box sx={controlPanelStyle}>
            <DisplayPanel panelText={panelText}/>
            <NumberPanel floorLocation={props.floorLocation} handleFloorSelection={handleFloorSelection}/>
        </Box>
    );
}

export default ControlPanel;
