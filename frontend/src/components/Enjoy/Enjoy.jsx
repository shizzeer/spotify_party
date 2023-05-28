import './Enjoy.css';
import { confetti } from "tsparticles-confetti";
import React, { useEffect } from 'react';

// go Buckeyes!
const colors = ["#1ed760", "#ffffff"];

const run = () => {
    const end = Date.now() + 15 * 1000;
    (function frame() {
        confetti({
            particleCount: 2,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: colors
        });

        confetti({
            particleCount: 2,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: colors
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
};

export default function Enjoy() {
    useEffect(() => {
        run();
    }, []);

    return (
        <>
            <div className="enjoy-container">
                <h1>Enjoy the music!</h1>
            </div>
        </>
    );
}