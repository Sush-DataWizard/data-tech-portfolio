

https://prepare.sh/interviews/data-engineering



reference :

sql :
    https://medium.com/@aftab4092/top-15-sql-coding-interview-questions-5b87b26a97a8
    https://datalemur.com/sql-interview-questions
    https://codesignal.com/blog/interview-prep/28-sql-interview-questions-and-answers-from-beginner-to-senior-level/



I have one spark application
1. 50 GB data is divided in 10 partition
2. Reads 50 GB of Parquet data from Raw layer in datalake
3. Transform data - SELECT, Filter, Change Column Name, Change Column DataTYPE
3. Write data into SILVER Layer


Cluster Configuration
1 Master  (2 CPU, 4 GB Memory, 20 GB)
2 Slave  (2 CPU, 4 GB Memory, 50 GB Each)

I want your help to inderstand 
1. How many DAG's. Stages and Tasks will get created
2. How many executors and cores are allocated to this application


# Spark architecture


Apache Spark's architecture is a master-slave distributed computing model designed for efficient processing of large-scale data. Its key components work together to enable parallel processing, fault tolerance, and in-memory computation.

Driver program (spark context/spark session)
    -   Entrypoint
    -   converting user code (e.g., DataFrame transformations) into a logical plan, optimizing it, and breaking it into jobs and tasks.
    -   Communicates with the Cluster Manager to request resources and with Executors to schedule and monitor tasks.

Cluster manager
    -   Manages the resources of the cluster (YARN)
    -   Allocates resources to Spark applications and monitors the health and availability of worker nodes.
    -   Communicates with the Driver program to provide resource information and with Worker nodes to manage their resources.

Worker Nodes
    -   Slave nodes in the Spark cluster.
    -   Host one or more Executors. 
    -   Receive tasks from the Driver program and execute them.`

Executors:
    -   Processes that run on Worker Nodes.
    -   Responsible for performing the actual data processing tasks assigned by the Driver.
    -   Each Executor typically processes a portion of the data (a partition) and returns the results to the Driver.


# deploy mode client vs cluster

deploy modes is where the driver program runs. The driver is the component that controls the application and coordinates with the cluster manager to request resources.

Client Mode
    -   In Client Mode, the driver program runs on the machine where you submitted the job
    -   Best suited for debugging because it gives logs on your local terminal.

Cluster Mode
    -   In Cluster mode, the driver program runs on one of the worker node within cluster
    -   Production jobs and long-running applications


# Master, Core and Task Node 

Master :
    Think of it as the brain of the cluster.
    It decides what task runs where.
    Examples: Spark Driver, YARN ResourceManager, HDFS NameNode.

Core Node :
    They perform heavy lifting: storing HDFS blocks and running compute.

Task Nodes :
    Used when you need more compute but not additional storage.
    Good for temporary scaling of Spark, MapReduce, etc.




# How many DAGs?
    Spark creates one DAG per action (e.g., write, count, collect).
    Since your app performs one write action, there will be 1 DAG.

#  How many stages?

    Spark creates a new stage for each shuffle boundary.
    Your operations:
        SELECT, FILTER, RENAME, CAST → narrow transformations
        write → may involve a shuffle, depending on partitioning at the write stage.

    Two possibilities:
        If you don't repartition during write, Spark may not shuffle, and you get:
        ✅ 1 Stage

        If you repartition, e.g., .repartition(10) or use partitionBy() in write, it may involve a shuffle:
        🔁 2 Stages

    Stage 1: read + narrow transformations
    Stage 2: shuffle + write

# How many tasks?
    Spark creates 1 task per partition per stage.
    Your source has 10 partitions, so:

        Stage 1: 10 tasks (read & transform)
        Stage 2 (if shuffle): 10 tasks (write)

        ✅ Total: 10–20 tasks depending on shuffle

# LAZY EVALUTION

Lazy Evaluation means Spark doesn't execute transformations (like map, filter, select, join, etc.) immediately when they are called — it just builds a logical execution plan (DAG).
The actual computation happens only when an action is called (like collect(), count(), show(), write()).


| Benefit               | Explanation                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------- |
| ✅ **Optimizations**   | Spark can analyze the full DAG and optimize before execution (e.g., predicate pushdown, physical plan changes). |
| ✅ **Reduced I/O**     | If intermediate data isn't needed, Spark skips unnecessary steps.                                               |
| ✅ **Fault Tolerance** | Spark re-computes from lineage (not stored intermediate results).                                               |


# Spark Optmisation

| Layer            | Technique                               |
| ---------------- | --------------------------------------- |
| Code             | `select`, `filter`, avoid `collect()`   |
| Data             | Parquet, partitioning, bucketing        |
| Join             | Broadcast, sort-merge, skew handling    |
| Memory           | `cache()`, executor tuning, GC analysis |
| Execution Engine | AQE, Catalyst, Tungsten                 |


# SQL Optimisation 

| Area          | Key Practices                                |
| ------------- | -------------------------------------------- |
| **SELECT**    | Avoid `SELECT *`, use columns only           |
| **Filters**   | Apply early filters, use indexed columns     |
| **Joins**     | Filter first, avoid LEFT/OUTER unless needed |
| **Indexes**   | Add indexes on joins, filters                |
| **Execution** | Use `EXPLAIN`, check for full scans          |
| **Big data**  | Partitioning, clustering, materialized views |

# cache() vs persist()


cache(): This is the most common method. When you call .cache() on a DataFrame, Spark marks it to be cached. The actual caching doesn't happen until the first action (like count() or show()) is called on the DataFrame. The data is stored in memory as serialized Java objects.

persist(): The persist() method is more flexible than cache(). It allows you to specify the storage level for the cached DataFrame. For instance, you can choose to store it in memory only, on disk, or a combination of both with or without replication. This is useful for balancing performance and fault tolerance.


# SQL Question 

Find all EMP whose dept and Sal are same


    Method 1

        SELECT e1.*
        FROM EMP e1
        JOIN EMP e2
        ON e1.DEPTNO = e2.DEPTNO
        AND e1.SAL = e2.SAL
        AND e1.EMPNO <> e2.EMPNO;

    Method 2

        SELECT *
        FROM EMP
        WHERE (DEPTNO, SAL) IN (
        SELECT DEPTNO, SAL
        FROM EMP
        GROUP BY DEPTNO, SAL
        HAVING COUNT(*) > 1
        );


# Python Question

Python : count all occurrences of words in a string (has map)


    Method 1

        from collections import Counter

        aa = "Hello"
        d = Counter(aa)
        print(d)

        max_len = max(d.items(), key=lambda x: x[1])
        print(max_len)

    Method 2

        di = {}

        for w in aa:
            if w in di:
                di[w] += 1
            else:
                di[w] = 1

        print(di)

        max_le = 0
        max_le = max(di, key=di.get)
        print(max_le, di[max_le])


# Narrow and wide transformations

Narrow :
    - output partition depends on only one input partition
    - no shuffling
    - map(), filter(), select(), flatMap(), union(), withColumn()

Wide :
    - output partitions depend on multiple input partitions
    - bacause of above shuffling takes place
    - groupBy(), groupByKey(), join(), distinct(), orderBy(), sort(), repartition()


# Spark JOb


| Term       | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| **Action** | Triggers execution (e.g., `count()`, `collect()`, `write`)       |
| **Job**    | Created per action                                               |
| **Stage**  | A group of tasks with narrow dependencies                        |
| **Task**   | Work on **1 partition** of data — the smallest unit of execution |


Job 1 :

    df = spark.read.parquet("s3://data/raw")                 # 10 partitions
    df_filtered = df.filter("status = 'active'")
    df_selected = df_filtered.select("id", "status")
    df_selected.write.parquet("s3://data/filter_processed")  # ✅ Action (Job 1)


| Stage       | Description                     | Trigger                     |
| ----------- | ------------------------------- | --------------------------- |
| **Stage 1** | Read + Filter + Select (narrow) | Input scan & transformation |
| **Stage 2** | Output Write                    | Writing to disk (Parquet)   |

    10 tasks each stage

Job 2:

    df = spark.read.parquet("s3://data/raw")

    # First wide transformation
    df1 = df.groupBy("dept").agg({"salary": "sum"})

    # Second wide transformation
    df2 = df1.join(other_df, "dept")

    df2.write.parquet("s3://data/output")


| Stage | Description                      | # Tasks                                   |
| ----- | -------------------------------- | ----------------------------------------- |
| 0     | Read + prepare keys (narrow)     | 1 task per input partition                |
| 1     | Shuffle for groupBy              | 1 task per `spark.sql.shuffle.partitions` |
| 2     | Shuffle for join and final write | Again, 1 task per `shuffle.partitions`    |


# General Rule:

Each wide transformation = new shuffle = new stage.

So if you chain:

    2 narrow → still 1 stage

    1 wide → 2 stages
    2 wide → 3 stages
    3 wide → 4 stages (and so on…)


# What Happens Internally During a Shuffle?

- Map Stage: Each executor writes shuffle files (e.g., 200 small files) to local disk, one per reduce task.
- Shuffle Read (Reduce Stage): Executors fetch those files from all other nodes over the network.
- Data gets grouped, sorted, aggregated, or joined.
- The output is repartitioned into the number of shuffle partitions.

 Example: With 10 input partitions and default 200 shuffle partitions:

- Each executor writes 200 files → total of 2000 shuffle blocks
- On the next stage, 200 tasks will read those 2000 files, causing heavy disk + network IO


# SCD

| Type | Name                | What It Does                                            |
| ---- | ------------------- | ------------------------------------------------------- |
| 0    | Fixed Dimensions    | **No change allowed** — attribute is static             |
| 1    | Overwrite           | **Overwrite** old data with new data                    |
| 2    | Historical Tracking | **Insert new row** for every change (with versioning)   |
| 3    | Limited History     | Add **new column** to store previous value              |
| 4    | History Table       | Keep history in a **separate historical table**         |
| 6    | Hybrid (1 + 2 + 3)  | Combine overwriting, current and previous data tracking |


# fact table : Stores measurable business metrics or events

e.g : Sales_Fact

| Sale_ID  | Product_ID  | Customer_ID  |   Date   | Amount | Quantity |
| -------- | ----------- | ------------ | -------- | ------ | -------- |


# Dimension table : Stores descriptive attributes related to fact data

e.g : Customer_dim

| Customer_ID  | Name | City | Segment |
| ------------ | ---- | ---- | ------- |

e.g : Date_dim

| Date_ID  | Full_Date  | Month | Year |
| -------- | ---------- | ----- | ---- |


# STAR Schema : Fact table in the center, directly connected to denormalized dimension tables.

         Customer_Dim
              |
Product_Dim — Sales_Fact — Date_Dim
              |
         Store_Dim


Fast query performance (fewer joins)
Simple to understand and navigate
Best for OLAP 

# SNOWFLAKE schema : A normalized version of star schema — dimensions are split into sub-dimensions.

         Region_Dim
              |
         Country_Dim
              |
Product_Dim — Sales_Fact — Date_Dim
              |
         Customer_Dim — Segment_Dim


# STAR vs SNOWFLAKE

| Feature            | Star Schema        | Snowflake Schema  |
| ------------------ | ------------------ | ----------------- |
| Normalization      | Denormalized       | Normalized        |
| Query Speed        | Faster             | Slower            |
| Storage Efficiency | More space         | Less space        |
| Design Complexity  | Simpler            | More complex      |
| Best For           | OLAP, BI Reporting | OLTP, Backend DWH |


# Normalisation vs denormalisation

Normalization :
    process of organizing data into multiple related tables to reduce data redundancy and improve data integrity.
    Data is split into multiple normalized tables
    Uses foreign keys to relate tables
    Less duplication, but more joins

    e.g :
        | Orders                        | Customers                |
        | ----------------------------- | ------------------------ |
        |  order_id,  customer_id, date |  customer_id, name, city |

DeNormalisation :
    process of combining tables to reduce the number of joins and improve read/query performance.
    Data is duplicated across tables
    Fewer joins → faster for reads
    More suitable for reporting, analytics

    e.g :
        | order_id | customer_name | city | date |



| Aspect                 | **Normalization**                 | **Denormalization**               |
| ---------------------- | --------------------------------- | --------------------------------- |
| Purpose                | Efficient writes, integrity       | Efficient reads, reporting        |
| Use Case               | OLTP (Transactional systems)      | OLAP (Analytics systems)          |
| Query Performance      | ⚠️ Slower (more joins)            | ✅ Faster (fewer joins)            |
| Storage Usage          | ✅ Efficient                       | ❌ Larger (due to duplication)    |
| Maintainability        | ✅ Easier to update a single point | ❌ More risk of inconsistency     |
| Integrity Constraints  | ✅ Enforced with keys              | ⚠️ Harder to maintain manually    |



# LOGICAL JOINS 

| Logical Join Type    | What It Does                                                                   | Example                                                       |
| -------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **INNER JOIN**       | Returns rows where **keys match** in both tables                               | `orders JOIN customers ON orders.cust_id = customers.cust_id` |
| **LEFT OUTER JOIN**  | Returns **all rows from left**, matched rows from right, NULL if no match      | Customers without orders                                      |
| **RIGHT OUTER JOIN** | Returns **all rows from right**, matched from left, NULL if no match           | Products never ordered                                        |
| **FULL OUTER JOIN**  | Returns all rows from both sides, NULL where no match                          | Combine customer + order list (include missing on both sides) |
| **LEFT SEMI JOIN**   | Returns rows from **left table only if match exists in right** (no right cols) | Find customers **who placed** orders                          |
| **LEFT ANTI JOIN**   | Returns rows from **left with no match** in right                              | Customers **who never placed** orders                         |
| **CROSS JOIN**       | Cartesian product (every row with every row)                                   | Not recommended unless necessary                              |
| **NON-EQUI JOIN**    | Joins on `<`, `>`, `!=`, etc. instead of `=`                                   | Salary band, range-based joins                                |


# PHYSICAL JOINS

| Physical Join Type          | What It Does                                                      | When Used                           | Example                                         |
| --------------------------- | ----------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------- |
| **BroadcastHashJoin**       | Broadcasts small table to all executors and **builds hash table** | One table is **small (<10MB)**      | Join customer_dim (small) to large sales_fact |
| **SortMergeJoin**           | **Sorts and shuffles both tables** on join key, then merges       | Both tables are large & sorted      | Join `orders` with `payments` on `order_id`     |
| **ShuffledHashJoin**        | Hashes one partitioned side in memory, streams the other          | Join key present, one side smallish | Occasionally chosen by Spark if better          |
| **BroadcastNestedLoopJoin** | Tries all combinations (cross join or non-equi)                   | Non-equi joins, **no usable key**   | `salary > min_band AND salary < max_band`       |
| **Cartesian Product**       | Pure cross join — every row with every row                        | If no join condition is given       | `df1.crossJoin(df2)`                            |


# ACID

| Property            | Meaning                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| **A** – Atomicity   | All operations in a transaction **succeed or none do**                     |
| **C** – Consistency | The database remains in a **valid state** before and after the transaction |
| **I** – Isolation   | **Concurrent transactions don’t interfere** with each other                |
| **D** – Durability  | Once committed, data is **permanently saved**, even in case of failure     |

ACID ensures that transactions are reliable and fault-tolerant. 
In traditional RDBMS like Postgres, ACID is enforced through transaction logs and locks. 
In data lakes like Delta Lake or Apache Hudi, ACID is achieved using metadata logs.
This guarantees that even in the presence of concurrent jobs or failures, our data remains consistent and trustworthy.

| System                      | OLTP / OLAP | ACID Compliance                                     | Notes                                                                       |
| --------------------------- | ----------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| **MySQL (InnoDB)**          | ✅ OLTP      | ✅ Full ACID                                         | Fully compliant when using InnoDB engine; ideal for transactional workloads |
| **PostgreSQL**              | ✅ OLTP      | ✅ Full ACID                                         | Strong OLTP performance with MVCC and rich SQL support                      |
| **MS SQL Server**           | ✅ OLTP      | ✅ Full ACID                                         | Full support with advanced transaction isolation & durability               |
| **Hive (with ACID tables)** | ⚠️ OLAP     | ⚠️ Partial (ACID for ORC transactional tables only) | ACID supported only with transactional tables + ORC format + Tez/LLAP       |
| **BigQuery**                | ✅ OLAP      | ❌ Not fully ACID                                    | No full multi-table transactions, eventual consistency on writes            |
| **Amazon Redshift**         | ✅ OLAP      | ⚠️ Partial ACID                                     | Basic ACID properties, lacks full isolation and transactional guarantees    |


# DELTA LAKE

Delta Lake is an open-source storage layer built on top of Apache Parquet.
Brings ACID transactions, schema enforcement, versioning & streaming support to data lakes like Amazon S3, Azure Data Lake, and HDFS.



Features: 
- ACID transactions                  
- Schema enforcement & evolution     
- Compaction (OPTIMIZE) : Merges small files for faster queries.
- Z-ordering : Optimizes data layout for faster filtering.
- Time travel (query older versions) 
- Unified streaming + batch      
- Upserts/Merges	    

# DELTA LAKE OPTIMISATION 

1. Z-Ordering (Data Skipping) : 
    Z-Ordering improves query performance by clustering data on one or more columns used in filters.
2. OPTIMIZE Command (Compaction) : 
    Delta tables generate many small files from streaming or frequent writes. Use OPTIMIZE to compact them.
3. VACUUM (Storage Cleanup) :
    Delta retains old files for time travel and versioning. Use VACUUM to delete unused files.
4. Partitioning
5. Caching Frequently Queried Data :
    Use Spark’s CACHE TABLE to keep hot data in memory.

# Z-ORDER BY

Z-Ordering is a multi-dimensional clustering technique that optimizes how data is physically stored on disk in Delta Lake tables, especially to speed up filter queries.
It works by co-locating related records on the same data blocks using Z-order curves, which improves data skipping.
Delta Lake collects column stats (min, max, nulls) per Parquet file.
Z-Ordering reorganizes the rows across files so that similar values (e.g., same customer_id, or region) are physically stored close together.
This increases the chance that irrelevant files will be skipped during query execution.


# AUTOLOADER

Allows to incrementally and efficiently ingest data from cloud object stores like AWS S3, Azure Data Lake, or GCS into Delta Lake.
A smart file watcher + scalable ingestion engine, That detects new files, loads only new data, and avoids reprocessing old files.

It’s schema-aware, checkpointed, and optimized for millions of files. 
Use it for real-time pipelines, especially in medallion architecture for loading raw → bronze → silver layers


# Unity Catalog

Unity Catalog is a unified metadata layer and governance solution in Databricks that provides:

    Centralized data cataloging
    Fine-grained access control
    Data lineage
    Auditability across workspaces

It brings enterprise-grade data governance to your Delta Lake, tables, files, and ML models in Databricks.

# DELTA Sharing


Delta Sharing is an open-source protocol that allows you to share live data (especially Delta Lake tables) across clouds, platforms, or organizations — without copying the data.

Think of it like this:

🔑 “Give access to data, not copies of it.”



# repartition vs coalesce

| Aspect               | `repartition(n)`                          | `coalesce(n)`                             |
| -------------------- | ----------------------------------------- | ----------------------------------------- |
| **Shuffle**          | ✅ Yes (full shuffle of data)              | ❌ No (avoids shuffle, merges partitions)  |
| **Use Case**         | Increase partitions (e.g., from 10 → 100) | Decrease partitions (e.g., from 100 → 10) |
| **Performance Cost** | ❗ Higher (due to network & disk I/O)      | ✅ Faster (minimizes I/O)                  |
| **Skew Handling**    | ✅ Better (even distribution)              | ❌ May result in skew                      |
| **Parallelism**      | ✅ Increases parallelism                   | ❌ May reduce parallelism                  |
| **When Used**        | Before wide transformations or joins      | Before write (e.g., reduce files)         |


# medallion architecture


| Layer         | Purpose                               | Data Quality | Data Type       | Used By       |
| ------------- | ------------------------------------- | ------------ | --------------- | ------------- |
| 🥉 **Bronze** | Raw ingested data from source systems | Low          | JSON, CSV, logs | Engineers     |
| 🥈 **Silver** | Cleaned, filtered, structured data    | Medium       | Parquet, ORC    | Analysts, ML  |
| 🥇 **Gold**   | Aggregated, business-level KPIs       | High         | Star schema     | BI, Reporting |





# CAP Theorem

| System                                      | Type                                       | Why                                           |
| ------------------------------------------- | ------------------------------------------ | --------------------------------------------- |
| **CP – Consistency + Partition Tolerance**  | HBase, MongoDB (in strict mode), Zookeeper | Prioritize data correctness over availability |
| **AP – Availability + Partition Tolerance** | Cassandra, Couchbase, DynamoDB             | Prioritize always responding, even if stale   |
| **CA – Consistency + Availability**         | Traditional RDBMS (only if no partition)   | Only possible in non-distributed setups       |




# Indexing in SQL

An index is a data structure (usually a B-tree or hash) that allows faster retrieval of rows from a table, similar to an index in a book.
Without an index, SQL performs a full table scan to find rows.

| Benefit                          | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| ✅ **Faster queries**             | Especially `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY` |
| ✅ **Improves lookup**            | Quick access to rows using primary or foreign keys |
| ✅ **Better performance in OLTP** | Faster reads for highly transactional systems      |

Partitioning helps the engine skip whole chunks of data

Indexing helps quickly locate rows within those chunks




# DATA SKEW

Data skew occurs when certain keys appear far more frequently than others, causing:

Uneven partition sizes, Some tasks to run much longer, Shuffle bottlenecks, Resource wastage

e.g :
        SELECT region, COUNT(*) 
        FROM sales 
        GROUP BY region
    
    If 90% of rows belong to "Delhi", then one reducer will be overloaded.


#  Adaptive Query Execution (AQE) in Spark

dynamically adjust query plans at runtime 
Improve performance based on actual data characteristics, not just estimates.
Automatically detects and mitigates skew.

AQE:

    Switches between shuffle join and broadcast join based on the actual size of data at runtime.
    Skew-aware shuffle
    Replans stages based on runtime stats


# Hive Execution Engine

Apache Tez is a DAG-based execution engine that lets Hive and Pig run multiple stages in a single job, reducing overhead, I/O, and latency.
It's designed to replace MapReduce for Hive.



MapReduce follows a rigid two-stage model that writes intermediate data to disk, making it slow. 
Tez uses a DAG model with in-memory processing, which speeds up execution and reduces job overhead. 


# USER INDEXES

User indexes are indexes that are explicitly created by users (developers or DBAs) on one or more columns of a table to improve query performance.

They are different from system-generated indexes like primary key or unique constraints, which may be created automatically.


# Default core and executor size

I am reading and writing 10 GB file 

Default - 
    - 1 executor Per Application
    - 1 Core per executor
    - 1 GB executor memory
       Note : This means Spark will struggle with a 10 GB file unless configured properly.

Best Config for 10 Gb :

    - 3 executor
    - 2 core per executor
        3*2 = 6 core in total  -->> 6 task/partition will run parallely
    - 4 GB executor memory
        
        Note : Spark will divide 10 GB into 128 MB block/partition partition


# How to tune spark executor number, cores and executor memory?

ref : https://stackoverflow.com/questions/37871194/how-to-tune-spark-executor-number-cores-and-executor-memory



6 Node cluster | 16 Core | 64 GB memory 


1 Core + 1 GB memory  -> For OS / Hadoop



Cores :
    Number of cores = Concurrent tasks as executor can run 


    So we might think, more concurrent tasks for each executor will give better performance. But research shows that
    any application with more than 5 concurrent tasks, would lead to bad show. So stick this to 5.


Number of Executor :

    1 Node Calculation :
        15 Core + 63 Memory 

        15 / 5 = 3 execuetors with 5 core each [ i.e 5 conccurrent task ]

    So with 6 node  :
        18 execuetors with 5 core each

    Lets give 1 executor for YARN / Java process 

    17 is the number we give to spark using --num-executors while running from spark-submit shell command


Memory for each executor:


    From above step, we have 3 executors  per node. And available RAM is 63 GB

    So memory for each executor is 63/3 = 21GB. 

    However small overhead memory is also needed to determine the full memory request to YARN for each executor.
    Formula for that over head is max(384, .07 * spark.executor.memory)

    Calculating that overhead - .07 * 21 (Here 21 is calculated as above 63/3)
                                = 1.47

    Since 1.47 GB > 384 MB, the over head is 1.47.
    Take the above from each 21 above => 21 - 1.47 ~ 19 GB


    So executor memory - 19 GB
    Final numbers - Executors - 17, Cores 5, Executor Memory - 19 GB


# Pandas DF vs Spark DF

| Feature           | **Pandas DataFrame**                | **Spark DataFrame**                           |
| ----------------- | ----------------------------------- | --------------------------------------------- |
| Processing Engine | Python (single-threaded, in-memory) | Spark engine (distributed, JVM-based)         |
| Language          | Pure Python                         | PySpark (Python API over JVM/Scala)           |
| Execution Type    | Eager (executes immediately)        | Lazy (executes only on action like `.show()`) |
| Parallelism       | None (single core by default)       | Distributed across multiple nodes/cores       |


# which python libraries I have used ?

Pandas
postgres and mysql connection libraries
GCP and AWS libraries
kafka-python

# List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

e.g:

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    
    newlist = [x for x in fruits if "a" in x]

    print(newlist)


