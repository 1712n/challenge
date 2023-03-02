package com.cryptoscams.api.hacks;

import com.cryptoscams.api.app.AbstractMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class HackMapper extends AbstractMapper<Hack, HackDTO> {
    HackMapper() {
        super(HackDTO.class);
    }
}
