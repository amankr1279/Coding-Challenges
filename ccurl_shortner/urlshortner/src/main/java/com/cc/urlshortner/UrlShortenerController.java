package com.cc.urlshortner;

import com.cc.urlshortner.model.AddUrlRequest;
import com.cc.urlshortner.model.AddUrlResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.net.http.HttpResponse;

@RestController
public class UrlShortenerController {

    @Autowired
    private UrlShortenerService shortenerService;

    @PostMapping("/add")
    public ResponseEntity<AddUrlResponse> postURL(@RequestBody AddUrlRequest body) {
        System.out.println(body.toString());
        String shortUrl = shortenerService.shortenUrl(body.getLongUrl());
        AddUrlResponse addUrlResponse = new AddUrlResponse();
        addUrlResponse.setShortUrl("http://localhost:8080/" + shortUrl);
        addUrlResponse.setLongUrl(body.getLongUrl());
        addUrlResponse.setKey(shortUrl);
        ResponseEntity<AddUrlResponse> response = new ResponseEntity<AddUrlResponse>(addUrlResponse, HttpStatus.OK);
        return response;
    }

    @DeleteMapping("/remove")
    public void removeUrl() {

    }
}
