import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg">
        <Link className="navbar-brand" to="/">Home</Link>
        <Link className="navbar-brand" to="/about">Sobre</Link>
    </nav>
  );
};

export default Navbar;
