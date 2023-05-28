import React, {useContext} from "react";
import "./Header.css";
import SpotifyPartyLogo from "../SpotifyPartyLogo/SpotifyPartyLogo";
import {RoomContext} from '../../context/RoomContext';

const Header = () => {
    const { roomCode } = useContext(RoomContext);

    return (
        <header className="header">
            <div className="header-logo-container">
                <SpotifyPartyLogo />
            </div>
            <div className="header-code-container">
                {roomCode && <h2 className="header-code">Room: {roomCode}</h2>}
            </div>
        </header>
    );
};

export default Header;