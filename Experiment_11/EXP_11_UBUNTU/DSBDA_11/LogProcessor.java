// ─── LogProcessor.java 

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LogProcessor {

    public static void main(String[] args) throws Exception {

        //Configuration 
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Log File Processing");

        //Set classes 
        job.setJarByClass(LogProcessor.class);
        job.setMapperClass(LogMapper.class);
        job.setCombinerClass(LogReducer.class);  // local pre-reduce
        job.setReducerClass(LogReducer.class);

        //Output key/value types 
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        //I/O paths (from args) 
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        //Run 
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}