import React from "react";
import "./NextArrow.css";
export default function NextArrow(props) {
    const { className, onClick } = props;
    return (
        <div
            className={`${className} next-arrow`}
            onClick={onClick}
        />
    );
}