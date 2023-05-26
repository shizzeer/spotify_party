import './AlbumsList.css';
import React, {useEffect, useState} from 'react';
import AlbumCard from "../AlbumCard/AlbumCard";


export default function AlbumsList({albums, setSelectedAlbums}) {
    const [checkedAlbums, setCheckedAlbums] = useState([]);

    const handleCheckedChange = (index, isChecked) => {
        setCheckedAlbums(prevState => {
            const newState = [...prevState];
            if (isChecked) {
                newState.push(albums[index]);
            } else {
                newState.splice(newState.indexOf(albums[index]), 1);
            }
            return newState;
        });
    };

    useEffect(() => {
        setSelectedAlbums(checkedAlbums);
    }, [checkedAlbums, setSelectedAlbums]);

    return (
        <>
            <div className="albums-list-container">
                {albums.map((album, index) => (
                    <AlbumCard
                        key={index}
                        albumName={album.name}
                        artistName={album.artist}
                        img={album.image}
                        onCheckedChange={(isChecked) => handleCheckedChange(index, isChecked)}
                    />
                ))}
            </div>
        </>
    )
}