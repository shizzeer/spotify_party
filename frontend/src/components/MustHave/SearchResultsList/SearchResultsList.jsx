import "./SearchResultsList.css";
import { Key } from "react";
import {SearchResult} from "./SearchResult/SearchResult";

export const SearchResultsList = ({ results }) => {
  return (
    <div className="results-list">
      {results.map((result: { name: any; }, id: Key | null | undefined) => {
        return <SearchResult result={result.name} key={id} />;
      })}
    </div>
  );
};
