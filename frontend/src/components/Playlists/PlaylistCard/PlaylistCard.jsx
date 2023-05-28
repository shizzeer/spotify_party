import { useState} from 'react';
import './PlaylistCard.css';

export default function PlaylistCard({img, playlistName, description, onCheckedChange}) {
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
        <div style={checkedStyle} className="playlist-card-container" onClick={handleClick}>
            <img className="playlist-cover" src={img} alt="Playlist Cover"/>
            <div className="desc-container">
                <h3>{playlistName}</h3>
                <span>{description}</span>
            </div>
        </div>
    )
}