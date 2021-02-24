package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"
)

const (
	hostname string = "server"
	port     string = "8000"
)

func main() {

	addrs, err := net.LookupHost(hostname)
	checkError(err)

	fmt.Println("Server address: ", addrs, ":", port)

	// service: address:8000
	service := addrs[0] + ":" + port

	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	checkError(err)

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	checkError(err)

	message := "Hello from GO"
	fmt.Println("Send message: ", message)
	_, err = conn.Write([]byte(message))
	checkError(err)

	result, err := ioutil.ReadAll(conn)
	checkError(err)

	fmt.Println("Receive message: " + string(result))
	os.Exit(0)

}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}
