import Logo from '../../assets/logo.svg';
import './SpotifyPartyLogo.css';
export default function SpotifyPartyLogo() {
    return (
        <div className="logo-container">
            <img className='logo-image' src={Logo} alt={'SpotifyParty Logo'}></img>
        </div>
    );
}