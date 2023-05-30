import React from "react";
import ReactDOM from 'react-dom/client';
import Root from './routers/Root';
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./index.css";
import {RoomProvider} from "./context/RoomContext";

const root = ReactDOM.createRoot(
    document.getElementById("root")
);

const router = createBrowserRouter(Root);

root.render(
    <React.StrictMode>
        <RoomProvider>
            <RouterProvider router={router} />
        </RoomProvider>
    </React.StrictMode>
);

