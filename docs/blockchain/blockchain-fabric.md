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
rm -rf /usr/local/go
```

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
./network.sh down
```

```
./network.sh up
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
./network.sh up createChannel -ca -s couchdb
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