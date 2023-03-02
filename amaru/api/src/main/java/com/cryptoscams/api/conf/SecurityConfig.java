package com.cryptoscams.api.conf;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.autoconfigure.security.SecurityProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Value("${api.http.auth-token-header-name}")
    private String apiKeyHeader;

    @Value("${api.http.auth-token}")
    private String apiKey;

    @Bean
    @Order(SecurityProperties.BASIC_AUTH_ORDER)
    SecurityFilterChain defaultSecurityFilterChain(HttpSecurity http) throws Exception {

        HeaderApiKeyFilter filter = new HeaderApiKeyFilter(apiKeyHeader);
        filter.setAuthenticationManager(authentication -> {
            String principal = (String) authentication.getPrincipal();
            if (!apiKey.equals(principal)) {
                throw new BadCredentialsException("The API key was not found or not the expected value.");
            } else {
                authentication.setAuthenticated(true);
            }
            return authentication;
        });

        http.csrf().disable().
            sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS).
            and().addFilter(filter).authorizeHttpRequests().anyRequest().authenticated();
        return http.build();
    }
}
