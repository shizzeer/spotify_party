import './Albums.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AlbumsList from "./AlbumsList/AlbumsList";
import {useNavigate} from "react-router-dom";

export default function Albums() {
    const [albums, setAlbums] = useState([]);
    const [selectedAlbums, setSelectedAlbums] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchAlbums = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/me/albums', { withCredentials: true });
                setAlbums(response.data);
            } catch (error) {
                console.error('Error fetching albums:', error);
            }
        };

        fetchAlbums();
    }, []);

    const handleSubmitAlbums = async () => {
        navigate("/join/generes");
        try {
            await axios.post('http://127.0.0.1:8000/api/me/albums', { selected_albums: selectedAlbums }, { withCredentials: true });
            console.log('Albums submitted successfully!');
        } catch (error) {
            console.error('Error submitting albums:', error);
        }
    };

    return (
        <>
            <div className="albums-container">
                <h1>Choose your favourite albums:</h1>
                <div className="albums-list-container">
                    <AlbumsList
                        albums={albums}
                        setSelectedAlbums={setSelectedAlbums}
                    />
                </div>
                <button onClick={handleSubmitAlbums}>Submit</button>
            </div>
        </>
    );
}