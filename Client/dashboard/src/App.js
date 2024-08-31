import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

//import from files
import Header from './components/Header';
import Tabsrow from './components/Tabsrow';

function App() {
    // State to save data received from the server
    const [mainData, setMainData] = useState([]);    
    
    // Asynchronous function to fetch data from server and update the state
    const getDataFromDB = async() => {
        try {
            // Update the URL to point to your Flask backend
            const response = await axios.get("http://localhost:5000/api/data/all");
            setMainData(response.data.data);
        } catch(e) {
            console.log(e);
        }
    }

    // Call the above function on first render
    useEffect(() => {
        getDataFromDB();
    }, []);
    
    // Print the length of data received whenever the mainData state is updated
    useEffect(() => {
        console.log(mainData.length);
    }, [mainData]);

    return (
        <div>
            <Header />
            <Tabsrow data={mainData} setMainData={setMainData} />
        </div>
    );
}

export default App;

