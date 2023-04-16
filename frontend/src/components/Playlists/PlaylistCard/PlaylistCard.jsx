import { useState } from 'react';
import './PlaylistCard.css';

export default function PlaylistCard({img, playlistName, description}) {
    const [clicked, setClicked] = useState(false);

    const handleClick = () => {
        setClicked(!clicked);
    }

    const clickedStyle = {
        outline: clicked ? '2px solid #1DB954' : 'none',
        transform: clicked ? 'scale(1.02)' : 'scale(1.00)',
        transition: 'transform 0.2s ease-in-out'
    };

    return (
        <div style={clickedStyle} className="playlist-card-container" onClick={handleClick}>
            <div className="playlist-cover-container">
                <img className="playlist-cover" src={img} alt="Playlist Cover"/>
            </div>
            <div className="desc-container">
                <h3>{playlistName}</h3>
                <span>{description}</span>
            </div>
        </div>
    )
}