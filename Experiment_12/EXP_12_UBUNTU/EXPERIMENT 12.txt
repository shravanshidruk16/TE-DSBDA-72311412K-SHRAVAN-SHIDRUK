EXPERIMENT 12

Locate dataset (e.g., sample_weather.txt) for working on weather data which reads the text input files and finds average for temperature, dew point and wind speed.

==================== WeatherMapper.java ====================

• Purpose:
  - Acts as the Mapper phase in Hadoop MapReduce
  - Reads weather dataset line by line
  - Converts weather records into intermediate key-value pairs

• Main Functions:
  - Skips header line
  - Splits CSV data using comma (,)
  - Extracts:
      → Temperature
      → Dew Point
      → Wind Speed

• Emits Intermediate Key-Value Pairs:
      WEATHER → 28.5,18.2,12.4,1
      WEATHER → 30.1,19.5,15.0,1

• Important Points:
  - Mapper does NOT calculate averages
  - Only emits weather values for processing
  - Runs in parallel on distributed systems

============================================================

==================== WeatherReducer.java ====================

• Purpose:
  - Acts as the Reducer phase in Hadoop MapReduce
  - Receives grouped weather values from Hadoop

• Main Functions:
  - Receives:
      WEATHER → [all weather records]

  - Calculates:
      → Total Temperature
      → Total Dew Point
      → Total Wind Speed
      → Total Record Count

  - Computes:
      → Average Temperature
      → Average Dew Point
      → Average Wind Speed

• Final Output Example:
      Average Temperature : 29.9187 °C
      Average Dew Point   : 19.9000 °C
      Average Wind Speed  : 15.0824 km/h

• Important Points:
  - Performs actual average calculations
  - Generates final analytics output
  - Works after Shuffle & Sort phase

=============================================================

==================== WeatherDriver.java ====================

• Purpose:
  - Driver/Main class of Hadoop weather program
  - Controls complete MapReduce execution

• Main Functions:
  - Creates Hadoop job configuration
  - Connects:
      → WeatherMapper
      → WeatherReducer

  - Sets:
      → Input dataset path
      → Output folder path
      → Output key/value data types

• Controls Entire Workflow:
      Weather Dataset
             ↓
          Mapper
             ↓
      Shuffle & Sort
             ↓
          Reducer
             ↓
       Final Output

• Important Points:
  - Starts Hadoop job execution
  - Manages complete processing flow
  - Responsible for Hadoop job configuration

============================================================



Step 1: Install Java
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version

Step 2: Download and Install Hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/Hadoop

Step 3: Set Environment Variables
nano ~/.bashrc

Paste at bottom:

export JAVA_HOME=/usr/lib/jvm/default-java
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
*****Ctrl + 0 then Enter then Ctrl + X (to save and exit the changes)*****

Apply changes:

source ~/.bashrc

Step 4: Verify Hadoop Installation
hadoop version

Step 5 : Paste all the files 
1. Sample_Weather.txt
2. WeatherMapper.java
3. WeatherReducer.java
4. WeatherDriver.java

Step 6 : Compilation
javac -classpath $(hadoop classpath) -d . WeatherMapper.java WeatherReducer.java WeatherDriver.java

Step 7 : Create Jar File
jar -cvf WeatherAnalysis.jar *.class

Step 8 : Run Hadoop Job
hadoop jar WeatherAnalysis.jar WeatherDriver Sample_Weather.txt output

Step 9 : View Output 
cat output/part-r-00000

