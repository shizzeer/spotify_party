import { useState } from 'react';
import './ArtistCard.css';

export default function ArtistCard({img, artistName, onCheckedChange}) {
    const [checked, setChecked] = useState(false);

    const handleClick = () => {
        const newCheckedState = !checked;
        setChecked(newCheckedState);
        onCheckedChange(newCheckedState);
    };

    const checkedStyle = {
        outline: checked ? '2px solid #1DB954' : 'none',
        transform: checked ? 'scale(1.02)' : 'scale(1.00)',
        transition: 'transform 0.2s ease-in-out'
    };

    return (
        <div style={checkedStyle} className="artist-card-container" onClick={handleClick}>
            <img className="circular-avatar" src={img} alt="Avatar"/>
            <div className="desc-container">
                <h3 className="artists-name">{artistName}</h3>
            </div>
        </div>
    )
}