import _ from 'lodash';
import React from 'react';
import TweetButton from './TweetButton';
// TODO check props

const Quote = (props) => {
    const {
        quote,
        title,
        url
    } = props;
    return (
        <div className="card text-center">
            <div className="card-body">
                <blockquote className="blockquote">
                    <p>{quote}</p>
                    <footer className="blockquote-footer">
                        <cite><a href={url} target="_blank" className="card-link text-secondary">{title}</a></cite>
                    </footer>
                </blockquote>
            </div>
            <div className="card-footer d-flex">
                <TweetButton text={quote} hashtags="quotes" url={url}/>
                <button type="button" className="btn btn-link" onClick={() => _.invoke(props, 'onRefresh')}>
                    <i className="fa fa-refresh fa-2x" aria-hidden="true"></i>
                </button>
            </div>
        </div>
    );
};

export default Quote;