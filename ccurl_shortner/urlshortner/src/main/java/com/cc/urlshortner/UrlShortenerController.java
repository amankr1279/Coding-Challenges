package com.cc.urlshortner;

import com.cc.urlshortner.model.AddUrlRequest;
import com.cc.urlshortner.model.AddUrlResponse;
import jakarta.servlet.http.HttpServletRequest;
import lombok.extern.slf4j.Slf4j;
import org.jetbrains.annotations.NotNull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@Slf4j
public class UrlShortenerController {

    @Autowired
    private UrlShortenerService shortenerService;

    @PostMapping("/add")
    public ResponseEntity<AddUrlResponse> postURL(@RequestBody @NotNull AddUrlRequest body) {
        log.info("Request body :" + body.toString());
        AddUrlResponse addUrlResponse = new AddUrlResponse();
        try {
            String shortUrl = shortenerService.shortenUrl(body.getLongUrl());
            addUrlResponse.setShortUrl("http://localhost:8080/" + shortUrl);
            addUrlResponse.setLongUrl(body.getLongUrl());
            addUrlResponse.setKey(shortUrl);
            ResponseEntity<AddUrlResponse> response = new ResponseEntity<>(addUrlResponse, HttpStatus.OK);
            return response;
        } catch (Exception e) {
            e.printStackTrace();
            addUrlResponse.setMessage("Bad Request");
            ResponseEntity<AddUrlResponse> response = new ResponseEntity<>(addUrlResponse, HttpStatus.BAD_REQUEST);
            return response;
        }
    }

    @DeleteMapping("/{key}")
    public ResponseEntity<String> removeUrl(@PathVariable("key") String key, @NotNull HttpServletRequest request) {
        try {
            log.info("Request to remove : " + request.getRequestURI());
            shortenerService.removeUrl(key);
            ResponseEntity<String> response = new ResponseEntity<>("Deleted\n", HttpStatus.OK);
            return response;
        } catch (Exception e) {
            e.printStackTrace();
            ResponseEntity<String> response = new ResponseEntity<>("Not found\n", HttpStatus.NOT_FOUND);
            return response;
        }

    }

    @RequestMapping("/{key}")
    public ResponseEntity<String> redirect(@PathVariable("key") String key, @NotNull HttpServletRequest request) {
        log.info("Request to get : " + request.getRequestURL().toString());
        String longUrl = shortenerService.getLongUrl(key);
        if (longUrl.isBlank()) {
            ResponseEntity<String> response = new ResponseEntity<>("Bad Request\n", HttpStatus.BAD_REQUEST);
            return response;
        }
        HttpHeaders headers = new HttpHeaders();
        headers.add("location", longUrl);
        ResponseEntity<String> response = new ResponseEntity<>("Redirecting\n",headers, HttpStatus.FOUND);
        return response;
    }
}
