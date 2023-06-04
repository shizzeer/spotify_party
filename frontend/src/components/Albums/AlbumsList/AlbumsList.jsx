import './AlbumsList.css';
import React, {useEffect, useState} from 'react';
import AlbumCard from "../AlbumCard/AlbumCard";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import NextArrow from "../../Arrows/NextArrow/NextArrow";
import PrevArrow from "../../Arrows/PrevArrow/PrevArrow";

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

    const settings = {
        dots: false,
        infinite: albums.length >= 5,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 5,
        nextArrow: <NextArrow />,
        prevArrow: <PrevArrow />,
        lazyLoad: true
    };

    return (
        <>
            {albums ? (
                <Slider {...settings}>
                    {albums.map((album, index) => {
                        return (
                            <AlbumCard
                                key={album.id}
                                albumName={album.name}
                                artistName={album.artist}
                                img={album.image}
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