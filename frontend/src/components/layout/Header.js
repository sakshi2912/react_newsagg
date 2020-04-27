import React, { Component } from 'react'
import { Link } from "react-router-dom";
import './Header.css';
export class Header extends Component {
    render() {
        return (
       
            <ul>
            <li >
                <Link to="/all" style={{ textDecoration: 'none'}}>Latest</Link>
            </li>
            <li >
                <Link to="/world" style={{ textDecoration: 'none'}}> World </Link>
            </li>
            <li >
                <Link to="/tech" style={{ textDecoration: 'none'}}> Tech</Link>
            </li>
            <li >
                <Link to="/covid" style={{ textDecoration: 'none'}}> Covid</Link>
            </li>
            <li>
                <Link to="/sports" style={{ textDecoration: 'none'}}>Sports</Link>
            </li>
           
            <li>
                <Link to="/weather" style={{ textDecoration: 'none'}}>Weather</Link>
            </li>
            
            
            </ul>

        )
    }
}

export default Header
