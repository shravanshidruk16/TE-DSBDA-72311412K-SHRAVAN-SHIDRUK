// ─── LogReducer.java ─
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class LogReducer
    extends Reducer<Text, IntWritable, Text, IntWritable> {

    private IntWritable result = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values,
                           Context ctx)
            throws IOException, InterruptedException {

        // ── Sum all values for this key
        int total = 0;
        for (IntWritable val : values) {
            total += val.get();
        }

        // ── Emit final aggregated result 
        result.set(total);
        ctx.write(key, result);
    }