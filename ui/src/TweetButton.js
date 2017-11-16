import React from 'react';

// TODO check props

const TweetButton = props => {
    const {text, hashtags, url} = props;
    const href = `https://twitter.com/intent/tweet?text=${text}&hashtags=${hashtags}&url=${url}`;
    return (
        <a href={href} className="btn btn-link" target="_blank">
            <i className="fa fa-twitter-square fa-2x" aria-hidden="true"></i>
        </a>
    );
};

export default TweetButton;