package com.cc.loadbalancer.receiver;

import com.cc.loadbalancer.client.CallBackend;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;

@Service
@Slf4j
public class LoadBalancerService {

    private int requestCnt = 0;
    private final int serverCount = 3;
    private final CallBackend callBackend = new CallBackend();
    private final ObjectMapper objectMapper = new ObjectMapper();
    private int getServerId() {
        requestCnt += 1;
        int serverId = requestCnt % serverCount + 1;
        if(!healthCheck("server" + serverId)){
            log.debug("Server" + serverId + " is unhealthy");
            serverId += 1;
            serverId = serverId % serverCount + 1;
        }

        if(requestCnt == 100) {
            requestCnt = 0;
        }

        return serverId;
    }

    public String makeHttpCallToBackend() {
        int serverId = getServerId();
        int port = 8080 + serverId;
        log.info("Making backend call using {}", Thread.currentThread());
        String backendResponse = callBackend.httpGETServer("http://localhost:" + String.valueOf(port));
        log.debug("Received form BE:" + backendResponse );
        String loadBalancerResponse = "Altered at LB, Raw response: " + backendResponse;
        return loadBalancerResponse;
    }

    // Do periodic health check
    public Boolean healthCheck(String server) {
        try {
            JsonNode jsonNode = objectMapper.readTree(new File("../health_status.json"));
            Boolean status = jsonNode.get(server).asBoolean();
            log.debug(server + " status is " + status);
            return status;
        } catch (IOException e) {
            return false;
        }
    }

    public static void main(String[] args) {
        LoadBalancerService service = new LoadBalancerService();
        service.healthCheck("server1");
        service.healthCheck("server2");
        service.healthCheck("server3");
    }
}
