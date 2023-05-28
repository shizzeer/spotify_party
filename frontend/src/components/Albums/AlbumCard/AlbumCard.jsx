import { useState } from 'react';
import './AlbumCard.css';

export default function AlbumCard({img, albumName, artistName, onCheckedChange}) {
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
        <div style={checkedStyle} className="album-card-container" onClick={handleClick}>
            <img className="album-cover" src={img} alt="Album Cover"/>
            <div className="desc-container">
                <h3 className={'album-name'}>{albumName}</h3>
                <span>{artistName}</span>
            </div>
        </div>
    )
}