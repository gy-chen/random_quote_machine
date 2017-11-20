import axios from 'axios';

const URL = "https://enigmatic-brushlands-20140.herokuapp.com";

async function fetchRandomQuote() {
    const randomQuote = await axios.get(URL + "/quote/random").then(res => res.data);
    return randomQuote;
};

export {
    fetchRandomQuote
};