import React from 'react';
import ReactDOM from 'react-dom/client';
import {GlobalStyles} from '@mui/system';
import App from './App';

const globalStyles = (
    <GlobalStyles styles={{
        body: {
            margin: 0,
            fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
        'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
        sans-serif`,
            WebkitFontSmoothing: 'antialiased',
            MozOsxFontSmoothing: 'grayscale',
        },
        code: {
            fontFamily: `source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
        monospace`,
        },
    }}/>
);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        {globalStyles}
        <App/>
    </React.StrictMode>
);
