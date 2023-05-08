import {Grid} from "@mui/material";
import {AwesomeButton} from "react-awesome-button";
import './custom-button.css'

function NumberPanel(props) {

    // Keep them in this order to display properly
    const floorNumbers = [6, 7, 8, 3, 4, 5, 0, 1, 2];

    return (
        <Grid sx={{marginTop: '5px'}} container spacing={3}>
            {(() => {
                const items = [];
                for (const floorNumber of floorNumbers) {
                    items.push(
                        <Grid item key={floorNumber}>
                            <AwesomeButton
                                disabled={props.floorLocation === floorNumber}
                                type="primary"
                                onPress={() => {
                                    props.handleFloorSelection(floorNumber);
                                }}>
                                <span>{floorNumber}</span>
                            </AwesomeButton>
                        </Grid>
                    );
                }

                return items;
            })()}
        </Grid>
    );
}

export default NumberPanel;
