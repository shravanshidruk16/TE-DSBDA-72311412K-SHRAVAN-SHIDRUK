import org.apache.spark.{SparkConf, SparkContext}

object WordCount {
  def main(args: Array[String]): Unit = {

    //Initialize SparkConf and SparkContext
    val conf = new SparkConf()
      .setAppName("WordCount")
      .setMaster("local[*]")         // Run locally using all available cores

    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")          // Suppress INFO/WARN logs

    //oad the text file into an RDD
    val textFile = sc.textFile("sample_input.txt")

    //Split lines into words (flatMap - Transformation 1)
    val words = textFile.flatMap(line => line.split("\\s+"))

    // Map each word to (word, 1) (map - Transformation 2)
    val wordPairs = words.map(word => (word.toLowerCase, 1))

    //Reduce by key - sum up counts (reduceByKey - Action)
    val wordCount = wordPairs.reduceByKey(_ + _)

    //Sort by count descending for better readability
    val sortedWordCount = wordCount.sortBy(_._2, ascending = false)

    //Display the results
    println("\n===== Word Count Results =====")
    sortedWordCount.collect().foreach {
      case (word, count) => println(s"$word : $count")
    }
    println(" ")

    //top SparkContext
    sc.stop()
  }
}