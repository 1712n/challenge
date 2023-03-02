package com.cryptoscams.api.hacks;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface HackRepo extends MongoRepository<Hack, Long> {
}
