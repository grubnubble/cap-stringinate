package com.comcast.stringinator.model;

import java.util.Map;

public class StatsResult {
    private final Map<String, Integer> inputs;

    public StatsResult(Map<String, Integer> inputs) {
        this.inputs = inputs;
    }

    public Map<String, Integer> getInputs() {
        return inputs;
    }
}
