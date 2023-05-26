import './ArtistsList.css';
import React from 'react';
import ArtistCard from '../ArtistCard/ArtistCard';

export default function ArtistsList({artists}) {

    return (
        <>
            <div className="artists-list-container">
                {artists.map((artist, index) => (
                    <ArtistCard
                        key={index}
                        artistName={artist.name}
                        img={artist.image}
                    />
                ))}
            </div>
        </>
    )
}