import './ArtistsList.css';
import React from 'react';
import ArtistCard from '../ArtistCard/ArtistCard';
import artist1 from '../../../assets/artist1.jpg';
import artist2 from '../../../assets/artist2.jpeg';
import artist3 from '../../../assets/artist3.jpeg';
import artist4 from '../../../assets/artist4.jpeg';
import artist5 from '../../../assets/artist5.png';

export default function ArtistsList({artists}) {
    return (
        <>
            <div className="artists-list-container">
                <ArtistCard title="Lorem ipsum dolor" description="Artist" img={artist1}/>
                <ArtistCard title="Lorem ipsum dolor" description="Artist" img={artist2}/>
                <ArtistCard title="Lorem ipsum dolor" description="Artist" img={artist3}/>
                <ArtistCard title="Lorem ipsum dolor" description="Artist" img={artist4}/>
                <ArtistCard title="Lorem ipsum dolor" description="Artist" img={artist5}/>
            </div>
        </>
    )
}