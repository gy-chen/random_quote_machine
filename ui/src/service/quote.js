import axios from 'axios';

// const URL = "https://enigmatic-brushlands-20140.herokuapp.com";
const URL = "http://127.0.0.1:8000";

async function fetchRandomQuote() {
    const randomQuote = await axios.get(URL + "/quote/random");
    return randomQuote;
};

export {
    fetchRandomQuote
};