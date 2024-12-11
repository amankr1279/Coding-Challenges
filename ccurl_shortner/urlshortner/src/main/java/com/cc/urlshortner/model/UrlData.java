package com.cc.urlshortner.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class UrlData {
    private String shortUrl;
    private String longUrl;
    @Id
    private String hash;

    @Override
    public String toString() {
        return "UrlData{" +
                "key='" + shortUrl + '\'' +
                ", longUrl='" + longUrl + '\'' +
                ", hash='" + hash + '\'' +
                '}';
    }
}
