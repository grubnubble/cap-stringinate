## Initial Thoughts
It's been about 2 years since I used Python on a regular basis, so I am a little nervous about writing a Flask app. However, since I have been working exclusively on the front end for over a year, it makes the most sense for me to try out Python instead of spending time working out how to set up a backend in NodeJS. My strength at the moment is JavaScript, but I'm sure I can make good progress in Python, too. Plus I do enjoy Python, and I'm excited to try it out again.

## Notes
Wow, it has *really* been a long time since I looked at a Python app. I am trying my best to just take small steps (create a github repo, get the app running, follow the directions, etc) and not let myself get overwhelmed by this sense that I will not get this done to the quality I would like in the time I have allotted. 

For now, I am running the app and trying out different things in the browser and via the command line with `curl`. So far, I am successfully sending some strings to `/stringinate`, so I must be doing something right! I can see also that the `/stats` endpoint returns an `inputs` dictionary with inputted strings as keys and the number of times the string has been sent to `/stringinate` as the value.

:musical_note:_It's all coming back, it's all coming back to me nowww_:musical_note: I finally took a look at the code in `python/app.py` and it's starting to look familiar.

## Testing
I decided to work on tests as I go, which has the benefit of covering the "add your own adventure" feature portion of this assignment. To run tests, you will need to install [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html). Normally, you should be able to run `pytest` in the command line, but that was giving me trouble, so I run the tests with `python -m pytest` and it works better for me.