import HostButtonImage from '../../../assets/host.png';
import './HostButton.css';
import axios from "axios";
export default function HostButton() {
    const hostParty = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/auth/host');
            const { data } = response;

            if (data && data.url) {
                window.location.href = data.url;
            }
        } catch (error) {
            console.error('Error hosting a party:', error);
        }
    };

    return (
        <div className="host-button-container" onClick={hostParty}>
            <img className='host-button-image' src={HostButtonImage} alt={'Host Image'}></img>
            <p className="host-button-text">{'Host a party'}</p>
        </div>
    );
}