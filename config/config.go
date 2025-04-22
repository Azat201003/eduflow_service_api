package config

type Service struct {
	Name        string `yaml:"name"`
	Description string `yaml:"description"`
	Host        string `yaml:"host"`
	Port        int    `yaml:"port"`
	ID          int    `yaml:"id"`
	DB_user     string `yaml:"db_user"`
	DB          string `yaml:"db"`
}

type Database struct {
	Host string `yaml:"host"`
	Port int    `yaml:"port"`
}

type Config struct {
	Services []*Service `yaml:"services"`
	Database Database   `yaml:"db"`
}
