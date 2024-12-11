package com.cc.urlshortner.model;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AddUrlRequest {
    private String longUrl;

    @Override
    public String toString() {
        return "AddUrlRequest{" +
                "longUrl='" + longUrl + '\'' +
                '}';
    }

}
