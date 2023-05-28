import "./SearchResultsList.css";
import {SearchResult} from "./SearchResult/SearchResult";

export const SearchResultsList = ({ results }) => {
  return (
      <table className="results-list">
        {results.map((result) => {
          return <SearchResult result={result} />;
        })}
      </table>
  );
};
