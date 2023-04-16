import './GeneresList.css';
import React from 'react';
import GenreCard from "../GenereCard/GenereCard";
import Foto from '../../../assets/foto.svg';
export default function GeneresList({generes}) {
    return (
        <>
            <div className="generes-list-container">
                <GenreCard genere={'Pop'} cardColor={'#44836C'} imgSrc={Foto}/>
                <GenreCard genere={'Hip-hop'} cardColor={'#223161'} imgSrc={Foto}/>
                <GenreCard genere={'Jazz'} cardColor={'#CF4421'} imgSrc={Foto}/>
                <GenreCard genere={'Rock'} cardColor={'#D5325D'} imgSrc={Foto}/>
                <GenreCard genere={'Country'} cardColor={'#777777'} imgSrc={Foto}/>
            </div>
        </>
    )
}