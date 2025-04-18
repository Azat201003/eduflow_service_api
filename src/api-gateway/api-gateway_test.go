package main

import (
	"net/http"
	"testing"
)

func TestMainPage(t *testing.T) {
	response, err := http.Get("http://localhost:8080/")
	if err != nil {
		t.Errorf("Error with requesting: %v", err)
	}
	defer response.Body.Close()
	bs := make([]byte, 1024)
	n, err := response.Body.Read(bs)
	text := string(bs[:n])
	if text != "Hello, world!" {
		t.Errorf("Bad response: \"%v\"", text)
	}
}
