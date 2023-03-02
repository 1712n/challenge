package com.cryptoscams.api.hacks;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("hacks")
public class HackController {

    private final HackService hackService;
    private final HackMapper mapper;

    public HackController(HackService hackService, HackMapper mapper){
        this.hackService = hackService;
        this.mapper = mapper;
    }

    @GetMapping("/{pageNumber}")
    public List<HackDTO> getHacks(@PathVariable Integer pageNumber) {
        return mapper.mapPage(hackService.getHacks(pageNumber));
    }
}
