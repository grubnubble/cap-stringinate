import re
from flask import Flask
from flask import request

app = Flask(__name__)

seen_strings = {}

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

    input_without_punct = re.sub(r"[^\w\s]", "", input)
    stripped_input = re.sub(r"\s+", "", input_without_punct)
    char_dict = {}
    for i in range(len(stripped_input)):
        if stripped_input[i] in char_dict:
            char_dict[stripped_input[i]] += 1
        else:
            char_dict[stripped_input[i]] = 1

    most_common_char = ''
    most_common_occurences = 0
    for char in char_dict.keys():
        if char_dict[char] > most_common_occurences:
            most_common_char = char
            most_common_occurences = char_dict[char]


    return {
        "input": input,
        "length": len(input),
        "most_common_character": most_common_char,
        "occurences_of_most_common_character": most_common_occurences,
    }

@app.route('/stats')
def string_stats():
    most_popular_string = ''
    most_popular_occurences = 0
    for item in seen_strings.keys():
        if seen_strings[item] > most_popular_occurences:
            most_popular_string = item
            most_popular_occurences = seen_strings[item]

    return {
        "inputs": seen_strings,
        "most_popular": most_popular_string,
    }