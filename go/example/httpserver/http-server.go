package main

import (
	"fmt"
	"log"
	"net/http"
)

func pingPong(w http.ResponseWriter, req *http.Request) {
	w.Write([]byte("pong"))
}

func main()  {
	http.HandleFunc("/", func (w http.ResponseWriter, req *http.Request)  {
		w.Write([]byte("Hello World"))
		for k, v := range req.Header {
			fmt.Printf("Header field %q, Value %q\n", k, v)
		}
	})

	http.HandleFunc("/ping", pingPong)

	log.Fatal(http.ListenAndServe(":8080", nil))
}