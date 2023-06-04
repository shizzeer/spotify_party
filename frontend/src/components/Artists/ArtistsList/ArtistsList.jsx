import './ArtistsList.css';
import React, { useState, useEffect } from 'react';
import ArtistCard from '../ArtistCard/ArtistCard';
import NextArrow from "../../Arrows/NextArrow/NextArrow";
import PrevArrow from "../../Arrows/PrevArrow/PrevArrow";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

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

    const settings = {
        dots: false,
        infinite: artists.length >= 5,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 5,
        nextArrow: <NextArrow />,
        prevArrow: <PrevArrow />,
        lazyLoad: true
    };

    return (
        <>
            {artists ? (
                <Slider {...settings}>
                    {artists.map((artist, index) => {
                        return (
                            <ArtistCard
                                key={artist.id}
                                img={artist.image}
                                artistName={artist.name}
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