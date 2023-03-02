package com.cryptoscams.api.hacks;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class HackService {

    @Value("${api.data.default_page_size}")
    private Integer defaultPageSize;
    private final HackRepo hackRepo;

    public HackService(HackRepo hackRepo) {
        this.hackRepo = hackRepo;
    }

    public Page<Hack> getHacks(int pageNumber) {
        var pageRequest = PageRequest.of(pageNumber, defaultPageSize);
        return hackRepo.findAll(pageRequest);
    }
}
