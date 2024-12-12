package com.cc.urlshortner.model;

import jakarta.persistence.Column;
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
    @Id
    private String hash;
    @Column(unique = true)
    private String shortUrl;
    private String longUrl;

    @Override
    public String toString() {
        return "UrlData{" +
                "key='" + shortUrl + '\'' +
                ", longUrl='" + longUrl + '\'' +
                ", hash='" + hash + '\'' +
                '}';
    }
}
