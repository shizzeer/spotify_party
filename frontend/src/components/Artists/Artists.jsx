import './Artists.css';
import ArtistsList from "./ArtistsList/ArtistsList";
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {useNavigate} from "react-router-dom";
import NextButton from "../NextButon/NextButton";
export default function Artists() {
    const [artists, setArtists] = useState([]);
    const [selectedArtists, setSelectedArtists] = useState([]);
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
        navigate("/join/generes");
        try {
            await axios.post('http://127.0.0.1:8000/api/me/artists', { selected_artists: selectedArtists }, { withCredentials: true });
            console.log('Artists submitted successfully!');
        } catch (error) {
            console.error('Error submitting artists:', error);
        }
    };

    return (
        <>
            <div className="artists-container">
                <h1>Choose your artists:</h1>
                <div className="artists-list-container">
                    <ArtistsList
                        artists={artists}
                        setSelectedArtists={setSelectedArtists}
                    />
                </div>
                <NextButton onClick={handleSubmitArtists} />
            </div>
        </>
    );
}