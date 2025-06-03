df = (spark.read
        .format("csv")
        .option("Header","True")
        .option("inferSchema","True")
        .load("/FileStore/sampleData/sample.csv")
)
display(df)
