package com.comcast.stringinator.model;

public class StringinatorResult {
    private final String input;
    private final Integer length;

    public StringinatorResult(String input, Integer length) {
        this.input = input;
        this.length = length;
    }

    public Integer getLength() {
        return length;
    }

    public String getInput() {
        return this.input;
    }
}
