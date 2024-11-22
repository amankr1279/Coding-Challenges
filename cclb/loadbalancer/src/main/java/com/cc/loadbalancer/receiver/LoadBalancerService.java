package com.cc.loadbalancer.receiver;

import com.cc.loadbalancer.client.CallBackend;
import org.springframework.stereotype.Service;

@Service
public class LoadBalancerService {

    private int requestCnt = 0;
    private int serverCount = 3;
    private final CallBackend callBackend = new CallBackend();
    private int getServerId() {
        requestCnt += 1;
        int serverId = requestCnt % serverCount + 1;

        /**
         * TODO: implement round-robin here
         * Send to only healthy servers []
         * Handle concurrent requests []
         * Upper limit of request Count handling []
         * Polling Healthy servers every 10 sec
        */

        return serverId;
    }

    public String makeHttpCallToBackend() {
        int serverId = getServerId();
        int port = 8080 + serverId;
        String backendResponse = callBackend.httpGETServer("http://localhost:" + String.valueOf(port));
        System.out.println("Received form BE:" + backendResponse);
        String loadBalancerResponse = "Altered at LB, Raw response: " + backendResponse;
        return loadBalancerResponse;
    }

    // Do periodic health check
    public void healthCheck() {

    }
}
