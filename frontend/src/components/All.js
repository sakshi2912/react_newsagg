import React, { Component } from "react";
import { render } from "react-dom";
import  './App.css';
import { Link } from "react-router-dom";

class All extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }
  

  componentDidMount() {
    fetch("api/fullmore")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <div className="container-1">
        <div class="heading">
        <h1>Latest</h1>
       </div>
        {this.state.data.map(contact => {
          return (

            <a  className ="more" href={contact.hyperlink}>
                      <div id="box">
                        <div className="head" >
                          <h5>{contact.headlines} </h5>
                        </div>
                      
                      <p id="source_style">{contact.source}</p>
                <p> {contact.description}</p>
                
                      </div> 
            </a>

         
          );
        })}
        
      </div>

      
    );
  }
}

export default All;

const container = document.getElementById("app");
render(<All />, container);