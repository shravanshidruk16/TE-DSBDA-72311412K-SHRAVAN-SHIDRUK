# <div align="center"><u>Experiment 12 : Weather Data Analysis using Java File Handling</u></div>

### <div align="center"> Name : Shravan Santosh Shidruk , PRN : 72311412K </div>

---

## Problem Statement

Locate a dataset (sample_weather.txt) for working on weather data which reads the text input files and finds the **average Temperature, Dew Point, and Wind Speed**.

---

## Technologies Used

- Java (JDK 8 or above)
- File Handling using `BufferedReader` and `FileReader`
- Ubuntu / Linux Terminal

---


## Dataset Format (sample_weather.txt)

The file is comma-separated with the following columns:

```
Date, Temperature (°C), DewPoint (°C), WindSpeed (km/h)
```

Example:
```
Date,Temperature,DewPoint,WindSpeed
2024-01-01,28.5,18.2,12.4
2024-01-02,30.1,19.5,15.0
...
```

---

## Algorithm

1. Start
2. Input: `sample_weather.txt`
3. Open file in read mode using `BufferedReader`
4. Skip the header line
5. Initialize: `sumTemp = 0`, `sumDew = 0`, `sumWind = 0`, `count = 0`
6. For each line:
   - Split by comma
   - Extract Temperature (index 1), DewPoint (index 2), WindSpeed (index 3)
   - Convert to `double` using `Double.parseDouble()`
   - Add to respective sums
   - Increment `count`
7. Calculate:
   - `avgTemp = sumTemp / count`
   - `avgDew  = sumDew  / count`
   - `avgWind = sumWind / count`
8. Display results
9. Close file (handled automatically by try-with-resources)
10. Stop

---

## How to Run on Ubuntu

### Step 1: Install Java

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
java -version
```

### Step 2: Compile the Java file

```bash
javac WeatherAverage.java
```
### Step 3: Run the program

```bash
java WeatherAverage
```
