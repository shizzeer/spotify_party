import "./NextButton.css"
import React from "react";

export default function NextButton(props) {
    return (
        <button className="next-button" onClick={props.onClick}>
            <span className="next-button__text">Next</span>
            <span className="next-button__arrow">→</span>
        </button>
    )
}