import React from 'react';

// TODO check props

const Quote = (props) => {
    const {quote, title, url} = props;
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
        </div>
    );
};

export default Quote;