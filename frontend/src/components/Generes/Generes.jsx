import './Generes.css';
import GeneresList from "./GeneresList/GeneresList";
import React from "react";
import axios from "axios";
import {useNavigate} from "react-router-dom";
import NextButton from "../NextButon/NextButton";

export default function Generes() {
    const navigate = useNavigate();
    const handleSubmitGenres = async () => {
        navigate("/join/enjoy");
    };

    return (
        <>
            <div className="generes-container">
                <h1>Select your top generes:</h1>
                <div className="generes-list-container">
                    <GeneresList />
                </div>
                <NextButton onClick={handleSubmitGenres} />
            </div>
        </>
    );
}