package com.cc.loadbalancer.client;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;

public class CallBackend {
    private int serverNum = 1;
    private final String[] backendServerUrls = {"http://localhost:8081", "http://localhost:8082", "http://localhost:8083"};
    public int getServerNum() {
        return serverNum;
    }

    public void setServerNum(int serverNum) {
        this.serverNum = serverNum;
    }


    /**
     * Make GET Call to Backend Server
     * @param url Backend Server URL
     * @return String
     * @throws RuntimeException
     */
    public String httpGETServer(String url) {
        String result;
        try {
            HttpRequest httpRequest = HttpRequest.newBuilder()
                    .GET()
                    .uri(URI.create(url))
                    .timeout(Duration.ofSeconds(10))
                    .build();

            System.out.println(httpRequest.toString());

            HttpClient client = HttpClient.newBuilder().build();

            HttpResponse<String> httpResponse = client.send(httpRequest, HttpResponse.BodyHandlers.ofString());

            System.out.println(httpResponse.body());
            result = httpResponse.body();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }

        return result;
    }

    /**
     *
     * @param url Backend Server health check URL
     * @return
     */
    public String healthCheck(String url) {
        String response = httpGETServer(url);

        return response;
    }

    public static void main(String[] args) throws InterruptedException {
        CallBackend callBackend = new CallBackend();
        for (String url: callBackend.backendServerUrls) {
            Thread.sleep(500);
            callBackend.httpGETServer(url);
        }

    }
}
