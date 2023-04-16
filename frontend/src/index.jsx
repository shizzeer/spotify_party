import React from "react";
import ReactDOM from "react-dom";
import Root from './routers/Root';
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "./index.css";

const root = ReactDOM.createRoot(
    document.getElementById("root")
);

const router = createBrowserRouter(Root);

root.render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);

