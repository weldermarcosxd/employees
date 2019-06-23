import os
import logging
import subprocess
from agatereports.adapters import MysqlAdapter
from agatereports.basic_report import BasicReport
from datetime import datetime
from time import time


class DepartmentRpt(object):
    def print(self):
        logger.info('running datasource mysql sample')
        jrxml_filename = './reports/departments.jrxml'  # input jrxml filename
        output_filename = 'output\datasource_mysql.pdf'  # output pdf filename

        # MySQL datasource
        config = {'host': 'localhost', 'port': '3306', 'user': 'root',
                  'password': 'rock', 'database': 'employees'}
        data_source = MysqlAdapter(**config)

        pdf_page = BasicReport(jrxml_filename=jrxml_filename,
                               output_filename=output_filename, data_source=data_source)
        print(datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))
        pdf_page.generate_report()
        print(datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'))

        path = os.path.abspath((os.path.join(os.getcwd(), output_filename)))
        subprocess.Popen('%s' % path, shell=True)


logger = logging.getLogger(__name__)
