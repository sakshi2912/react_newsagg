import React, { Component } from "react";
import { render } from "react-dom";
import  './App.css';
import { Link } from "react-router-dom";

class ConstrainVideoFacingModeParameters extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }
  

  componentDidMount() {
    fetch("api/covid1")
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
        <div >
          <h1>Covid</h1>
       </div>
      <div id="box-covid">

        {this.state.data.map(contact => {
          return (

            <a id="more" >
                          <br />
                          <h5>{contact.place} - {contact.number}</h5>

            </a>

         
          );
        })}
        
      </div>
      </div>
      
    );
  }
}

export default ConstrainVideoFacingModeParameters;

const container = document.getElementById("app");
render(<ConstrainVideoFacingModeParameters />, container);