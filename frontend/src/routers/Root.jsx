import App from "../pages/Main/App";
import Host from "../pages/Host/Host";
import Join from "../pages/Join/Join";
import Generes from "../components/Generes/Generes";
import MustHave from "../components/MustHave/MustHave";
import Artists from "../components/Artists/Artists";
import Playlists from "../components/Playlists/Playlists";
import Enjoy from "../components/Enjoy/Enjoy";

const Root = [
    {
        path: "/",
        element: <App />,
    },
    {
        path: "host",
        element: <Host />,
    },
    {
        path: "join",
        element: <Join />,
        children: [
            {
                path: "generes",
                element: <Generes />
                // loader: generesLoader https://reactrouter.com/en/main/route/loader
            },
            {
                path: "playlists",
                element: <Playlists />
                // loader: playlistsLoader https://reactrouter.com/en/main/route/loader
            },
            {
                path: "must-have",
                element: <MustHave />
                // loader: must_Loader https://reactrouter.com/en/main/route/loader
            },
            {
                path: "artists",
                element: <Artists />
                // loader: must_Loader https://reactrouter.com/en/main/route/loader
            },
            {
                path: "enjoy",
                element: <Enjoy />
            },
        ],
    },
];

export default Root;
