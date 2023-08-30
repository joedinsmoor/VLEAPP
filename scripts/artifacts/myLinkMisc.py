import csv
import os
import sqlite3
import re

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, logdevinfo, is_platform_windows, open_sqlite_db_readonly

#Compatability Data
vehicles = ['Chevrolet 2017+']
platforms = ['MyLink, Intellilink']
def myLink_misc(files_found, report_folder, seeker, wrap_text):
    data_list = []
    for file_found in files_found:
        with open(file_found, "r") as f:
            filename = f.splits()
            pass
    data_list.append(filename)
    if len(data_list) > 0:
        report = ArtifactHtmlReport('Music Resume Data')
        report.start_artifact_report(report_folder, f'Music Resume Data')
        report.add_script()
        data_headers = ('Filename')
        file_found = os.path.dirname(file_found)
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
        
        tsvname = f'Music Resume Data'
        tsv(report_folder, data_headers, data_list, tsvname)
        
    else:
        logfunc(f'No Music Resume Data available')
__artifacts__ = {
    "MyLink Miscellaneous Data": (
        "MyLink Misc Data",
        ('*Resume.dat'),
        myLink_misc),
}