import "./SearchResult.css";

// @ts-ignore
export const SearchResult = ({ result }) => {
  return (
    <tr className="search-result" onClick={(e) => alert(`You selected ${result}!`)}>
      <td>#</td>
      <td>{result}</td>
    </tr>
  );
};