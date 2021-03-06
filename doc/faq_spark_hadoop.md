## SPARK / HADOOP ECOSYSTEM  FAQ 

0. - Spark Tutorial 
	-https://data-flair.training/blogs/spark-tutorial/

   - Hadoop VS hive VS hbase VS pig VS RDBMS (in EMR system)
   	-https://aws.amazon.com/tw/emr/faqs/

1. Difference between Spark VS Hadoop?

- ***Hadoop*** is a big data infrastructure that make large scale dataset storage possible via split the dataset (`HDFS`) into `data block` and save in each node (data node)
	- Data node : the components save split data block
	- Name node : the components manage data storage places

- ***Spark*** is a big data framework that access large scale dataset like above, and doing processing like : ETL, stream, machine learning and so on...

- In short, Hadoop and Spark are different. `Hadoop :  data storage`,
`spark : data process`

2. Things happen after `spark-submit`?

3. What's RDD, HDFS ?

- Resilient Distributed Datasets (RDD) is a simple and immutable distributed collection of objects. Each RDD is split into multiple partitions which may be computed on different nodes of the cluster. In Spark, every function is performed on RDDs only.

- Spark revolves around the concept of a resilient distributed dataset (RDD), which is a fault-tolerant collection of elements that can be operated on in parallel.

- Hadoop HDFS VS RDD 

	- In Hadoop, we store the data as blocks and store them in different data nodes. In Spark, instead of following the above approach, we make partitions of the RDDs and store in worker nodes (datanodes) which are computed in parallel across all the nodes.

	- In Hadoop, we need to replicate the data for fault recovery, but in case of Spark, replication is not required as this is performed by RDDs.

	- RDDs load the data for us and are resilient which means they can be recomputed.

	- RDDs perform two types of operations: Transformations which creates a new dataset from the previous RDD and actions which return a value to the driver program after performing the computation on the dataset.

	- RDDs keeps a track of transformations and checks them periodically. If a node fails, it can rebuild the lost RDD partition on the other nodes, in parallel.


3'. Explain data partition in Spark?

- Partitioning is nothing but dividing it into parts. If you talk about partitioning in distributed system, we can define it as the division of the large dataset and store them as multiple parts across the cluster.

- Spark works on data locality principle. Worker nodes takes the data for processing that are nearer to them. By doing partitioning network I/O will be reduced so that data can be processed a lot faster.

- In Spark, operations like co-group, groupBy, groupByKey and many more will need lots of I/O operations. In this scenario, if we apply partitioning, then we can reduce the number of I/O operations rapidly so that we can speed up the data processing.

- To divide the data into partitions first we need to store it. Spark stores its data in form of RDDs.

- https://acadgild.com/blog/partitioning-in-spark

4. Explain spark  `master node`,`worker node` ,`executor`, `receiver`,`driver`...?

	<img src ="https://github.com/yennanliu/CS_basics/blob/master/doc/pic/spark_driver_workder_executor.png" width="500" height="300">

	- Driver 
		- The program that runs on the master node of the machine and declares transformations and actions on data RDDs. In simple terms, a driver in Spark creates `SparkContext`, connected to a given Spark Master. The driver also delivers the RDD graphs to Master, where the standalone cluster manager runs.

	- Master
		- Master node is responsible for task scheduling and resource dispensation.

	- Worker  
		- `Worker node refers to any node that can run the application code in a cluster`. The driver program must listen for and accept incoming connections from its executors and must be network addressable from the worker nodes. 

		- Worker node is basically the `slave node`. Master node assigns work and worker node actually performs the assigned tasks. `Worker nodes process the data stored on the node and report the resources to the master`. Based on the resource availability, the master schedule tasks.

	- Executor 
		- When SparkContext connects to a cluster manager, it acquires an Executor on nodes in the cluster. Executors are Spark processes that run computations and store the data on the worker node. The final tasks by SparkContext are transferred to executors for their execution.

5. Explain how to deal with `Spark data skew` problems ? ***

6. How do if one of the spark node failed because of overloading ?

7. Why Spark is faster than MapReduce in general ?

8. Explain Spark running mode : `stand alone`, `Mesos`, `YARN` ?

	- Spark stand anlone 
		- When running on standalone cluster deployment, the cluster manager is a Spark master instance.

	- Spark Mesos
		- When using Mesos, the Mesos master replaces the Spark master as the cluster manager. Mesos determines what machines handle what tasks. Because it takes into account other frameworks when scheduling these many short-lived tasks, multiple frameworks can coexist on the same cluster without resorting to a static partitioning of resources.

	- Spark YARN 

9. Explain spark operator ?

10. Explain `cache` VS `persist` ?

11. Which one is better in RDD ? `reducebykey` VS `groupby` ? why?

12. What errors may happen when `spark streaming` ? how to fix them ? 

13. How to prevent spark `out of memeory` `(OOM)` problem ?

14. How does saprk split `stage` ?

15. What're spark work, stage, task; and there relationship ?

16. How to set up spark master HA ?

17. How does `spark-submit` import external `jars`  

18. Explain spark Polyglot, Lazy Evaluation ?

19. Is there any benefit of learning MapReduce if Spark is better than MapReduce?

	- Yes, MapReduce is a paradigm used by many big data tools including Spark as well. It is extremely relevant to use MapReduce when the data grows bigger and bigger. Most tools like Pig and Hive convert their queries into MapReduce phases to optimize them better.

20. What is Executor Memory in a Spark application?

21. What operations does RDD support?

	- RDDs support two types of operations: transformations and actions. 

		- Transformations: Transformations create new RDD from existing RDD like map, reduceByKey and filter we just saw. Transformations are executed on demand. That means they are computed lazily.
		e.g. :`map`, `flatmap`, `reducebykey`, `filter`, `union`, `sample`

		- Actions: Actions return final results of RDD computations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.

22. Flatmap VS map ? Reduce VS ReduceByKey ? 

23. Illustrate some cons of using Spark.

24. What is a Sparse Vector?

25. How can you minimize data transfers when working with Spark?

	- Minimizing data transfers and avoiding shuffling helps write spark programs that run in a fast and reliable manner. The various ways in which data transfers can be minimized when working with Apache Spark are:

		- Using Broadcast Variable- Broadcast variable enhances the efficiency of joins between small and large RDDs.

		- Using Accumulators – Accumulators help update the values of variables in parallel while executing.

	The most common way is to avoid operations ByKey, repartition or any other operations which trigger shuffles.

26. What are broadcast variables and accumulators?

27. How can you trigger automatic clean-ups in Spark to handle accumulated metadata?

	- You can trigger the clean-ups by setting the parameter `spark.cleaner.ttl` or by dividing the long running jobs into different batches and writing the intermediary results to the disk.

28. Explain Caching in Spark Streaming ? 

	- DStreams allow developers to cache/ persist the stream’s data in memory. This is useful if the data in the DStream will be computed multiple times. This can be done using the persist() method on a DStream. For input streams that receive data over the network (such as Kafka, Flume, Sockets, etc.), the default persistence level is set to replicate the data to two nodes for fault-tolerance.

29. What are the various levels of persistence in Apache Spark?

	- MEMORY_ONLY: Store RDD as deserialized Java objects in the JVM. If the RDD does not fit in memory, some partitions will not be cached and will be recomputed on the fly each time they’re needed. This is the default level.

	- MEMORY_AND_DISK: Store RDD as deserialized Java objects in the JVM. If the RDD does not fit in memory, store the partitions that don’t fit on disk, and read them from there when they’re needed.
	
	- MEMORY_ONLY_SER: Store RDD as serialized Java objects (one byte array per partition).

	- MEMORY_AND_DISK_SER: Similar to MEMORY_ONLY_SER, but spill partitions that don’t fit in memory to disk instead of recomputing them on the fly each time they’re needed.

	- DISK_ONLY: Store the RDD partitions only on disk. OFF_HEAP: Similar to MEMORY_ONLY_SER, but store the data in off-heap memory.

30. Explain `mapPartitions`, what's the difference between mapPartitions and map ?

31. Explain `broadcast join`, what's the difference between `broadcast join`and join ?

32. How to optimize spark with `partitioner` ?

33. Explain `combineByKey` VS. `groupByKey` ?

i.e. 
```scala
// reduceByKey
rdd.reduceByKey(_.sum)

// groupByKey
rdd.groupByKey().mapValue(_.sum)

```

## Ref 
- https://www.edureka.co/blog/interview-questions/top-apache-spark-interview-questions-2016/
- https://data-flair.training/blogs/spark-rdd-operations-transformations-actions/
- https://zhuanlan.zhihu.com/p/47499258


