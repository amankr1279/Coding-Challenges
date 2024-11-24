package com.cc.loadbalancer.receiver;

import lombok.extern.slf4j.Slf4j;
import org.jetbrains.annotations.NotNull;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

/**
 * Receive call from FE
 * Send them to service
 * Service will then make call to backend
 * get the backend server's response
 * relay it to balancer
 * balance will then forward it to FE
 * */

@RestController
@Slf4j
public class LoadBalancerController {

    @Autowired
    private LoadBalancerService loadBalancerService;

    /**
     * Receive GET Requests from Client
     */
    @GetMapping("/home")
    public String getBalancer(@RequestHeader @NotNull HttpHeaders httpHeaders) {
        log.debug("Get load balancer");
        Map<String, String> headerMap = httpHeaders.toSingleValueMap();
        for (Map.Entry<String, String> entry: headerMap.entrySet()) {
            log.debug(entry.getKey() + ":\t" + entry.getValue());
        }

        String backendResponse = loadBalancerService.makeHttpCallToBackend();

        return backendResponse;
    }
}
