import './Playlists.css';
import PlaylistsList from "./PlaylistsList/PlaylistsList";
export default function Playlists() {
    return (
        <>
            <div className="playlists-container">
                <h1>Choose your playlists:</h1>
                <div className="playlists-list-container">
                    <PlaylistsList />
                </div>
            </div>
        </>
    );
}