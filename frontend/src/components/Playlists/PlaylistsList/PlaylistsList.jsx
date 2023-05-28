import './PlayListsList.css';
import React, { useState, useEffect } from 'react';
import defaultCover from '../../../assets/cover1.jfif';
import PlaylistCard from "../PlaylistCard/PlaylistCard";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import NextArrow from "../../Arrows/NextArrow/NextArrow";
import PrevArrow from "../../Arrows/PrevArrow/PrevArrow";


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

    const settings = {
        dots: false,
        infinite: playlists.length >= 5,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 5,
        nextArrow: <NextArrow />,
        prevArrow: <PrevArrow />,
        lazyLoad: true
    };

    return (
        <>
            {playlists ? (
                <Slider {...settings}>
                    {playlists.map((playlist, index) => {
                        return (
                            <PlaylistCard
                                key={playlist.id}
                                playlistName={playlist.name}
                                description={playlist.description}
                                img={playlist.image || defaultCover}
                                onCheckedChange={(isChecked) => handleCheckedChange(index, isChecked)}
                            />
                        );
                    })}
                </Slider>
            ) : (
                <p>Loading...</p>
            )}
        </>
    );
}