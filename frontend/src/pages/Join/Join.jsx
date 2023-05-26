import './Join.css'
import Header from "../../components/Header/Header";
import MustHave from "../../components/MustHave/MustHave";
import SessionPopup from "../../components/SessionPopup/SessionPopup";
import Artists from "../../components/Artists/Artists";
import Generes from "../../components/Generes/Generes";
import {Route, Routes} from "react-router-dom";
import Playlists from "../../components/Playlists/Playlists";
import Enjoy from "../../components/Enjoy/Enjoy";
import Albums from "../../components/Albums/Albums";
export default function Join() {

    return (
        <div className="Join">
            <Header />
          <div className="content">
              {/*Temporary routing for 17.04.2023 */}
              <Routes>
                  <Route path="/" element={<SessionPopup />} />
                  <Route path="/playlists" element={<Playlists />} />
                  <Route path="/albums" element={<Albums />} />
                  <Route path="/artists" element={<Artists />} />
                  <Route path="/generes" element={<Generes />} />
                  <Route path="/must-have" element={<MustHave />} />
                  <Route path="/enjoy" element={<Enjoy />} />
              </Routes>
              {/*Temporary routing for 17.04.2023 */}
          </div>
        </div>
    );
}