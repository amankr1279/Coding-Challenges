package com.cc.urlshortner.repo;

import com.cc.urlshortner.model.UrlData;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UrlDataRepo extends JpaRepository<UrlData, String> {

}
