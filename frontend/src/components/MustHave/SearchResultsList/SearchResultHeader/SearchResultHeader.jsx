import React from 'react';
import './SearchResultHeader.css';
import { FaClock} from "react-icons/fa";

function SearchResultHeader(){
  // @ts-ignore
  return (
        <tr className="table-header">
          <th>#</th>
          <th>TITLE</th>
          <th>ALBUM</th>
          <th>
            <FaClock id="clock-icon" />
          </th>
        </tr>
    );
}

export default SearchResultHeader;