import {Box, Typography, Paper} from '@mui/material';


const elevatorInfoDisplayStyles = {
    marginLeft: '30px',
    marginTop: '20px',
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 2,
};

function ElevatorInfoDisplay(props) {
    return (
        <Box sx={elevatorInfoDisplayStyles}>
            {props.elevatorInfo.map((elevator) => {
                const {number, current_floor} = elevator;

                return (
                    <Paper key={number} elevation={3} sx={{padding: 2, minWidth: '150px'}}>
                        <Typography variant="h6">
                            Elevator #{number}
                        </Typography>
                        <Typography variant="body1">
                            Currently on Floor {current_floor}
                        </Typography>
                    </Paper>
                );
            })}
        </Box>
    );
}

export default ElevatorInfoDisplay;
