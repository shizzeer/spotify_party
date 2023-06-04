import React, {useState} from 'react';

export const RoomContext = React.createContext();

export function RoomProvider({ children }) {
    const [roomCode, setRoomCode] = useState(null);
    const [isHost, setIsHost] = useState(false);

    return (
        <RoomContext.Provider value={{ roomCode, setRoomCode, isHost, setIsHost }}>
            {children}
        </RoomContext.Provider>
    );
}