import org.apache.spark.{SparkConf,SparkContext}

object SparkWordCount1{
  def main(args: Array[String]): Unit ={
    System.setProperty("hadoop.home.dir","D:\\UMKC Projects\\hadoop-2.7.7-src")
    val sparkConf = new SparkConf().setAppName("SparkWordCount1").setMaster("local")

    val sc=new SparkContext(sparkConf)

    val input=sc.textFile("input")

    val wc=input.flatMap(line=>{line.split(" ")}).map(word=>(word.charAt(0),word)).cache()
    val output=wc.reduceByKey(_+","+_)
    output.saveAsTextFile("output")
  }
}