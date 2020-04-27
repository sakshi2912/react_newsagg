import React, { Component } from "react";
import { render } from "react-dom";
import  './App.css';
import { Link } from "react-router-dom";

class Weather extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }
  

  componentDidMount() {
    fetch("api/weathernews")
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
          <h1>Weather</h1>
       </div>
        {this.state.data.map(contact => {
          return (

            <div className="res">
                <h4>Weather Report</h4>
                <br />
                <p id="city">City : {contact.city} </p>
                <p id="temp">Temperature : {contact.temperature} °C </p>
                <p id="pres">Pressure : {contact.pressure} mb</p>
                <p id="hum">Humidity : {contact.humidity} %</p>
                <br />    
                <p id="desc">{contact.description}</p>
       
                </div>

         
          );
        })}
        
      </div>

      
    );
  }
}

export default Weather;

const container = document.getElementById("app");
render(<Weather />, container);