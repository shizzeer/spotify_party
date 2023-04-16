import './PlayListsList.css';
import React from 'react';
import cover1 from '../../../assets/cover1.jfif';
import cover2 from '../../../assets/cover2.jfif';
import cover3 from '../../../assets/cover3.jfif';
import cover4 from '../../../assets/cover4.jfif';
import cover5 from '../../../assets/cover5.jfif';

import PlaylistCard from "../PlaylistCard/PlaylistCard";


export default function PlaylistsList({playlists}) {
    return (
        <>
            <div className="playlists-list-container">
                <PlaylistCard playlistName="Lorem ipsum dolor" description="Lorem ipsum dolor sit amet, consecte...." img={cover1}/>
                <PlaylistCard playlistName="Lorem ipsum dolor" description="Lorem ipsum dolor sit amet, consecte...." img={cover2}/>
                <PlaylistCard playlistName="Lorem ipsum dolor" description="Lorem ipsum dolor sit amet, consecte...." img={cover3}/>
                <PlaylistCard playlistName="Lorem ipsum dolor" description="Lorem ipsum dolor sit amet, consecte...." img={cover4}/>
                <PlaylistCard playlistName="Lorem ipsum dolor" description="Lorem ipsum dolor sit amet, consecte...." img={cover5}/>
            </div>
        </>
    )
}