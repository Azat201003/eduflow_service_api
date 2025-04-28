package config

import "errors"

type DBConnect struct {
	User     string `yaml:"user"`
	DB       string `yaml:"database"`
	Schema   string `yaml:"schema"`
	Password string `yaml:"password"`
}

type RedisConnect struct {
	User     string `yaml:"user"`
	DB       uint   `yaml:"db"`
	Protocol uint   `yaml:"protocol"`
	Password string `yaml:"password"`
}

type Service struct {
	Name         string        `yaml:"name"`
	Description  string        `yaml:"description"`
	Host         string        `yaml:"host"`
	Port         uint          `yaml:"port"`
	ID           uint          `yaml:"id"`
	DBConnect    *DBConnect    `yaml:"db"`
	RedisConnect *RedisConnect `yaml:"redis"`
}

type Database struct {
	Host string `yaml:"host"`
	Port uint   `yaml:"port"`
}

type Redis struct {
	Host string `yaml:"host"`
	Port uint   `yaml:"port"`
}

type Config struct {
	Services []*Service `yaml:"services"`
	Database *Database  `yaml:"db"`
	Redis    *Redis     `yaml:"redis"`
}

func (config *Config) GetServiceById(id uint) (*Service, error) {
	for _, service := range config.Services {
		if service.ID == id {
			return service, nil
		}
	}
	return nil, errors.New("Not found")
}
