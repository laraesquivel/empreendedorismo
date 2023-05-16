import {Login} from "../pages/Login";
import {SignUp} from "../pages/SignUp";
import { BrowserRouter, Routes, Route } from "react-router-dom";

export const RoutesBase = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login/>}/>                               
                <Route path="/signUp" element={<SignUp/>}/>                               
            </Routes>
        </BrowserRouter>
    );
};