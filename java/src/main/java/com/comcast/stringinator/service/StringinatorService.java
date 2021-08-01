package com.comcast.stringinator.service;

import com.comcast.stringinator.model.StatsResult;
import com.comcast.stringinator.model.StringinatorInput;
import com.comcast.stringinator.model.StringinatorResult;

public interface StringinatorService {
    StringinatorResult stringinate(StringinatorInput input);

    StatsResult stats();
}