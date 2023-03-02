package com.cryptoscams.api;

import com.cryptoscams.api.hacks.HackDTO;
import com.cryptoscams.api.hacks.HackMapper;
import com.cryptoscams.api.hacks.HackRepo;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class ApiApplicationTests {

    @Value("${api.http.auth-token-header-name}")
    private String apiKeyHeader;

    @Value("${api.http.auth-token}")
    private String apiKey;

    @Value("${api.data.default_page_size}")
    private Integer defaultPageSize;

    @Autowired
    private MockMvc mvc;

    @Autowired
    private HackRepo hackRepo;

    @Autowired
    private HackMapper hackMapper;

    private final ObjectMapper mapper = new ObjectMapper();

    @Test
    void Request_Without_Auth_failed() throws Exception {

        mvc.perform(get("/hacks/0")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    @Test
    void Get_Hacks_200() throws Exception {

        var pageRequest = PageRequest.of(0, defaultPageSize);
        var page = hackRepo.findAll(pageRequest);
        var repoData = hackMapper.mapPage(page);

        var resStr = mvc.perform(get("/hacks/0")
                        .header(apiKeyHeader, apiKey)
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andReturn().getResponse().getContentAsString();
        var apiData = mapper.readValue(resStr, new TypeReference<List<HackDTO>>(){});

        assertTrue(repoData.size() == apiData.size()
                && repoData.containsAll(apiData)
                && apiData.containsAll(repoData));
    }
}
