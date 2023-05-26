import './PlayListsList.css';
import React, { useState, useEffect } from 'react';
import defaultCover from '../../../assets/cover1.jfif';
import PlaylistCard from "../PlaylistCard/PlaylistCard";


export default function PlaylistsList({playlists, setSelectedPlaylists}) {
    const [checkedPlaylists, setCheckedPlaylists] = useState([]);

    const handleCheckedChange = (index, isChecked) => {
        setCheckedPlaylists(prevState => {
            const newState = [...prevState];
            if (isChecked) {
                newState.push(playlists[index]);
            } else {
                newState.splice(newState.indexOf(playlists[index]), 1);
            }
            return newState;
        });
    };

    useEffect(() => {
        setSelectedPlaylists(checkedPlaylists);
    }, [checkedPlaylists, setSelectedPlaylists]);

    return (
        <>
            <div className="playlists-list-container">
                {playlists.map((playlist, index) => (
                    <PlaylistCard
                        key={playlist.id}
                        playlistName={playlist.name}
                        description={playlist.description}
                        img={playlist.image || defaultCover}
                        onCheckedChange={(isChecked) => handleCheckedChange(index, isChecked)}
                    />
                ))}
            </div>
        </>
    );
}