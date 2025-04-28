package config_test

import (
	"log"
	"testing"

	"github.com/Azat201003/eduflow_service_api/config"
)

func TestGetting(t *testing.T) {
	conf, err := config.GetConfig("example.yaml")
	if err != nil {
		t.Fatalf("Error with getting config: %v", err)
	}
	log.Println(conf)
}
