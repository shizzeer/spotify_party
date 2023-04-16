import './Artists.css';
import ArtistsList from "./ArtistsList/ArtistsList";
export default function Artists() {
    return (
        <>
            <div className="artists-container">
                <h1>Pick your favourite artists:</h1>
                <div className="artists-list-container">
                    <ArtistsList />
                </div>
            </div>
        </>
    );
}