import {useEffect, useState} from "react";
import FloorView from "./FloorView/FloorView";
import ElevatorInfoDisplay from "./ElevatorInfoDisplay/ElevatorInfoDisplay";
import Select from "react-select";
import {Box, Link} from "@mui/material";
import {ElevatorInfoContext} from "./Context/ElevatorInfoContext";

const selectStyles = {
    control: (provided) => ({
        ...provided,
        width: 300,
        fontSize: "2em",
        marginLeft: "30px",
        marginTop: "10px",
        textAlign: "center",
    }),
    singleValue: (provided) => ({...provided, fontSize: "30px"}),
    option: (provided) => ({...provided, fontSize: "20px"}),
    placeholder: (provided) => ({...provided, fontSize: "30px"}),
    menu: (provided) => ({
        ...provided,
        width: 300,
        marginLeft: "20px",
        zIndex: '1000',
    }),
};

function App() {

    const [elevatorInfo, setElevatorInfo] = useState([]);
    const [floorOptions, setFloorOptions] = useState([]);
    const [selectedFloor, setSelectedFloor] = useState(null);

    const handleReceivedFloors = (messageEvent) => {
        const floors = messageEvent["floors"];
        setFloorOptions(
            floors.map((floor) => {
                return {value: floor.id, label: floor.number};
            })
        );
    };

    const handleElevatorInfo = (messageEvent) => {
        setElevatorInfo(messageEvent['elevator_info']);
    };

    useEffect(() => {
        // First get all floors
        fetch("http://localhost:8000/elevator-control/get-all-floors/")
            .then((response) => response.json())
            .then((data) => handleReceivedFloors(data))
            .catch((error) => console.error("Error:", error));

        // Then get elevator info
        fetch("http://localhost:8000/elevator-control/get-all-elevator-info/")
            .then((response) => response.json())
            .then((data) => handleElevatorInfo(data))
            .catch((error) => console.error("Error:", error));
    }, []); // Only run once

    return (
        <>
            <Box sx={{display: "flex", flexDirection: "row"}}>
                <Select
                    placeholder={"Select a floor"}
                    value={selectedFloor}
                    onChange={setSelectedFloor}
                    options={floorOptions}
                    styles={selectStyles}
                />

                <Box sx={{marginLeft: "30px", marginTop: "25px"}}>
                    <Link href="http://127.0.0.1:8000/admin" style={{
                        textDecoration: "none",
                        fontSize: "20px",
                        color: "blue",
                        cursor: "pointer",
                    }}>
                        Click here to go to the config page
                    </Link>
                </Box>

            </Box>

            <ElevatorInfoDisplay elevatorInfo={elevatorInfo}/>

            <ElevatorInfoContext.Provider value={{setElevatorInfo}}>
                {selectedFloor ? (
                    <FloorView selectedFloor={selectedFloor}/>
                ) : <Box sx={{marginLeft: "30px", marginTop: '40px'}}>
                    Select a floor to view its control panels
                </Box>}
            </ElevatorInfoContext.Provider>
        </>

    );
}

export default App;
