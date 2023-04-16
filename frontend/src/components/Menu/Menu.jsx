import { Link } from "react-router-dom";
import "./Menu.css";
import HostButton from "./HostButton/HostButton";
import JoinButton from "./JoinButton/JoinButton";

export default function Menu() {
    return (
        <div className="menu">
            <Link to="/host">
                <HostButton />
            </Link>
            <Link to="/join">
                <JoinButton />
            </Link>
        </div>
    );
}
