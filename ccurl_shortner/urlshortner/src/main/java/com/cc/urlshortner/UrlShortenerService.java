package com.cc.urlshortner;

import com.cc.urlshortner.model.UrlData;
import com.cc.urlshortner.repo.UrlDataRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

@Service
public class UrlShortenerService {

    @Autowired
    private UrlDataRepo urlDataRepo;

    public void removeUrl(String key) {
        Optional<UrlData> byShortUrl = urlDataRepo.findByShortUrl(key);
        if(byShortUrl.isPresent()){
            String hash = byShortUrl.get().getHash();
            urlDataRepo.deleteById(hash);
        } else {
            throw new RuntimeException("Short Url does not exist");
        }
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

            Optional<UrlData> dataById = urlDataRepo.findById(base64Hash);
            if(dataById.isPresent()){
                shortUrl = dataById.get().getShortUrl();
                System.out.println(dataById.get());
                System.out.println("Found in DB");
            } else{
                shortUrl = getRandomKey();
                while(urlDataRepo.findByShortUrl(shortUrl).isPresent()){
                    System.out.println("Regenerating key because " + shortUrl + " already present in DB");
                    shortUrl = getRandomKey();
                }
                UrlData urlData = new UrlData();
                urlData.setHash(base64Hash);
                urlData.setShortUrl(shortUrl);
                urlData.setLongUrl(longUrl);
                urlDataRepo.save(urlData);
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

    public String getLongUrl(String key) {
        Optional<UrlData> byShortUrl = urlDataRepo.findByShortUrl(key);
        if (byShortUrl.isPresent()){
            String longUrl = byShortUrl.get().getLongUrl();
            System.out.println("Found in DB : " + longUrl);
            return longUrl;
        }
        return "";
    }
}
