import React, { useState } from "react";
import "./MustHave.css";
import SearchBar from "./SearchBar/SearchBar";
import { SearchResultsList } from "./SearchResultsList/SearchResultsList";
import SearchResultHeader from "./SearchResultsList/SearchResultHeader/SearchResultHeader";

export default function MustHave() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  return (
      <div className="must-have-container">
          <h1>Must-have song:</h1>
          <div className="search-bar-container">
              <SearchBar setResults={setResults} setLoading={setLoading}/>
          </div>
          <div className="search-results-container">
              <SearchResultHeader loading={loading}/>
              {results && results.length > 0 && <SearchResultsList results={results} />}
          </div>
      </div>
  );
}
