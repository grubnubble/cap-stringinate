import ast
import json
from app import app

client = app.test_client()
no_whitespace_or_punct = {
	"input": "thisTestInputH4sNoWh1tespaceOrPunctuation"
}
with_whitespace_and_punct = {
	"input": "this is some test input! 10:30am!!!!!"
}

def test_hello():
    response = client.get("/")
    assert response.status_code == 200

def test_stringinate():
	response = client.post("/stringinate",
		json=no_whitespace_or_punct)
	assert response.status_code == 200
	expected_response = ast.literal_eval(response.data.decode("utf-8"))
	assert expected_response["input"] == no_whitespace_or_punct["input"]
	assert expected_response["length"] == 41
	assert expected_response["most common character"] == "t"
	assert expected_response["occurences of most common character"] == 6

def test_whitespace_and_punctuation_not_included_in_count():
	response = client.post("/stringinate", json=with_whitespace_and_punct)
	assert response.status_code == 200
	expected_response = ast.literal_eval(response.data.decode("utf-8"))
	assert expected_response["input"] == with_whitespace_and_punct["input"]
	assert expected_response["length"] == 37
	assert expected_response["most common character"] == "t"
	assert expected_response["occurences of most common character"] == 4
