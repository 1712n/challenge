package com.cryptoscams.api.app;

import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ConfigurationException;
import org.modelmapper.MappingException;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.util.NoSuchElementException;

@Slf4j
@ControllerAdvice
public class RequestExceptionHandler extends ResponseEntityExceptionHandler {

    //Mapping entity to dto exception handler
    @ExceptionHandler(value = {ConfigurationException.class, MappingException.class})
    protected ResponseEntity<Object> handleMapperEx(RuntimeException ex, WebRequest request) {
        String responseBody = "Mapping entity to dto fucked up";
        log.info(responseBody, ex.getMessage());
        return handleExceptionInternal(ex, responseBody, new HttpHeaders(), HttpStatus.INTERNAL_SERVER_ERROR, request);
    }

    //No entity
    @ExceptionHandler(value = {NoSuchElementException.class})
    protected ResponseEntity<Object> handleNoEntityEx(RuntimeException ex, WebRequest request) {
        String responseBody = "Entity not exist";
        log.info(responseBody, ex.getMessage());
        return handleExceptionInternal(ex, responseBody, new HttpHeaders(), HttpStatus.NOT_FOUND, request);
    }
}