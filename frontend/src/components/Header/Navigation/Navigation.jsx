import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Navigation.css";
import {FaChevronRight, FaChevronLeft} from "react-icons/fa";

const Navigation: React.FC = () => {
    {/*Temporary routing for 17.04.2023 */}
    const pages = ["/join/", "/join/playlists", "/join/albums", "/join/generes", "/join/artists", "/join/must-have", "/join/enjoy"];
    const [currentPageIndex, setCurrentPageIndex] = useState(0);

    const goBack = () => {
        if (currentPageIndex > 0) {
            setCurrentPageIndex(currentPageIndex - 1);
        }
    };

    const goForward = () => {
        if (currentPageIndex < pages.length - 1) {
            setCurrentPageIndex(currentPageIndex + 1);
        }
    };

    return (
        <div className="header-navigation">
            <div className="circle" onClick={goBack}>
                <Link to={pages[currentPageIndex - 1]}>
                    <FaChevronLeft className="arrow" />
                </Link>
            </div>
            <div className="circle" onClick={goForward}>
                <Link to={pages[currentPageIndex + 1]}>
                    <FaChevronRight className="arrow" />
                </Link>
            </div>
        </div>
    );
};

export default Navigation;