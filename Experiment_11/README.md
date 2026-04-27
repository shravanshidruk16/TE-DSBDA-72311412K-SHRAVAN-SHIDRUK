# <div style='text-align: center'><u>Experiment 11 : MapReduce Log File Processing</u></div>

### <div align="center"> Name : Shravan Santosh Shidruk , PRN : 72311412K </div>

---
## Problem Statement
Design a distributed application using MapReduce which processes a log file of a system.

## Technologies Used
- Java
- Apache Hadoop MapReduce
- Ubuntu

## How to Run
```bash
1. Install Java
bashsudo apt update
sudo apt install openjdk-11-jdk -y
java -version

2. Install Hadoop
bash# Download Hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
# Extract
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop

3. Set environment variables
bashnano ~/.bashrc
Paste at the bottom:
bashexport JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
Then run:
bashsource ~/.bashrc

4. Verify Hadoop
bashhadoop version

5.Run Code
javac -classpath $(hadoop classpath) -d . LogMapper.java LogReducer.java LogProcessor.java
jar -cvf LogProcessor.jar *.class
hadoop jar LogProcessor.jar LogProcessor system.log output
cat output/part-r-00000
```

## Output
- Count of each HTTP status code (200, 404, 500)
- Access frequency of each URL
- Request count per IP address
