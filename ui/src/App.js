import React, {Component} from 'react';
import Navbar from './Navbar';
import QuoteApp from './QuoteApp';

class App extends Component {

    render() {
        return (
            <div>
                <Navbar/>
                <div className="mt-4">
                    <QuoteApp/>
                </div>
            </div>
        );
    }
}

export default App;
