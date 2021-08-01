import ast
import json
from app import app

client = app.test_client()
testing_input = {
	"input": "this is the test input"
}

def test_hello():
    response = client.get("/")
    assert response.status_code == 200

def test_stringinate():
	response = client.post("/stringinate",
		json=testing_input)
	assert response.status_code == 200
	expected_response = ast.literal_eval(response.data.decode("utf-8"))
	assert expected_response["input"] == testing_input["input"]
	assert expected_response["length"] == 22
	assert expected_response["most common character"] == "t"
	assert expected_response["occurences of most common character"] == 5
