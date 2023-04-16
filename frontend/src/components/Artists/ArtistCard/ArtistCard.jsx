import { useState } from 'react';
import './ArtistCard.css';

export default function ArtistCard({img, title, description}) {
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
        <div style={clickedStyle} className="artist-card-container" onClick={handleClick}>
            <div className="circular-avatar-container">
                <img className="circular-avatar" src={img} alt="Avatar"/>
            </div>
            <div className="desc-container">
                <h3>{title}</h3>
                <span>{description}</span>
            </div>
        </div>
    )
}