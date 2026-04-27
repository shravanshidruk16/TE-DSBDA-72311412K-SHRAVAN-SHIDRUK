//LogMapper
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class LogMapper
    extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable ONE = new IntWritable(1);
    private final Text outKey = new Text();

    // Log pattern: 7 space-separated tokens (Apache Combined Log Format)
    // [0]=IP [1]=ident [2]=user [3]=time [4]=request [5]=status [6]=bytes

    @Override
    protected void map(LongWritable key, Text value, Context ctx)
            throws IOException, InterruptedException {

        String line = value.toString().trim();
        if (line.isEmpty() || line.startsWith("#")) return;

        //Parse fields
        String[] parts = line.split(" ");
        if (parts.length < 7) return;  // malformed line

        String ip         = parts[0];              // client IP
        String statusCode = parts[5];              // HTTP status
        String requestUrl = extractUrl(parts[4]); // URL from "GET /path HTTP/1.1"

        //Emit 1: status code count
        outKey.set("STATUS_" + statusCode);
        ctx.write(outKey, ONE);

        //Emit 2: URL access count
        if (requestUrl != null) {
            outKey.set("URL_" + requestUrl);
            ctx.write(outKey, ONE);
        }

        //Emit 3: IP access count
        outKey.set("IP_" + ip);
        ctx.write(outKey, ONE);
    }

    /** Extract URL path from request field like: "GET /home HTTP/1.1" */
    private String extractUrl(String requestField) {
        // Remove surrounding quotes if present
        String req = requestField.replace("\"", "");
        String[] tokens = req.split(" ");
        return (tokens.length >= 2) ? tokens[1] : null;
    }
}