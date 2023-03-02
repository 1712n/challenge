package com.cryptoscams.api.hacks;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "hacks")
@Getter @Setter
public class Hack {

    @Id
    private String id;
    private String amountOfLoss;
    private String attackMethod;
    private String description;
    private String referenceUrl;
    private String target;
    private String time;
}
