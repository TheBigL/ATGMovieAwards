import React from 'react';
 
import { NavLink } from 'react-router-dom';
import PrivateRoute from '..';

 
const Navigation = () => {
    return (
       <div>
          <NavLink to="/">Home</NavLink>
          <NavLink to="/about">About</NavLink>
          <NavLink to="/login">Login</NavLink>
          <PrivateRoute><NavLink to="/logout">Logout</NavLink></PrivateRoute>
          <PrivateRoute><NavLink to="/profile">Profile</NavLink></PrivateRoute>
          
       </div>
    );
}
 
export default Navigation;