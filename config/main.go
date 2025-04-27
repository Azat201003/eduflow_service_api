package config

import (
	"os"

	"gopkg.in/yaml.v3"
)

func GetConfig(path string) (*Config, error) {
	config := new(Config)
	f, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	err = yaml.Unmarshal(f, config)

	if err != nil {
		return nil, err
	}

	return config, nil
}
