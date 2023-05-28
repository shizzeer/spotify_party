import './ArtistsList.css';
import React, { useState, useEffect } from 'react';
import ArtistCard from '../ArtistCard/ArtistCard';

export default function ArtistsList({artists, setSelectedArtists}) {
    const [checkedArtists, setCheckedArtists] = useState([]);

    const handleCheckedChange = (index, isChecked) => {
        setCheckedArtists(prevState => {
            const newState = [...prevState];
            if (isChecked) {
                newState.push(artists[index]);
            } else {
                newState.splice(newState.indexOf(artists[index]), 1);
            }
            return newState;
        });
    };

    useEffect(() => {
        setSelectedArtists(checkedArtists);
    }, [checkedArtists, setSelectedArtists]);

    return (
        <>
            <div className="artists-list-container">
                {artists.map((artist, index) => (
                    <ArtistCard
                        key={artist.id}
                        artistName={artist.name}
                        img={artist.image}
                        onCheckedChange={(isChecked) => handleCheckedChange(index, isChecked)}
                    />
                ))}
            </div>
        </>
    );
}