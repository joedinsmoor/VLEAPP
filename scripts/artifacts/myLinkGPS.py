import csv
import os
import sqlite3
import re

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, logdevinfo, is_platform_windows, open_sqlite_db_readonly

#Compatability Data
vehicles = ['Chevrolet 2017+']
platforms = ['MyLink, Intellilink']

def myLink_gps():
    pass
__artifacts__ = {
    "MyLink GPS Data": (
        "MyLink GPS Data",
        ('*/bluetooth/DB_BMS/CH_*.db*'),
        myLink_gps),
}