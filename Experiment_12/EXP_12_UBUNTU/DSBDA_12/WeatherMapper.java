import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.io.LongWritable;

public class WeatherMapper
        extends Mapper<LongWritable, Text, Text, Text> {

    private final static Text outKey = new Text("WEATHER");
    private final Text outValue = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        String line = value.toString().trim();

        // Skip empty lines
        if (line.isEmpty()) {
            return;
        }

        // Skip header
        if (line.startsWith("Date")) {
            return;
        }

        // Split CSV
        String[] parts = line.split(",");

        if (parts.length < 4) {
            return;
        }

        try {

            String temp = parts[1].trim();
            String dew = parts[2].trim();
            String wind = parts[3].trim();

            // Emit:
            // WEATHER -> temp,dew,wind,1
            outValue.set(temp + "," + dew + "," + wind + ",1");

            context.write(outKey, outValue);

        } catch (Exception e) {
            // Ignore malformed rows
        }
    }
}
