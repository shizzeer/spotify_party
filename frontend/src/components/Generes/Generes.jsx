import './Generes.css';
import GeneresList from "./GeneresList/GeneresList";
import React from "react";
import axios from "axios";
import {useNavigate} from "react-router-dom";

export default function Generes() {
    const navigate = useNavigate();
    const handleSubmitGenres = async () => {
        navigate("/join/artists");
    };

    return (
        <>
            <div className="generes-container">
                <h1>Select your top generes:</h1>
                <div className="generes-list-container">
                    <GeneresList />
                </div>
                <button onClick={handleSubmitGenres}>Submit</button>
            </div>
        </>
    );
}