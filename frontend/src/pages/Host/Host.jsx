import "./Host.css";

import axios from 'axios';
import { useEffect, useContext } from 'react';
import {RoomContext, RoomProvider} from '../../context/RoomContext';

export default function Host() {
    const { roomCode, setRoomCode } = useContext(RoomContext);

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

                setRoomCode(response.data.room_code);
            } catch (error) {
                console.error('Error creating room:', error);
            }
        };

        createRoom();
    }, [setRoomCode]);

    return (
        <RoomProvider>
            <div className="Host">
                <h1>Your Room Code:</h1>
                <h2>{roomCode}</h2>
            </div>
        </RoomProvider>
    );
}
