package com.cc.urlshortner;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UrlData {
    private String key;
    private String longUrl;
    @Id
    private String hash;

    @Override
    public String toString() {
        return "UrlData{" +
                "key='" + key + '\'' +
                ", longUrl='" + longUrl + '\'' +
                ", hash='" + hash + '\'' +
                '}';
    }
}
