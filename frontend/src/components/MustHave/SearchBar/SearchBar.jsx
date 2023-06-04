import React, { useState, useEffect } from "react";
import axios from "axios";
import { FaSearch } from "react-icons/fa";
import "./SearchBar.css";

const SearchBar = ({ setResults, setLoading }) => {
    const [input, setInput] = useState("");
    const [debouncedInput, setDebouncedInput] = useState("");


    useEffect(() => {
        const timerId = setTimeout(() => {
            setDebouncedInput(input);
        }, 3000);

        // Start the loading animation 500ms after user starts typing
        const loadingTimerId = setTimeout(() => {
            if (input) {
                setLoading(true);
            } else {
                setLoading(false);  // If input is empty, stop the loading animation
            }
        }, 500);

        return () => {
            clearTimeout(timerId);
            clearTimeout(loadingTimerId);
        };
    }, [input, setLoading]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/me/must-have?q=${debouncedInput}`, { withCredentials: true });
                setResults(response.data);
            } catch (error) {
                console.error('Error:', error);
                setLoading(false);
            } finally {
                setLoading(false);
            }
        };

        if(debouncedInput) {
            fetchData();
        }
    }, [debouncedInput, setResults]);

    const handleChange = (event) => {
        if (event && event.target) {
            setInput(event.target.value);
        }
    };

    return (
        <div className="input-wrapper">
            <FaSearch id="search-icon" />
            <input
                placeholder="Search for a song..."
                value={input}
                onChange={handleChange}
            />
        </div>
    );
};

export default SearchBar;
