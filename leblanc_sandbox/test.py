#!/usr/bin/env python

from pyspark import SparkConf, SparkContext

import os
import collections


dropoutRateCsvPath = @"../data/High_School_Dropout_Statistics_by_County_2012-2013_School_Year_5-Year_Cohort_Dropout_Rates.csv"
enrollmentCsvPath = @"../data/K-12_Public_School_Enrollment_by_Grade_Level_October_Enrollment_Report_2009-2013.csv"
schoolDistPopCsvPath = @"../data/WAOFM_-_SAEP_-_School_District_Population_Estimates__2000-2016.csv"

print "path is valid: {0}".format(os.path.exists(dropoutRateCsvPath))

print "done"
