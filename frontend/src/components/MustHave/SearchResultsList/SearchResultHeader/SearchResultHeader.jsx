import React from 'react';
import './SearchResultHeader.css';
import { FaClock} from "react-icons/fa";

export default function SearchResultHeader({ loading }){
    return (
        <tr className={`table-header ${loading ? 'loading' : ''}`}>
            <th>#</th>
            <th>TITLE</th>
            <th>ALBUM</th>
            <th>
                <FaClock id="clock-icon" /> {/*DURATION*/}
            </th>
        </tr>
    );
}