import React from 'react';
import axios from 'axios';
import JoinButtonImage from '../../../assets/join.png';
import './JoinButton.css';
export default function JoinButton() {
    const joinParty = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/auth/join');
            const { data } = response;

            if (data && data.url) {
                window.location.href = data.url;
            }
        } catch (error) {
            console.error('Error joining party:', error);
        }
    };

    return (
        <div className="join-button-container" onClick={joinParty}>
            <img className='join-button-image' src={JoinButtonImage} alt={'Join Image'}></img>
            <p className="join-button-text">{'Join the party'}</p>
        </div>
    );
}
