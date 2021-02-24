echo "Wait 5s"
sleep 5

go run client.go

echo "Wait 5s"
sleep 5

go run client.go

# mantain container running
tail -f /dev/null