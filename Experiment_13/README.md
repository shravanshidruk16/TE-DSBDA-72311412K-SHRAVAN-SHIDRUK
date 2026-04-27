# <div align="center"><u>Experiment 13 : Word Count using Scala and Apache Spark Framework</u></div>

### <div align="center"> Name : Shravan Santosh Shidruk , PRN : 72311412K </div>

---

## Problem Statement

Write a simple program using **SCALA** and **Apache Spark Framework** that reads a text input file (`sample_input.txt`) and finds the **count of each word** in the file using Spark RDD transformations and actions.

---

## Technologies Used

- Scala (2.12 or above)
- Apache Spark (3.x) with SparkContext and RDD
- Java (JDK 8 or above)
- Ubuntu / Linux Terminal

---

## Algorithm

1. Start
2. Input: `sample_input.txt`
3. Initialize SparkConf and SparkContext with `setMaster("local[*]")`
4. Load text file into RDD using `sc.textFile()`
5. Split each line into words using `flatMap()` (Transformation-1)
6. Map each word to `(word, 1)` using `map()` (Transformation-2)
7. Reduce by key to sum all counts using `reduceByKey(_ + _)`
8. Sort results by count in descending order using `sortBy()`
9. Collect and display word count results using `collect().foreach()`
10. Stop SparkContext using `sc.stop()`
11. Stop

---

## How to Run on Ubuntu

### Step 1: Install Java

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
```

### Step 2: Install Scala

```bash
sudo apt install scala -y
scala -version
```

### Step 3: Download and Set Up Apache Spark

```bash
wget https://downloads.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar -xvzf spark-3.5.0-bin-hadoop3.tgz
sudo mv spark-3.5.0-bin-hadoop3 /opt/spark
```

### Step 4: Set Environment Variables

```bash
nano ~/.bashrc
```

Add the following lines at the bottom:

```bash
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

Apply the changes:

```bash
source ~/.bashrc
```

### Step 5: Compile the Scala file

```bash
scalac -classpath "$SPARK_HOME/jars/*" WordCount.scala
```

This creates `WordCount.class` in the same folder.

### Step 6: Create a JAR file

```bash
jar -cf wordcount.jar *.class
```

### Step 7: Run the program

```bash
spark-submit --class WordCount --master local[*] wordcount.jar
```
