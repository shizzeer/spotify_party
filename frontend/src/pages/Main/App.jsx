import "./App.css";
import SpotifyPartyLogo from "../../components/SpotifyPartyLogo/SpotifyPartyLogo";
import Menu from "../../components/Menu/Menu";

export default function App() {
    return (
        <>
            <div className="App">
                <div className="App-logo">
                    <SpotifyPartyLogo />
                </div>
                <div className="App-menu">
                    <Menu />
                </div>
            </div>
        </>
    );
}
