import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WeatherAverage {

    public static void main(String[] args) {

        //Set input file path
        String fileName = "Sample_Weather.txt";

        //Step 2: Initialize accumulator variables
        double sumTemp  = 0.0;
        double sumDew   = 0.0;
        double sumWind  = 0.0;
        int    count    = 0;

        //Open and read the file line by line
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {

            String line;
            boolean isHeader = true;

            while ((line = br.readLine()) != null) {

                line = line.trim();

                // Skip empty lines
                if (line.isEmpty()) continue;

                // Skip the header row (first line)
                if (isHeader) {
                    isHeader = false;
                    continue;
                }

                //Step 4: Split line by comma
                String[] parts = line.split(",");

                if (parts.length < 4) {
                    System.out.println("Skipping malformed line: " + line);
                    continue;
                }

                //Extract and parse values
                // CSV format: Date, Temperature, DewPoint, WindSpeed
                double temperature = Double.parseDouble(parts[1].trim());
                double dewPoint    = Double.parseDouble(parts[2].trim());
                double windSpeed   = Double.parseDouble(parts[3].trim());

                //Accumulate sums
                sumTemp  += temperature;
                sumDew   += dewPoint;
                sumWind  += windSpeed;
                count++;

                System.out.printf("Read: Date=%-12s  Temp=%5.1f°C  Dew=%5.1f°C  Wind=%5.1f km/h%n",
                        parts[0].trim(), temperature, dewPoint, windSpeed);
            }

        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            System.err.println("Make sure sample_weather.txt is in the same folder.");
            return;
        } catch (NumberFormatException e) {
            System.err.println("Error parsing number: " + e.getMessage());
            return;
        }

        //Check if data was found
        if (count == 0) {
            System.out.println("No valid data rows found in the file.");
            return;
        }

        //Calculate averages
        double avgTemp = sumTemp / count;
        double avgDew  = sumDew  / count;
        double avgWind = sumWind / count;

        //Display results
        System.out.println();
        System.out.println("         WEATHER DATA ANALYSIS RESULTS          ");
        System.out.printf("  Total records processed : %d%n", count);
        System.out.println("------------------------------------------------");
        System.out.printf("  Average Temperature     : %.2f °C%n", avgTemp);
        System.out.printf("  Average Dew Point       : %.2f °C%n", avgDew);
        System.out.printf("  Average Wind Speed      : %.2f km/h%n", avgWind);
    }
}