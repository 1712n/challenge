package com.cryptoscams.api.hacks;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Objects;

@NoArgsConstructor
@AllArgsConstructor
@Data
public class HackDTO {

    private String id;
    private String amountOfLoss;
    private String attackMethod;
    private String description;
    private String referenceUrl;
    private String target;
    private String time;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        HackDTO hackDTO = (HackDTO) o;
        return Objects.equals(id, hackDTO.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}