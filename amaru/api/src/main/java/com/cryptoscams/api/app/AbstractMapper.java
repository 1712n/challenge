package com.cryptoscams.api.app;

import org.modelmapper.ModelMapper;
import org.springframework.data.domain.Page;

import java.util.List;

public abstract class AbstractMapper<E, T> {
    private final ModelMapper modelMapper = new ModelMapper();
    private final Class<T> type;

    protected AbstractMapper(Class<T> type) {
        this.type = type;
    }

    public T mapEntity(E entity) {
        return modelMapper.map(entity, type);
    }

    public List<T> mapEntities(List<E> entities) {
        return entities.stream().map(this::mapEntity).toList();
    }

    public List<T> mapPage(Page<E> p){
        return p.map(this::mapEntity).stream().toList();
    }
}
