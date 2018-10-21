IMGURL="https://s3.eu-central-1.amazonaws.com/faas-evaluation/testimage.png"
ITERATIONS="100"

python3 main.py openfaas http://35.157.150.146:8080/function/image-resizer $IMGURL $ITERATIONS
python3 main.py wsk http://3.120.137.21:9090/api/23bc46b1-71f6-4ed5-8c54-816aa4f8c502/guest/imageResizer $IMGURL $ITERATIONS
python3 main.py aws https://rl2tpkf0k5.execute-api.eu-central-1.amazonaws.com/default/imageResizer $IMGURL $ITERATIONS
python3 main.py gce https://europe-west1-faas-216715.cloudfunctions.net/imageResizer $IMGURL $ITERATIONS