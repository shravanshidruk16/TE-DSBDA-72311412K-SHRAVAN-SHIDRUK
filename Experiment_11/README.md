# <div align="center"><u>Experiment 11 : MapReduce Log File Processing</u></div>

### <div align="center"> Name : Shravan Santosh Shidruk , PRN : 72311412K </div>

---

## Problem Statement

Design a distributed application using MapReduce which processes a log file of a system.

---

## Technologies Used

* Java
* Apache Hadoop 3.3.6
* Ubuntu (Single Node Setup)

---

## Theory

Hadoop MapReduce is a programming model used for processing large datasets in a distributed manner.
In this experiment, we process system log files to:

* Count HTTP status codes
* Count URL access frequency
* Count requests per IP address

---

## Steps to Execute

### Step 1: Install Java

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
```

---

### Step 2: Download and Install Hadoop

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop
```

---

### Step 3: Set Environment Variables

```bash
nano ~/.bashrc
```

Paste at bottom:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

Apply changes:

```bash
source ~/.bashrc
```

---

### Step 4: Verify Hadoop Installation

```bash
hadoop version
```

---

### Step 5: Create Project Directory

```bash
mkdir logprocessor
cd logprocessor
```

Copy files:

* LogMapper.java
* LogReducer.java
* LogProcessor.java
* system.log

---

### Step 6: Compile Java Files  ✅ (IMPORTANT FIX)

```bash
javac -classpath $(hadoop classpath) -d . LogMapper.java LogReducer.java LogProcessor.java
```

---

### Step 7: Create JAR File

```bash
jar -cvf LogProcessor.jar *.class
```

---

### Step 8: Run Hadoop Job (Local Mode)

```bash
hadoop jar LogProcessor.jar LogProcessor system.log output
```

⚠️ If output folder exists:

```bash
rm -r output
```

---

### Step 9: Display Output

```bash
cat output/part-r-00000
```

---

## Output Explanation

The program generates:

* STATUS_200 → Count of successful requests

* STATUS_404 → Not found errors

* STATUS_500 → Server errors

* URL_/home → URL access frequency

* URL_/login → URL access frequency

* IP_192.168.x.x → Requests per IP

---

## Sample Output

```
STATUS_200    4
STATUS_404    2
STATUS_500    1

URL_/home     2
URL_/login    1
URL_/dashboard 1

IP_10.0.0.5   2
IP_192.168.1.10 2
```

---

## Conclusion

We have successfully implemented a distributed MapReduce application to process system log files and extract meaningful insights such as status counts, URL frequency, and IP access statistics.

---
