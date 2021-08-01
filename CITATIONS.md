## References

- To review flask and python: my [take-home coding challenge](https://github.com/grubnubble/safeharbor) for Elsevier in 2019
- For a review of Python data structures: the [Python docs](https://docs.python.org/3/tutorial/datastructures.html)
- To remind myself how to use the [python debugger](https://docs.python.org/3/library/pdb.html)
- I was having trouble parsing the response in my test and learned about `ast.literal_eval()` in this [stackoverflow post](https://stackoverflow.com/questions/49184578/how-to-convert-bytes-type-to-dictionary)
- For a review of different loops in Python: the Python [control flow tutorial](https://docs.python.org/3/tutorial/controlflow.html)
- I also looked for different ways of looping through a dictionary, since that is the data structure I chose. I considered using tuples, but the dictionary solution came most easily to me, so I went with that. Here is the [source](https://realpython.com/iterate-through-dictionary-python/#iterating-through-items) I used for reviewing how to iterate through a python dictionary.
- Unpacking tuples: https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/
- I came across an issue with an `UnboundError` when trying to use a variable outside the scope of the routes. [Here](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value) is where I found out that the variable should be explicitly set as `global`. I don't feel great about this as a solution, but I do think that making the input string into a class would also take care of this issue.