import './Enjoy.css';
import { confetti } from "tsparticles-confetti";
import React, { useContext, useEffect } from 'react';
import axios from 'axios';
import { RoomContext } from '../../context/RoomContext';

// go Buckeyes!
const colors = ["#1ed760", "#ffffff"];

const run = () => {
    const end = Date.now() + 15 * 1000;
    (function frame() {
        confetti({
            particleCount: 2,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: colors
        });

        confetti({
            particleCount: 2,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: colors
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
};

export default function Enjoy() {
    const { roomCode, isHost } = useContext(RoomContext);
    useEffect(() => {
        run();
        console.log(isHost);
    }, []);

    const handleCreatePlaylist = async () => {
        try {
            console.log('Room code: ', roomCode);
            await axios.post('http://127.0.0.1:8000/api/merge_playlists', { room_code: roomCode }, { withCredentials: true });
            console.log('Playlist created successfully!');
        } catch (error) {
            console.error('Error submitting playlists:', error);
        }
    };

    return (
        <>
            <div className="enjoy-container">
                <h1>Enjoy the music!</h1>
                {isHost && <button onClick={handleCreatePlaylist}>CREATE PLAYLIST</button>}
            </div>
        </>
    );
}