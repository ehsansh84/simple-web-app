NAMESPACE=swapp
USER=Ehsan
SERVER_IP=server_ip
openssl genrsa -out $USER.key 2048
openssl req -new -key $USER.key -out $USER.csr -subj "/CN=swapp.devserver.ir/O=$NAMESPACE"
scp ubuntu@$SERVER_IP:/etc/kubernetes/pki/ca.{crt,key} .
openssl x509 -req -in $USER.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out $USER.crt -days 365
kubectl create -n $NAMESPACE secret tls swapp-tls --cert=$USER.crt --key=$USER.key
