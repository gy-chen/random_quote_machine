import React, {Component} from 'react';
import Quote from './Quote';
import { fetchRandomQuote } from './service/quote';

class App extends Component {

    constructor(props) {
        super(props);

        this.state = {
            quote: null
        };
    }

    async componentDidMount() {
        const quote = await fetchRandomQuote();
        this.setState({
           quote
        });
    }

    _renderQuote() {
        if (!this.state.quote) {
            return;
        }
        const {quote: {quote}} = this.state.quote;
        const {video: {title, url}} = this.state.quote;
        return (
            <Quote quote={quote} title={title} url={url}/>
        );
    }

    render() {
        return (
            <div className="container-fluid">
                <div className="row justify-content-center">
                    <div className="col-md-6 col-sm-12">
                        {this._renderQuote()}
                    </div>
                </div>
            </div>
        );
    }
}

export default App;
