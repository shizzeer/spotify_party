import "./SessionPopup.css";

export default function SessionPopup() {
    return (
        <div className="session-code-container">
            <h2>Join to your friends!</h2>
            <label className="session-code-input-wrapper">
                <input type="text" placeholder="Session Code"/>
            </label>
            <label className="session-code-input-wrapper">
                <button className="session-code-enter-button">Enter</button>
            </label>
        </div>
    );
}