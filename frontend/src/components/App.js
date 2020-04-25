import React ,{ Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Header from './layout/Header';
import Dashboard from './leads/Dashboard';
import Tech from './Tech';
import Covid from './Covid';
import All from './All';
import World from './World';
import Sports from './Sports';
import Weather from './Weather';
import { HashRouter as Router , Route , Switch, Redirect} from 'react-router-dom';

class App extends Component{
    render(){
        return (
            <Router>
            <Fragment>
                <Header />
                <div className="container">
                    <Switch>
                        <Route exact path ="/" component= {Dashboard} />
                        <Route exact path ="/tech" component= {Tech} />
                        <Route exact path ="/covid" component= {Covid} />
                        <Route exact path ="/all" component= {All} />
                        <Route exact path ="/sports" component= {Sports} />
                        <Route exact path ="/world" component= {World} />
                        <Route exact path ="/weather" component= {Weather} />

                       
                    </Switch>
               
                </div>
                
            </Fragment>
            </Router>
        )
    }
}

ReactDOM.render(<App />,document.getElementById('app'));