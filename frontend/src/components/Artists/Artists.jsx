import './Artists.css';
import ArtistsList from "./ArtistsList/ArtistsList";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {useNavigate} from "react-router-dom";
export default function Artists() {
    const [artists, setArtists] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchArtists = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/me/artists', { withCredentials: true });
                setArtists(response.data);
            } catch (error) {
                console.error('Error fetching artists:', error);
            }
        };

        fetchArtists();
    }, []);

    const handleSubmitArtists = async () => {
        navigate("/join/must-have");
    };

    return (
        <>
            <div className="artists-container">
                <h1>Pick your favourite artists:</h1>
                <div className="artists-list-container">
                    <ArtistsList artists={artists} />
                </div>
                <button onClick={handleSubmitArtists}>Submit</button>
            </div>
        </>
    );
}