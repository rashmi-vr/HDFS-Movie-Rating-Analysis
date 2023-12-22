Movie reviews can be a significant source of textual data, which is exponentially growing and are often written in natural language, making them difficult to interpret and relevant for various applications, such as market & sentiment analysis and recommender systems. As a result, a storage system like HDFS, along with the MapReduce program on the Hadoop framework, is an excellent alternative because of its distributed structure, as it allows for the parallel processing of enormous datasets and is adaptable enough to be customised for various analyses compared to the regular file system. In addition, given the amount of data and the repetitive procedure of computational tasks involved in filtering out the best movies, MapReduce, a batch-processing framework, might be the preferred choice. </br> 
The following is a brief description of the gathered dataset before moving on to the data processing stage, </br> 
• The dataset comprises the Reviewer ID, Movie Title, Genre, Year of Release, and Rating.
• Around 100,000 reviews have been included in the analysis.
• A scale of 1 to 5 is used as a rating.
• The gathered dataset includes movies released between 1902 and 2018. </br>
The analysis has been carried out using the MapReduce design, which divides the data into smaller portions and performs parallel processing. The partial aggregation of the mapper output has been carried out using a combiner in addition to the mapper and reducer, making it more effective and minimising computational costs. The following is an explanation of the data processing pipeline, </br> 
STEP 1: Mapper </br> 
STEP 2: Combiner </br> 
STEP 3: Reducer
