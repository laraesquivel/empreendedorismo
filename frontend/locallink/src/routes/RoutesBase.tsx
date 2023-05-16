import {Login} from "../pages/Login";
import { BrowserRouter, Routes, Route } from "react-router-dom";

export const RoutesBase = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login/>}/>                               
            </Routes>
        </BrowserRouter>
    );
};