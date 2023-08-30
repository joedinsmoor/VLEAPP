import csv
import os
import sqlite3
import re

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, logdevinfo, is_platform_windows, open_sqlite_db_readonly

#Compatability Data
vehicles = ['Chevrolet 2017+']
platforms = ['MyLink, Intellilink']
def myLink_devices(files_found, report_folder, seeker, wrap_text):
    data_list = []
    for file_found in files_found:
        with open(file_found, "r") as f:
            for line in f:
                model = f.splits()
        data_list.append((model))
            
    if len(data_list) > 0:
        report = ArtifactHtmlReport('Bluetooth Devices')
        report.start_artifact_report(report_folder, f'Bluetooth Devices')
        report.add_script()
        data_headers = ('model')
        file_found = os.path.dirname(file_found)
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
        
        tsvname = f'Bluetooth Devices'
        tsv(report_folder, data_headers, data_list, tsvname)
        
    else:
        logfunc(f'No Bluetooth Devices available')


__artifacts__ = {
    "MyLink Bluetooth Devices": (
        "MyLink Bluetooth Devices",
        ('bdAddr*.db*'),
        myLink_devices),
}