from __future__ import print_function
import string
from pyspark.sql import SparkSession
from pyspark.sql import Row

#java imports
from py4j.java_gateway import java_import
from py4j.java_gateway import JavaGateway, GatewayParameters
jvm = sc._jvm
java_import(jvm,"com.splicemachine.spark.splicemachine.*")
java_import(jvm, "org.apache.spark.sql.execution.datasources.jdbc.{JDBCOptions, JdbcUtils}")

def getContext(JDBC_URL):
	return jvm.com.splicemachine.spark.splicemachine.SplicemachineContext(JDBC_URL)
def getDF(JDBC_URL, table):
	return spark.read.format('com.splicemachine.spark.splicemachine').option(url=JDBC_URL,dbtable='SYS.SYSTABLES').load()
def welcomePrint():
	return "Welcome to pysplice! Use this package to create a SpliceMachineContext with Python."
