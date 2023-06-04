import React from "react";
import "./PrevArrow.css";

export default function PrevArrow(props) {
    const { className, onClick } = props;
    return (
        <div
            className={`${className} prev-arrow`}
            onClick={onClick}
        />
    );
}