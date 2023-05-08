import {Box} from "@mui/material";
import {useEffect, useState} from "react";
import ControlPanel from "./ControlPanel/ControlPanel";

function FloorView(props) {

    const [controlPanels, setControlPanels] = useState([]);

    useEffect(() => {
        if (props.selectedFloor) {
            fetch("http://127.0.0.1:8000/elevator-control/floor/" + props.selectedFloor.value + "/control-panels/")
                .then((response) => response.json())
                .then((data) => setControlPanels(data['control_panels']))
                .catch((error) => console.error("Error:", error));
        }

    }, [props.selectedFloor]); // re-run the effect if props.selectedFloor changes

    return (
        <Box sx={{display: 'flex', flexWrap: 'wrap'}}>
            {controlPanels.map((controlPanel) => (
                <ControlPanel key={controlPanel.id} id={controlPanel.id} floorLocation={props.selectedFloor.label}/>
            ))}
        </Box>
    );

}

export default FloorView;
