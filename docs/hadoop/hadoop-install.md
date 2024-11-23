
# File edit
## core-site.xml
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://192.168.237.131:9000</value>
    </property>
    <property>
        <name>hadoop.http.staticuser.user</name>
        <value>hdoop</value>
    </property>
</configuration>
```

## hdfs-site.xml
```
sudo vim /usr/local/hadoop/etc/hadoop/hdfs-site.xml
```

```
<configuration>

    <!-- Cấu hình số lượng bản sao của block -->
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>

    <!-- Địa chỉ RPC mà NameNode sử dụng -->
    <property>
        <name>dfs.namenode.rpc-address</name>
        <value>node1:9000</value>
    </property>

    <!-- Đường dẫn lưu trữ metadata cho NameNode -->
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop_tmp/hdfs/namenode</value>
    </property>

    <!-- Đường dẫn lưu trữ dữ liệu cho DataNode -->
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop_tmp/hdfs/datanode</value>
    </property>

</configuration>
```

# Worker or Slave
Hadoop 3.x và mới hơn: Tệp được đặt tên là workers.

Hadoop 2.x và cũ hơn: Tệp được đặt tên là slaves.

```
sudo vi $HADOOP_HOME/etc/hadoop/workers

$HADOOP_HOME/etc/hadoop/slaves
```

```
node1
node2
```

# Java
```
readlink -f $(which java)
```

```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

```
sudo vi /usr/local/hadoop/etc/hadoop/hadoop-env.sh
```

```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```


# Bashrc Hadoop
```
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
```