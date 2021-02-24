echo "Wait 5s"
sleep 5

python client.py

echo "Wait 5s"
sleep 5

python client.py

# mantain container running
tail -f /dev/null
