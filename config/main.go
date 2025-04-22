package config

import (
	"os"

	"gopkg.in/yaml.v3"
)

func GetConfig(path string) (*Config, error) {
	config := new(Config)
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	decoder := yaml.NewDecoder(f)

	err = decoder.Decode(config)
	if err != nil {
		return nil, err
	}

	return config, nil
}
