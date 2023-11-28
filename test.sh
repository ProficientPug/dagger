#! /usr/bin/bash

echo "Welcome to hadoop Installation"
# Updataing the system
sudo apt update

# Installing and setting up SSH

# Check if OpenSSH Server is installed
if ! dpkg -l | grep openssh-server; then
    echo "OpenSSH Server is not installed."
else
    # Stop the SSH service
    sudo service ssh stop

    # Uninstall OpenSSH Server
    sudo apt-get purge openssh-server
    sudo apt-get autoremove
    sudo apt-get clean

    echo "OpenSSH Server has been removed."

sudo apt install openssh-server

sudo service ssh start

ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

chmod 0600 ~/.ssh/authorized_keys

# Installing Java


# Check if Java is installed
if type -p java; then
    echo "Java is already installed."
else
    # Install OpenJDK 1.8
    echo "Java not found. Installing OpenJDK 1.8..."
    
    # Check if the package manager is apt or yum
    if [ -n "$(command -v apt-get)" ]; then
        sudo apt-get update
        sudo apt-get install openjdk-8-jdk
    elif [ -n "$(command -v yum)" ]; then
        sudo yum install java-1.8.0-openjdk
    else
        echo "Unsupported package manager. Please install Java manually."
        exit 1
    fi

    # Check if the installation was successful
    if type -p java; then
        echo "Java installation successful."
    else
        echo "Java installation failed. Please install Java manually."
        exit 1
    fi

java -version

# Installing Hadoop

cd ~
mkdir hadoop

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz

tar -zxf hadoop-3.2.0.tar.gz -C ~/hadoop

cd ~/hadoop/hadoop-3.2.0/

# Adding Path variables

echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=~/hadoop/hadoop-3.2.0
export PATH=\$PATH:\$HADOOP_HOME/bin
export PATH=\$PATH:\$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=\$HADOOP_HOME/etc/hadoop
export HADOOP_MAPRED_HOME=\$HADOOP_HOME
export HADOOP_COMMON_HOME=\$HADOOP_HOME
export HADOOP_HDFS_HOME=\$HADOOP_HOME
export YARN_HOME=\$HADOOP_HOME" >> ~/.bashrc

# update the bash file 
source ~/.bashrc

# Checking java and hadoop
java -version
hadoop version

cd ~/hadoop/hadoop-3.2.0/etc/hadoop

echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> hadoop-env.sh

core="    <property>\n    <name>fs.defaultFS</name>\n    <value>hdfs://localhost:9000</value>\n    </property>"
hdfs="    <property>\n    <name>dfs.replication</name>\n    <value>1</value>\n    </property>"
mapred="    <property>\n         <name>mapreduce.framework.name</name>        <value>yarn</value>\n    </property>\n    <property>\n    <name>mapreduce.application.classpath</name>\n    <value>\$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:\$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>\n    </property>"
yarn="    <property>\n  <name>yarn.nodemanager.aux-services</name>\n        <value>mapreduce_shuffle</value>\n    </property>\n   <property>\n        <name>yarn.nodemanager.env-whitelist</name>\n       <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>\n    </property>"

# Replacing core-site.xml
sed -i "/<configuration>/a \\
$core" "core-site.xml"

# Replacing hdfs-site.xml
sed -i "/<configuration>/a \\
$hdfs" "hdfs-site.xml"

# Replacing mapred-site.xml
sed -i "/<configuration>/a \\
$mapred" "mapred-site.xml"

# Replacing yarn-site.xml
sed -i "/<configuration>/a \\
$yarn" "yarn-site.xml"

# replacements done

cd ~/hadoop/hadoop-3.2.0

# formatting Namenode
bin/hdfs namenode -format

# starting daemons
sbin/start-dfs.sh
sbin/start-yarn.sh


# final check 
jps