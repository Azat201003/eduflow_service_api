package config

import (
	"os"
	"path/filepath"

	"gopkg.in/yaml.v3"
)

func GetConfig() (*Config, error) {
	config := new(Config)
	pwd, err := os.Getwd()
	if err != nil {
		return nil, err
	}
	path := (filepath.Dir(pwd)) + "/config.yaml"
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
