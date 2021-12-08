# Inter-Query-Parallelism

In Inter-query parallelism, there is an execution of multiple transactions by each CPU. It is called parallel transaction processing. DBMS uses transaction dispatching to carry inter query parallelism. We can also use some different methods, like efficient lock management. In this method, each query is run sequentially, which leads to slowing down the running of long queries. In such cases, DBMS must understand the locks held by different transactions running on different processes. Inter query parallelism on shared disk architecture performs best when transactions that execute in parallel do not accept the same data. Also, it is the easiest form of parallelism in DBMS, and there is an increased transaction throughput.

