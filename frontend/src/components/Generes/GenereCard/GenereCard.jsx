import './GenereCard.css';
import { useState } from 'react';
export default function GenreCard({genere, cardColor, imgSrc}) {
    const [clicked, setClicked] = useState(false);
    const handleClick = () => {
        setClicked(!clicked);
    }

    const clickedStyle = {
        outline: clicked ? '2px solid #1DB954' : 'none',
        transform: clicked ? 'scale(1.02)' : 'scale(1.00)',
        transition: 'transform 0.2s ease-in-out',

        backgroundColor: cardColor // Click-independent style :)
    };

    return (
        <div style={clickedStyle} className="genere-card-container" onClick={handleClick}>
            <h3>{genere}</h3>
            <div className="genere-card-image-container">
                <img className="genere-image" src={imgSrc} alt="Genere photo"/>
            </div>
        </div>
    );
}
