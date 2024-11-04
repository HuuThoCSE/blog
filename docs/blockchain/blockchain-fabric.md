```
ssh-copy-id -i C:/Users/huuth/.ssh/id_rsa.pub fit@192.168.237.133
```

```
ssh fit@192.168.237.133
```

```
sudo apt update -y && sudo apt upgrade -y
```

```
sudo apt install -y curl
```

```
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
```

```
sudo apt install -y nodejs
```

```
node -v
```

```
curl -sSL https://bit.ly/2ysbOFE | bash -s
```

```
sudo apt-get install git -y
```

```
sudo apt-get install docker-compose -y
```

```
sudo systemctl start docker
```

```
sudo systemctl enable docker
```

```
sudo systemctl status docker
```

```
sudo apt install jq -y
```

```
docker --version
```

# Thêm quyền người dùng vào group docker
```
sudo usermod -aG docker ${USER}
```

# Reboot
```
sudo reboot
```

```
docker run hello-world
```

```
sudo snap install code --classic
```

```
sudo apt-get update
```

```
sudo npm install npm@6.14.17 -g
```

```
wget https://go.dev/dl/go1.23.2.linux-amd64.tar.gz
```


# Cài `go`
## Nếu là máy ảo vmware
```
sudo tar -C /usr/local -xzf go1.23.2.linux-amd64.tar.gz
```

## Nếu là máy jetsion
Tải của `arm`

## Gỡ cài đặt `go` cũ
```
sudo rm -rf /usr/local/go
```

### Cài lại go
```
sudo tar -C /usr/local -xzf go1.23.2.linux-arm64.tar.gz
```

```
sudo nano ~/.bashrc
```

```
export GOROOT=/usr/local/go
export PATH=$GOROOT/bin:$PATH
```

```
source ~/.bashrc
```

```
go version
```

```
mkdir -p $HOME/go/src/project1
```

```
cd ~/go/src/project1/
```

```
curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh && chmod +x install-fabric.sh
```

```
./install-fabric.sh
```

```
cd ~/go/src/project1/
cd fabric-samples/test-network
```

```
ls
```

```
cd ~/go/src/project1/fabric-samples/test-network
sudo ./network.sh down
```

```
sudo ./network.sh up
```

# Cập nhật docker compose
```
docker-compose --version
```

```
sudo rm /usr/local/bin/docker-compose
```

```
sudo curl -L "https://github.com/docker/compose/releases/download/latest/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```

```
reboot
```

```
docker-compose --version
```


## Khởi động mạng
```
cd ~/go/src/project1/fabric-samples/test-network
```

```
sudo ./network.sh up createChannel -ca -s couchdb
```

# Triển khai hợp đồng thông minh (chaincode)
```
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
```

```
cd ~/go/src/project1/fabric-samples/asset-transfer-basic/application-gateway-javascript/src	
```

```
npm install @grpc/grpc-js
```

```
sudo apt install build-essential -y
```

```
npm install @hyperledger/fabric-gateway
```

## Tạo tài sản mẫu
```
node app.js
```

## Cài đặt peer để truy vấn tài sản
```
npm install --save-dev --ignore-scripts install-peers
```

```
vi ~/.bashrc

export PATH=$PATH:$HOME/fabric-samples/bin
```

```
export HOME=/home/fit
export GOROOT=/usr/local/go
export PATH=$GOROOT/bin:$PATH
export PATH=$PATH:$HOME/fabric-samples/bin

export FABRIC_CFG_PATH=$HOME/go/src/project1/fabric-samples/config/
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_MSPCONFIGPATH=$HOME/go/src/project1/fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051
export CORE_PEER_TLS_ROOTCERT_FILE=$HOME/go/src/project1/fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_TLS_ENABLED=true
```

```
source ~/.bashrc
```

# Xem toàn bộ tài sản trong một tổ chức
```
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'
```

# Truy vấn tài sản
```
peer chaincode query -C mychannel -n basic -c '{"Args":["ReadAsset","asset1"]}'
```

# Tạo tổ chức mới
## Tạo folder
```
mkdir ~/go/src/project1/fabric-samples/test-network/addOrg3

```


```
cd addOrg3

./addOrg3.sh generate -c mychannel
```


```
vi ~/.bashrc

export CORE_PEER_LOCALMSPID="Org3MSP"
export CORE_PEER_ADDRESS=localhost:9051
```

```
source ~/.bashrc
```

```
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
```

## Kiếm tra xác nhận 
```
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'
```


# **TẠO CHAINCODE (Viết Chaincode trên Hyperledger Fabric đã cài đặt)**
## Trong thư mục fabric-sample tạo thư mục mychaincode
```
cd $HOME/go/src/project1
mkdir -p fabric-samples/chaincode/mychaincode
```

## Di chuyển vào thư mục mychaincode tạo module Go (go.mod)
```
cd fabric-samples/chaincode/mychaincode
```

(rm go.mod)

```
go mod init mychaincode
```

## Tải và quản lý các dependencies cho dự án:
```
go mod tidy
```

## Đóng gói chaincode
Sau khi đã khởi tạo go.mod và tải tất cả các dependencies, quay lại thư mục test-network và thử lại quá trình đóng gói chaincode.
```
cd ../../test-network
```

## Đóng gói
```
peer lifecycle chaincode package mychaincode.tar.gz \
--path ../chaincode/mychaincode \
--lang golang \
--label mychaincode_1.0
```
Lệnh này sẽ tạo file mychaincode.tar.gz cho chaincode của bạn.

## Cài đặt chaincode lên peer như trước đây:
```
peer lifecycle chaincode install mychaincode.tar.gz
```
***(chờ tầm 5-6 phút)***

## Deploy chaincode
```
./network.sh deployCC \
-ccn mychaincode \
-ccp ../chaincode/mychaincode \
-ccl go
```

## Kiểm tra đường dẫn tlsRootCertFiles của peer đang tương tác
```
ls organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/
```

## Kiểm tra đường dẫn đến tập tin tlsca.example.com-cert.pem
```
ls organizations/ordererOrganizations/example.com/msp/tlscacerts/
```

# Gọi chaincode đã triển khai 
Lưu ý: chắc chắn rằng dữ liệu được đồng bộ tới tất cả các peer.
```
peer chaincode invoke \
    -o 127.0.0.1:7050 \
    --ordererTLSHostnameOverride orderer.example.com \
    --tls \
    --cafile $HOME/go/src/project1/fabric-samples/test-network/organizations/ordererOrganizations/example.com/msp/tlscacerts/tlsca.example.com-cert.pem \
    -C mychannel \
    -n mychaincode \
    --peerAddresses localhost:7051 \
    --tlsRootCertFiles $HOME/go/src/project1/fabric-samples/test-network/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt \
    --peerAddresses localhost:9051 \
    --tlsRootCertFiles $HOME/go/src/project1/fabric-samples/test-network/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt \
    -c '{"Args":["Set","key1","value1"]}'
```

## Lấy giá trị của key, value
```
peer chaincode query \
-C mychannel \
-n mychaincode \
-c '{"Args":["Get", "key1"]}'
```

## Truy xuất khối mới nhất
```
peer channel fetch newest ./newest_block.block \
    -o 127.0.0.1:7050 \
    --ordererTLSHostnameOverride orderer.example.com \
    --tls \
    --cafile $HOME/go/src/project1/fabric-samples/test-network/organizations/ordererOrganizations/example.com/msp/tlscacerts/tlsca.example.com-cert.pem \
    -c mychannel
```

## Đổi block xuất ra file JSON
```
configtxlator proto_decode --input newest_block.block --type common.Block --output newest_block.json
```

## Xem thông tin giao dịch: 
```
cat newest_block.json
```