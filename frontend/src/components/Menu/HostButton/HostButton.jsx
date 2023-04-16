import HostButtonImage from '../../../assets/host.png';
import './HostButton.css';
export default function HostButton() {
    return (
        <div className="host-button-container">
            <img className='host-button-image' src={HostButtonImage} alt={'Host Image'}></img>
            <p className="host-button-text">{'Host a party'}</p>
        </div>
    );
}