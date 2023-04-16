import JoinButtonImage from '../../../assets/join.png';
import './JoinButton.css';
export default function JoinButton() {
    return (
        <div className="join-button-container">
            <img className='join-button-image' src={JoinButtonImage} alt={'Join Image'}></img>
            <p className="join-button-text">{'Join the party'}</p>
        </div>
    );
}
