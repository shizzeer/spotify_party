import './Join.css'
import { RoomContext } from '../../context/RoomContext';
import Header from "../../components/Header/Header";
import MustHave from "../../components/MustHave/MustHave";
import SessionPopup from "../../components/SessionPopup/SessionPopup";
import Artists from "../../components/Artists/Artists";
import Generes from "../../components/Generes/Generes";
import {Route, Routes} from "react-router-dom";
import Playlists from "../../components/Playlists/Playlists";
import Enjoy from "../../components/Enjoy/Enjoy";
import Albums from "../../components/Albums/Albums";
import {useState} from "react";
export default function Join() {
    const [roomCode, setRoomCode] = useState(null);

    return (

        <div className="Join">
            <RoomContext.Provider value={{ roomCode, setRoomCode }}>
                <Header roomCode={roomCode}/>
                  <div className="content">
                      <Routes>
                          <Route path="/" element={<SessionPopup />} />
                          <Route path="/playlists" element={<Playlists />} />
                          <Route path="/albums" element={<Albums />} />
                          <Route path="/artists" element={<Artists />} />
                          <Route path="/generes" element={<Generes />} />
                          <Route path="/must-have" element={<MustHave />} />
                          <Route path="/enjoy" element={<Enjoy />} />
                      </Routes>
                  </div>
            </RoomContext.Provider>
        </div>
    );
}