import './Generes.css';
import GeneresList from "./GeneresList/GeneresList";

export default function Generes() {
    return (
        <>
            <div className="generes-container">
                <h1>Select your top generes:</h1>
                <div className="generes-list-container">
                    <GeneresList />
                </div>
            </div>
        </>
    );
}