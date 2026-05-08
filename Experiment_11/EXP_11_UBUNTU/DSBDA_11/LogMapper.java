import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class LogMapper
        extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable ONE = new IntWritable(1);
    private final Text outKey = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context ctx)
            throws IOException, InterruptedException {

        String line = value.toString().trim();

        // Ignore empty lines
        if (line.isEmpty()) {
            return;
        }

        // Split line properly
        String[] parts = line.split("\\s+");

        // Validate log line
        if (parts.length < 10) {
            return;
        }

        // Extract fields
        String ip = parts[0];
        String requestUrl = parts[6];
        String statusCode = parts[8];

        // Emit status code count
        outKey.set("STATUS_" + statusCode);
        ctx.write(outKey, ONE);

        // Emit URL access count
        outKey.set("URL_" + requestUrl);
        ctx.write(outKey, ONE);

        // Emit IP access count
        outKey.set("IP_" + ip);
        ctx.write(outKey, ONE);
    }
}
