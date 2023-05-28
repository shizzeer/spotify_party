import "./SearchResult.css";

export const SearchResult = ({ result, index }) => {
    return (
        <tr className="search-result" onClick={() => alert(`You selected ${result.name} by ${result.artist}!`)}>
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