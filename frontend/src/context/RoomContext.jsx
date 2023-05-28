import React, {useState} from 'react';

export const RoomContext = React.createContext();

export function RoomProvider({ children }) {
    const [roomCode, setRoomCode] = useState(null);

    return (
        <RoomContext.Provider value={{ roomCode, setRoomCode }}>
            {children}
        </RoomContext.Provider>
    );
}