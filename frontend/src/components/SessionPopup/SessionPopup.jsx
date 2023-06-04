import React, {useContext, useState} from 'react';
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { RoomContext } from '../../context/RoomContext';
import "./SessionPopup.css";

export default function SessionPopup() {
    const [sessionCode, setSessionCode] = useState('');
    const {setRoomCode } = useContext(RoomContext);
    const navigate = useNavigate();
    const handleInputChange = (event) => {
        setSessionCode(event.target.value);
    };

    const handleJoinSession = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/room', { action: 'join', room_code: sessionCode }, { withCredentials: true });
            console.log(response.data);

            if (response.status === 200) {
                setRoomCode(sessionCode);
                navigate("/join/playlists");
            }
        } catch (error) {
            console.error('Error joining session:', error);
        }
    };

    return (
        <div className="session-code-container">
            <h2>Join to your friends!</h2>
            <label className="session-code-input-wrapper">
                <input
                    type="text"
                    placeholder="Session Code"
                    value={sessionCode}
                    onChange={handleInputChange}
                />
            </label>
            <label className="session-code-input-wrapper">
                <button
                    className="session-code-enter-button"
                    onClick={handleJoinSession}>
                    Enter
                </button>
            </label>
        </div>
    );
}