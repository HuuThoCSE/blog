

# Worker or Slave
Hadoop 3.x và mới hơn: Tệp được đặt tên là workers.

Hadoop 2.x và cũ hơn: Tệp được đặt tên là slaves.

```
sudo nano vi $HADOOP_HOME/etc/hadoop/workers

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
nano /usr/local/hadoop/etc/hadoop/hadoop-env.sh
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