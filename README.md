# CAP Coding Interview

Through this exercise we wish to assess a candidates ability to execute on some of the more common types of tasks we see on a daily basis.  This exercise includes web services, string/collection manipulation, with a lead into design decisions for conversation during the interview.

Your job is to get the app running, [implement some features](#features-for-you-to-implement), and send us your implementation.

## Getting Started

To get you off to the right start we've provided an initial implementation of a basic rest service.  It provides an initial implementation of the `/`, `/stringinate` and `/stats` endpoints.  This implementation is available in 3 different languages:

- [Python](python/)
- [Java](java/)
- [Go](go/)

Each contains some instructions for requirements and how to get started in that environment. Before you begin work, please create a public repo in github and do all of your there.   
 

## Guidelines

We don't want to restrict your language choice here.  If your most productive language is NodeJs, Rust, etc. feel free to port the starting service over to the rest framework of your choice.  

Feel free to Google for things when you have questions.  We'd love some insight into your research process so please capture references (URLs) to sites you find helpful in solving these tasks.  Especially if you are tackling the tasks in a language with which you are not the most familiar.  References should be collected in the [CITATIONS.md](CITATIONS.md) file.

It's not expected that this exercise take more than an hour or two.  That being said, if you use
a language/framework combination other than those provided it could run over that time. We've provided a [NOTES.md](NOTES.md) file for you to document any decisions taken or things you'd like to communicate about you solutions.

This is a git project.  We prefer many small commits over one large commit.  It helps us understand your progression towards completion as well as giving us smaller increments to review.

## Submit

When you are ready to submit your exercise, please double check that you've included:

    1. Required features
    2. 1 Developer Choice feature
    3. Citations
    4. Decision document

Send us a link to your public repo with the above required features at least 24 hours before your scheduled interview. 


## The API

The application supports a small set of API endpoints that can be used to get information about and manipulate string values.  The application also tracks statistics about all the strings that have been sent to the server.

`/`

The root of the server, displays info about the other endpoints.  This is the only endpoint that does not return JSON.

`/stringinate`

Get all of the info you've ever wanted about a string. Accepts GET and POST requests.  For POSTs the endpoint takes JSON of the following form: 
    
```
    {"input":"your-string-goes-here"}
```
    
For GETs an input string is specified as `?input=<your-input>`.

`/stats`

Get statistics about all strings the server has seen, including the number of times each input has been received along with the longest and most popular strings etc.

## Features for You to Implement

Now that you have a running server it's time to add some features and make some changes to the application.

There are a few features that need to be added to the user-facing API:

* For the `/stringinate` endpoint, for a given input string we need to find the character that occurs most frequently and add that character, along with its number of occurrences to the API response JSON. You decide how to represent this in the JSON response.  Ignore white space and punctuation.
* For the `stats` endpoint, track which string input has been seen the most times. Return this value as the `most_popular` key in the response JSON.
* For the `stats` endpoint, track which string input is the longest string to be seen by the server and return as the `longest_input_received` key in the response JSON.

### Developer's Choice

It's your turn to add a feature or make other changes to improve the application.  Implement one new feature idea or change that makes the code better.

Some things you might consider:

* Could there be improvements to logging that might help with troubleshooting problems?
* Are there any input/output validations that might be helpful?
* Would the application benefit from unit or functional tests?
* Are there other interesting string manipulations or stats to implement? Longest palindrome? Anagram finder? Is a given string a dictionary word? The possibilities are virtually endless!
* Could any caching be added to reduce computation for a given input string?
* Could the code be refactored for better maintainability, understandability, extensibilty, etc?
* Could statistics be optionally stored outside of the app so that they can persist across server restarts?
* Would rate limiting to 5rps from a given IP be a useful tool for mitigating excess traffic to the server?
