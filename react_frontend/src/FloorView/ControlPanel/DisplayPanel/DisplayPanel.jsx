import {Box} from "@mui/material";

const displayPanelStyle = {
    backgroundColor: 'black',
    height: '200px'
};

const textDisplayStyle = {
    color: 'white',
    textAlign: 'center',
    fontSize: '36px'
};

function DisplayPanel(props) {
    return (
        <Box sx={displayPanelStyle}>
            <Box sx={textDisplayStyle}>
                {props.panelText}
            </Box>
        </Box>
    );
}

export default DisplayPanel;
