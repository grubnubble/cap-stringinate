import re
from flask import Flask
from flask import request

app = Flask(__name__)

seen_strings = {}
longest_string = ''

def get_highest_value_from_dictionary(dictionary):
    key_with_highest_value = ''
    the_highest_value = 0
    for key in dictionary.keys():
        if dictionary[key] > the_highest_value:
            key_with_highest_value = key
            the_highest_value = dictionary[key]
    return (key_with_highest_value, the_highest_value)

@app.route('/')
def root():
    return '''
    <pre>
    Welcome to the Stringinator 3000 for all of your string manipulation needs.

    GET / - You're already here!
    POST /stringinate - Get all of the info you've ever wanted about a string. Takes JSON of the following form: {"input":"your-string-goes-here"}
    GET /stats - Get statistics about all strings the server has seen, including the longest and most popular strings.
    </pre>
    '''.strip()

@app.route('/stringinate', methods=['GET','POST'])
def stringinate():
    input = ''
    if request.method == 'POST':
        input = request.json['input']
    else:
        input = request.args.get('input', '')

    if input in seen_strings:
        seen_strings[input] += 1
    else:
        seen_strings[input] = 1

    global longest_string
    if len(input) >= len(longest_string):
        longest_string = input

    input_without_punct = re.sub(r"[^\w\s]", "", input)
    stripped_input = re.sub(r"\s+", "", input_without_punct)
    char_dict = {}
    for i in range(len(stripped_input)):
        if stripped_input[i] in char_dict:
            char_dict[stripped_input[i]] += 1
        else:
            char_dict[stripped_input[i]] = 1

    (most_common_char, occurences) = get_highest_value_from_dictionary(char_dict)

    return {
        "input": input,
        "length": len(input),
        "most_common_character": most_common_char,
        "occurences_of_most_common_character": occurences,
    }

@app.route('/stats')
def string_stats():
    (most_popular_string, occurences) = get_highest_value_from_dictionary(seen_strings)

    return {
        "inputs": seen_strings,
        "most_popular": most_popular_string,
        "longest_input_received": longest_string,
    }