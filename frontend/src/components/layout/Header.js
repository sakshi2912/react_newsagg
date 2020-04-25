import React, { Component } from 'react'
import { Link } from "react-router-dom";
import './Header.css';
export class Header extends Component {
    render() {
        return (
       
            <ul>
            <li >
                <Link to="/all">Latest</Link>
            </li>
            <li >
                <Link to="/world"> World </Link>
            </li>
            <li >
                <Link to="/tech"> Tech</Link>
            </li>
            <li >
                <Link to="/covid"> Covid</Link>
            </li>
            <li>
                <Link to="/sports">Sports</Link>
            </li>
           
            <li>
                <Link to="/weather">Weather</Link>
            </li>
            
            
            </ul>

        )
    }
}

export default Header
