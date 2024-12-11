package com.cc.urlshortner;

import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

@Service
public class UrlShortenerService {

    private final ArrayList<UrlData> mockDB = new ArrayList<>();

    public void removeUrl() {

    }

    public String shortenUrl(String longUrl) {
        String shortUrl = "";
        /**
         * SHA 256 hash the url
         * Check if it already exists in DB
         * If yes then return that else add and return
         */

        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] encodedHash = digest.digest(longUrl.getBytes(StandardCharsets.UTF_8));
            String hexHash = HexFormat.of().formatHex(encodedHash);
            String base64Hash = Base64.getEncoder().encodeToString(encodedHash);
            System.out.println("Hex hash : "+ hexHash);
            System.out.println("base64 hash : "+ base64Hash);

            boolean alreadyExists = false;
            for (UrlData data: mockDB) {
                if(Objects.equals(data.getHash(), base64Hash)) {
                   alreadyExists = true;
                    System.out.println(data);
                    shortUrl = data.getKey();
                    System.out.println("Found in DB");
                   break;
                }
            }

            if(!alreadyExists) {
               shortUrl = getRandomKey();

                mockDB.add(new UrlData.UrlDataBuilder()
                        .key(shortUrl)
                        .hash(base64Hash)
                        .longUrl(longUrl)
                        .build());
            }

        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
        return shortUrl;
    }

    private String getRandomKey() {
        String key = "";
        for (int i = 0; i < 6; i++) {

            Random random = new Random();
            int upperBound = 36; // 0-9 numbers and a-z letters
            int randomNumber = random.nextInt(upperBound);
            String alphabets = "abcdefghijklmnopqrstuvwxyz";
            if(randomNumber >= 10) {
                Character letter = alphabets.charAt(randomNumber - 10);
                key = key.concat(String.valueOf(letter));
            } else {
                key = key.concat(String.valueOf(randomNumber));
            }
        }
        System.out.println("Generated random key: " + key);
        return key;
    }
}
