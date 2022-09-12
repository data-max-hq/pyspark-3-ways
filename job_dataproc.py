from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = (
    SparkSession.builder.appName("local").getOrCreate()
)

members_df = spark.read.csv("gs://<bucket-name>/data/members_v3.csv", header=True, inferSchema=True)

transactions_df = spark.read.csv(
    "gs://<bucket-name>/data/transactions/churn_comp_refresh/transactions_v2.csv",
    header=True,
    inferSchema=True,
)

user_logs_df = spark.read.csv(
    "gs://<bucket-name>/data/user_logs/churn_comp_refresh/user_logs_v2.csv", header=True, inferSchema=True
)

train_df = spark.read.csv(
    "gs://<bucket-name>/data/train/churn_comp_refresh/train_v2.csv", header=True, inferSchema=True
)

logs_agg = user_logs_df.groupBy("msno").agg(
    {
        "num_25": "sum",
        "num_50": "sum",
        "num_75": "sum",
        "num_985": "sum",
        "num_100": "sum",
        "num_unq": "sum",
        "total_secs": "sum",
    }
)
logs_agg = logs_agg.withColumn(
    "sum(num_total)",
    sum(
        [
            logs_agg["sum(num_25)"],
            logs_agg["sum(num_50)"],
            logs_agg["sum(num_75)"],
            logs_agg["sum(num_985)"],
            logs_agg["sum(num_100)"],
        ]
    ),
)

data = train_df.join(logs_agg, "msno")

cols = [col for col in data.drop("msno").drop("is_churn").columns]

assembler = VectorAssembler(inputCols=cols, outputCol="features")
output = assembler.transform(data)

output = output.withColumn("label", output["is_churn"])

# Train the model
trainingData, testingData = output.randomSplit([0.8, 0.2])
lr = LogisticRegression(maxIter=10, regParam=0.02, elasticNetParam=0.8)
lrModel = lr.fit(trainingData)
lrModel.save("gs://<bucket-name>/model")

prediction_df = lrModel.transform(testingData)

ev = MulticlassClassificationEvaluator()
print("accuracy ", ev.evaluate(prediction_df))

spark.stop()
