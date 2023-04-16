import React from "react";
import "./Header.css";
import SpotifyPartyLogo from "../SpotifyPartyLogo/SpotifyPartyLogo";
import Navigation from "./Navigation/Navigation";

const Header = () => {
  return (
        <header className="header">
            <div className="header-logo-container">
                <SpotifyPartyLogo />
            </div>
            <div className="header-navigation-container">
                <Navigation />
            </div>
        </header>
  );
};

export default Header;