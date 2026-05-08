import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class WeatherReducer
        extends Reducer<Text, Text, Text, Text> {

    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {

        double sumTemp = 0;
        double sumDew = 0;
        double sumWind = 0;
        int count = 0;

        for (Text val : values) {

            String[] data = val.toString().split(",");

            double temp = Double.parseDouble(data[0]);
            double dew = Double.parseDouble(data[1]);
            double wind = Double.parseDouble(data[2]);

            sumTemp += temp;
            sumDew += dew;
            sumWind += wind;

            count++;
        }

        double avgTemp = sumTemp / count;
        double avgDew = sumDew / count;
        double avgWind = sumWind / count;

        // Better formatted output
        String result =
                "\nAverage Temperature : " + String.format("%.4f", avgTemp) + " °C"
                + "\nAverage Dew Point   : " + String.format("%.4f", avgDew) + " °C"
                + "\nAverage Wind Speed  : " + String.format("%.4f", avgWind) + " km/h";

        // Empty key removes WEATHER word
        context.write(new Text(""), new Text(result));
    }
}
