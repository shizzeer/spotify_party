import './Playlists.css';
import PlaylistsList from "./PlaylistsList/PlaylistsList";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {useNavigate} from "react-router-dom";

export default function Playlists() {
    const [playlists, setPlaylists] = useState([]);
    const [selectedPlaylists, setSelectedPlaylists] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchPlaylists = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/me/playlists', { withCredentials: true });
                setPlaylists(response.data);
            } catch (error) {
                console.error('Error fetching playlists:', error);
            }
        };

        fetchPlaylists();
    }, []);

    const handleSubmitPlaylists = async () => {
        navigate("/join/albums");
        try {
            await axios.post('http://127.0.0.1:8000/api/me/playlists', { selected_playlists: selectedPlaylists }, { withCredentials: true });
            console.log('Playlists submitted successfully!');
        } catch (error) {
            console.error('Error submitting playlists:', error);
        }
    };

    return (
        <>
            <div className="playlists-container">
                <h1>Choose your playlists:</h1>
                <div className="playlists-list-container">
                    <PlaylistsList
                        playlists={playlists}
                        setSelectedPlaylists={setSelectedPlaylists}
                    />
                </div>
                <button onClick={handleSubmitPlaylists}>Submit</button>
            </div>
        </>
    );
}