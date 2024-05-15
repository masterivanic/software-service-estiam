import React from 'react';
import { Link } from 'react-router-dom';

function SideMenu() {
  return (
    <div className="side-menu">
        <div className='menu-items'><Link className='links' to="/">Accueil</Link></div>
        <div className='menu-items'><Link className='links' to="/users">Users List</Link></div>
    </div>
  );
}

export default SideMenu;
