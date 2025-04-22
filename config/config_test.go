package config

import (
	"log"
	"testing"
)

func TestGetting(t *testing.T) {
	conf, err := GetConfig("../config.yaml")
	if err != nil {
		log.Fatalf("Error with getting config: %v", err)
	}
	log.Println(conf)
}
