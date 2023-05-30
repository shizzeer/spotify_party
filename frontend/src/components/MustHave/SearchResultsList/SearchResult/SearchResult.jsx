import "./SearchResult.css";
import {useNavigate} from "react-router-dom";

export const SearchResult = ({ result, index }) => {
    const navigate = useNavigate();
    const handleSubmitMustHave = () => {
        navigate("/join/enjoy");
    }

    return (
        <tr className="search-result" onClick={handleSubmitMustHave}>
            <td>#</td>
            <td><img src={result.image} alt=" "/></td>
            <td className={'track-group'}>
                <span>{result.name}</span>
                <span>{result.artist}</span>
            </td>
            <td className={'album-result-container'}>{result.album}</td>
            <td>{result.duration}</td>
        </tr>
    );
};