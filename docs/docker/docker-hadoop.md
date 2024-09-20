# Sử dụng Docker Hadoop Image
```
docker pull bde2020/hadoop-namenode
```

```
sudo apt update
```


```
sudo apt install docker-compose
```

Tạo file docker-compose.yml:
```yml
version: '2'
services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    environment:
      - CLUSTER_NAME=test
    ports:
      - "9870:9870"
      - "9000:9000"
    volumes:
      - /tmp/namenode:/hadoop/dfs/name
    networks:
      - hadoop
    command: namenode -format

  datanode:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8
    container_name: datanode
    environment:
      - CLUSTER_NAME=test
    ports:
      - "9864:9864"
    volumes:
      - /tmp/datanode:/hadoop/dfs/data
    networks:
      - hadoop
    depends_on:
      - namenode

  resourcemanager:
    image: bde2020/hadoop-resourcemanager:2.0.0-hadoop3.2.1-java8
    container_name: resourcemanager
    ports:
      - "8088:8088"
    networks:
      - hadoop
    depends_on:
      - namenode

  nodemanager:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.2.1-java8
    container_name: nodemanager
    networks:
      - hadoop
    depends_on:
      - resourcemanager

networks:
  hadoop:
    driver: bridge
```
## Chạy cụm Hadoop với Docker Compose
```bash
docker-compose up
```


---

## Cài java
```
apt install openjdk-21-jre-headless
```

## Tạo file `docker-compose.yml`
```
vim docker-compose.yml
```

```yml
version: "3"
services:
   namenode:
      image: apache/hadoop:3.3.6
      hostname: namenode
      command: ["hdfs", "namenode"]
      ports:
        - 9870:9870
      env_file:
        - ./config
      environment:
          ENSURE_NAMENODE_DIR: "/tmp/hadoop-root/dfs/name"
   datanode:
      image: apache/hadoop:3.3.6
      command: ["hdfs", "datanode"]
      env_file:
        - ./config
   resourcemanager:
      image: apache/hadoop:3
      hostname: resourcemanager
      command: ["yarn", "resourcemanager"]
      ports:
         - 8088:8088
      env_file:
        - ./config
      volumes:
        - ./test.sh:/opt/test.sh
   nodemanager:
      image: apache/hadoop:3
      command: ["yarn", "nodemanager"]
      env_file:
        - ./config
```

## Tạo file config
```
vim config
```

```
CORE_SITE_XML_fs_default_name=hdfs://namenode
CORE_SITE_XML_fs_defaultFS=hdfs://namenode
HDFS_SITE_XML_dfs_namenode_rpc_address=namenode:8020
HDFS_SITE_XML_dfs_replication=1
MAPRED_SITE_XML_mapreduce_framework_name=yarn
MAPRED_SITE_XML_yarn_app_mapreduce_am_env=HADOOP_MAPRED_HOME=$HADOOP_HOME
MAPRED_SITE_XML_mapreduce_map_env=HADOOP_MAPRED_HOME=$HADOOP_HOME
MAPRED_SITE_XML_mapreduce_reduce_env=HADOOP_MAPRED_HOME=$HADOOP_HOME
YARN_SITE_XML_yarn_resourcemanager_hostname=resourcemanager
YARN_SITE_XML_yarn_nodemanager_pmem_check_enabled=false
YARN_SITE_XML_yarn_nodemanager_delete_debug_delay_sec=600
YARN_SITE_XML_yarn_nodemanager_vmem_check_enabled=false
YARN_SITE_XML_yarn_nodemanager_aux_services=mapreduce_shuffle
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_maximum_applications=10000
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_maximum_am_resource_percent=0.1
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_resource_calculator=org.apache.hadoop.yarn.util.resource.DefaultResourceCalculator
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_queues=default
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_capacity=100
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_user_limit_factor=1
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_maximum_capacity=100
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_state=RUNNING
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_acl_submit_applications=*
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_root_default_acl_administer_queue=*
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_node_locality_delay=40
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_queue_mappings=
CAPACITY_SCHEDULER_XML_yarn_scheduler_capacity_queue_mappings_override_enable=false
```

## Khởi động lại container
```bash
docker compose restart nodemanager
```

## Kiểm tra lại trạng thái container
```
docker compose ps
```

## Cập nhật lại docker nếu có thay đổi docker-compose.yml
```
docker compose up -d
```


# Khởi động lại Docker Compose
```
docker compose down
docker compose up -d
```

https://hub.docker.com/r/apache/hadoop


```
docker exec -it docker-3_namenode_1 /bin/bash 
```

```
yarn jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 10 15
```