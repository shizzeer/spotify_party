import "./Host.css";
import axios from 'axios';
import React, {useEffect, useContext, useState} from 'react';
import {RoomContext} from "../../context/RoomContext";
import NextButton from "../../components/NextButon/NextButton";
import {useNavigate} from "react-router-dom";

export default function Host() {
    const { roomCode, setRoomCode, isHost, setIsHost } = useContext(RoomContext);
    const [isLoading, setIsLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        const createRoom = async () => {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/room',
                    {
                        action: 'create'
                    },
                    {
                        withCredentials: true
                    });
                setIsLoading(false);
                setIsHost(true);
                setRoomCode(response.data.room_code);
            } catch (error) {
                console.error('Error creating room:', error);
            }
        };

        createRoom();
    }, [setRoomCode, setIsHost]);

    const handleJoinAsHost = async () => {
        navigate("/join/playlists");
    };

    return (
            <div className="Host">
                <h1>Your Room Code:</h1>
                {!isLoading && roomCode && <h2>{roomCode}</h2>}
                <NextButton onClick={handleJoinAsHost} disabled={isLoading || !roomCode} />
            </div>
    );
}
