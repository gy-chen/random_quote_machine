import React from 'react';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg bg-dark navbar-dark justify-content-between">
            <a className="navbar-brand" href="/">Random Quote Machine</a>
            <a className="btn btn-link" href="https://github.com/gy-chen/random_quote_machine">
                <i className="fa fa-github-square fa-2x"
                   aria-hidden="true"></i>
            </a>
        </nav>
    );
};

export default Navbar;