import React, {Component} from 'react';
import Quote from './Quote';
import nprogress from 'nprogress';
import {fetchRandomQuote} from './service/quote';

class QuoteApp extends Component {

    constructor(props) {
        super(props);

        this.state = {
            quote: null
        };
    }

    componentDidMount() {
        this._fetchRandomQuote();
    }

    async _fetchRandomQuote() {
        nprogress.start();
        const quote = await fetchRandomQuote();
        nprogress.done();
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
            <Quote quote={quote} title={title} url={url} onRefresh={() => this._fetchRandomQuote()}/>
        );
    }

    render() {
        return (
            <div className="container">
                <div className="row justify-content-center align-self-center">
                    <div className="col-md-6 col-sm-12">
                        {this._renderQuote()}
                    </div>
                </div>
            </div>
        );
    }
}

export default QuoteApp;
