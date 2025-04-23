package config

import "errors"

type DBConnect struct {
	user     string `yaml:"user"`
	db       string `yaml:"database"`
	schema   string `yaml:"schema"`
	password string `yaml:"password"`
}

type Service struct {
	Name        string     `yaml:"name"`
	Description string     `yaml:"description"`
	Host        string     `yaml:"host"`
	Port        uint       `yaml:"port"`
	ID          uint       `yaml:"id"`
	Connect     *DBConnect `yaml:"db"`
}

type Database struct {
	Host string `yaml:"host"`
	Port uint   `yaml:"port"`
}

type Config struct {
	Services []*Service `yaml:"services"`
	Database *Database  `yaml:"db"`
}

func (config *Config) GetServiceById(id uint) (*Service, error) {
	for _, service := range config.Services {
		if service.ID == id {
			return service, nil
		}
	}
	return nil, errors.New("Not found")
}
