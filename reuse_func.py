import configparser
import boto.s3
import json
import os
import psycopg2
import requests
from get_dir import pwd
from selenium import webdriver


class GetData():
    def __init__(self):
        self.p = pwd()

    def get_domain_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['domain']

    def get_nifi_status(self):
        cal = GetData()
        nifi_domain = cal.get_domain_name()
        url = nifi_domain + "/nifi-api/process-groups/root/process-groups"
        response = requests.get(url)
        json_resp = json.loads(response.text)
        nifi_status = []
        for x in json_resp.values():
            for y in x:
                name = y['component']['name']
                runningCount = y['component']['runningCount']
                stoppedCount = y['component']['stoppedCount']
                disabledCount = y['component']['disabledCount']
                invalidCount = y['component']['invalidCount']
                component_dict = {"name": name, "runningCount": runningCount, "stoppedCount": stoppedCount,
                                  "disabledCount": disabledCount, "invalidCount": invalidCount}
                nifi_status.append((component_dict))
        return nifi_status

    def get_runningCount(self, processor_name):
        cal = GetData()
        nifi_componets = cal.get_nifi_status()
        for x in nifi_componets:
            if x.get('name') == processor_name:
                self.runningCount = x.get('runningCount')
        return self.runningCount

    def get_stoppedCount(self, processor_name):
        cal = GetData()
        nifi_componets = cal.get_nifi_status()
        for x in nifi_componets:
            if x.get('name') == processor_name:
                self.stoppedCount = x.get('stoppedCount')
        return self.stoppedCount

    def get_invalidCount(self, processor_name):
        cal = GetData()
        nifi_componets = cal.get_nifi_status()
        for x in nifi_componets:
            if x.get('name') == processor_name:
                self.invalidCount = x.get('invalidCount')
        return self.invalidCount

    def get_disabledCount(self, processor_name):
        cal = GetData()
        nifi_componets = cal.get_nifi_status()
        for x in nifi_componets:
            if x.get('name') == processor_name:
                self.disabledCount = x.get('disabledCount')
        return self.disabledCount

    def get_time_zone(self):
        cal = GetData()
        nifi_domain = cal.get_domain_name()
        url = nifi_domain + "/nifi-api/process-groups/root/process-groups"
        response = requests.get(url)
        json_resp = json.loads(response.text)
        for x in json_resp.values():
            for y in x:
                self.time = y['status']['statsLastRefreshed']
                break
        return self.time

    def get_username(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['username']

    def get_password(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['password']

    def get_driver(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.p.get_download_dir()}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
        return self.driver

    def open_cqube_appln(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_domain_name())
        self.driver.implicitly_wait(60)

    def login_cqube(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id("username").send_keys(self.get_username())
        self.driver.find_element_by_id("password").send_keys(self.get_password())
        self.driver.find_element_by_id("kc-login").click()
        self.driver.find_element_by_tag_name('button').click()

    def get_basedir(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['basedirpath']

    def connect_to_postgres(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        con = psycopg2.connect(host=config['config']['host'], database=config['config']['database'],
                               user=config['config']['user'], password=config['config']['db_password'])
        return con

    def get_db_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['database']

    def get_s3_files(self, folder):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        conn = boto.s3.connect_to_region(config['config']['aws_default_region'])
        bucket = conn.get_bucket(config['config']['s3_bucket'])
        files = []
        for key in bucket.list(prefix=folder, delimiter='*.json'):
            files.append(key.name.split("/"))
        return files

    def get_bucket(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        conn = boto.s3.connect_to_region(config['config']['aws_default_region'])
        bucket = conn.get_bucket(config['config']['s3_bucket'])
        return bucket

    def get_stackbar_all_list(self):
        lst = ['diksha/stack_bar_reports/2401.json', 'diksha/stack_bar_reports/2402.json',
               'diksha/stack_bar_reports/2403.json', 'diksha/stack_bar_reports/2404.json',
               'diksha/stack_bar_reports/2405.json', 'diksha/stack_bar_reports/2406.json',
               'diksha/stack_bar_reports/2407.json', 'diksha/stack_bar_reports/2408.json',
               'diksha/stack_bar_reports/2409.json', 'diksha/stack_bar_reports/2410.json',
               'diksha/stack_bar_reports/2411.json', 'diksha/stack_bar_reports/2412.json',
               'diksha/stack_bar_reports/2413.json', 'diksha/stack_bar_reports/2414.json',
               'diksha/stack_bar_reports/2415.json', 'diksha/stack_bar_reports/2416.json',
               'diksha/stack_bar_reports/2418.json', 'diksha/stack_bar_reports/2419.json',
               'diksha/stack_bar_reports/2420.json', 'diksha/stack_bar_reports/2421.json',
               'diksha/stack_bar_reports/2422.json', 'diksha/stack_bar_reports/2423.json',
               'diksha/stack_bar_reports/2424.json', 'diksha/stack_bar_reports/2425.json',
               'diksha/stack_bar_reports/2426.json', 'diksha/stack_bar_reports/2427.json',
               'diksha/stack_bar_reports/2428.json', 'diksha/stack_bar_reports/2429.json',
               'diksha/stack_bar_reports/2430.json', 'diksha/stack_bar_reports/2431.json',
               'diksha/stack_bar_reports/2432.json', 'diksha/stack_bar_reports/2433.json',
               'diksha/stack_bar_reports/All.json',
               'diksha/stack_bar_reports/diksha_metadata.json']
        return lst
    def get_stackbar_last_30_days_list(self):
        lst = ['diksha/stack_bar_reports/last_30_days/2401.json', 'diksha/stack_bar_reports/last_30_days/2402.json',
               'diksha/stack_bar_reports/last_30_days/2403.json', 'diksha/stack_bar_reports/last_30_days/2404.json',
               'diksha/stack_bar_reports/last_30_days/2405.json', 'diksha/stack_bar_reports/last_30_days/2406.json',
               'diksha/stack_bar_reports/last_30_days/2407.json', 'diksha/stack_bar_reports/last_30_days/2408.json',
               'diksha/stack_bar_reports/last_30_days/2409.json', 'diksha/stack_bar_reports/last_30_days/2410.json',
               'diksha/stack_bar_reports/last_30_days/2411.json', 'diksha/stack_bar_reports/last_30_days/2412.json',
               'diksha/stack_bar_reports/last_30_days/2413.json', 'diksha/stack_bar_reports/last_30_days/2414.json',
               'diksha/stack_bar_reports/last_30_days/2415.json', 'diksha/stack_bar_reports/last_30_days/2416.json',
               'diksha/stack_bar_reports/last_30_days/2418.json', 'diksha/stack_bar_reports/last_30_days/2419.json',
               'diksha/stack_bar_reports/last_30_days/2420.json', 'diksha/stack_bar_reports/last_30_days/2421.json',
               'diksha/stack_bar_reports/last_30_days/2422.json', 'diksha/stack_bar_reports/last_30_days/2423.json',
               'diksha/stack_bar_reports/last_30_days/2424.json', 'diksha/stack_bar_reports/last_30_days/2425.json',
               'diksha/stack_bar_reports/last_30_days/2426.json', 'diksha/stack_bar_reports/last_30_days/2427.json',
               'diksha/stack_bar_reports/last_30_days/2428.json', 'diksha/stack_bar_reports/last_30_days/2429.json',
               'diksha/stack_bar_reports/last_30_days/2430.json', 'diksha/stack_bar_reports/last_30_days/2431.json',
               'diksha/stack_bar_reports/last_30_days/2432.json', 'diksha/stack_bar_reports/last_30_days/2433.json',
               'diksha/stack_bar_reports/last_30_days/All.json']
        return lst
    def get_stackbar_last_7_days_list(self):
        lst = ['diksha/stack_bar_reports/last_7_days/2401.json', 'diksha/stack_bar_reports/last_7_days/2402.json',
               'diksha/stack_bar_reports/last_7_days/2403.json', 'diksha/stack_bar_reports/last_7_days/2404.json',
               'diksha/stack_bar_reports/last_7_days/2405.json', 'diksha/stack_bar_reports/last_7_days/2406.json',
               'diksha/stack_bar_reports/last_7_days/2407.json', 'diksha/stack_bar_reports/last_7_days/2408.json',
               'diksha/stack_bar_reports/last_7_days/2409.json', 'diksha/stack_bar_reports/last_7_days/2410.json',
               'diksha/stack_bar_reports/last_7_days/2411.json', 'diksha/stack_bar_reports/last_7_days/2412.json',
               'diksha/stack_bar_reports/last_7_days/2413.json', 'diksha/stack_bar_reports/last_7_days/2414.json',
               'diksha/stack_bar_reports/last_7_days/2415.json', 'diksha/stack_bar_reports/last_7_days/2416.json',
               'diksha/stack_bar_reports/last_7_days/2418.json', 'diksha/stack_bar_reports/last_7_days/2419.json',
               'diksha/stack_bar_reports/last_7_days/2420.json', 'diksha/stack_bar_reports/last_7_days/2421.json',
               'diksha/stack_bar_reports/last_7_days/2422.json', 'diksha/stack_bar_reports/last_7_days/2423.json',
               'diksha/stack_bar_reports/last_7_days/2424.json', 'diksha/stack_bar_reports/last_7_days/2425.json',
               'diksha/stack_bar_reports/last_7_days/2426.json', 'diksha/stack_bar_reports/last_7_days/2427.json',
               'diksha/stack_bar_reports/last_7_days/2428.json', 'diksha/stack_bar_reports/last_7_days/2429.json',
               'diksha/stack_bar_reports/last_7_days/2430.json', 'diksha/stack_bar_reports/last_7_days/2431.json',
               'diksha/stack_bar_reports/last_7_days/2432.json', 'diksha/stack_bar_reports/last_7_days/2433.json',
               'diksha/stack_bar_reports/last_7_days/All.json']
        return lst
    def get_stackbar_last_day_list(self):
        lst = ['diksha/stack_bar_reports/last_day/2401.json', 'diksha/stack_bar_reports/last_day/2402.json',
               'diksha/stack_bar_reports/last_day/2403.json', 'diksha/stack_bar_reports/last_day/2404.json',
               'diksha/stack_bar_reports/last_day/2405.json', 'diksha/stack_bar_reports/last_day/2406.json',
               'diksha/stack_bar_reports/last_day/2407.json', 'diksha/stack_bar_reports/last_day/2408.json',
               'diksha/stack_bar_reports/last_day/2409.json', 'diksha/stack_bar_reports/last_day/2410.json',
               'diksha/stack_bar_reports/last_day/2411.json', 'diksha/stack_bar_reports/last_day/2412.json',
               'diksha/stack_bar_reports/last_day/2413.json', 'diksha/stack_bar_reports/last_day/2414.json',
               'diksha/stack_bar_reports/last_day/2415.json', 'diksha/stack_bar_reports/last_day/2416.json',
               'diksha/stack_bar_reports/last_day/2418.json', 'diksha/stack_bar_reports/last_day/2419.json',
               'diksha/stack_bar_reports/last_day/2420.json', 'diksha/stack_bar_reports/last_day/2421.json',
               'diksha/stack_bar_reports/last_day/2422.json', 'diksha/stack_bar_reports/last_day/2423.json',
               'diksha/stack_bar_reports/last_day/2424.json', 'diksha/stack_bar_reports/last_day/2425.json',
               'diksha/stack_bar_reports/last_day/2426.json', 'diksha/stack_bar_reports/last_day/2427.json',
               'diksha/stack_bar_reports/last_day/2428.json', 'diksha/stack_bar_reports/last_day/2429.json',
               'diksha/stack_bar_reports/last_day/2430.json', 'diksha/stack_bar_reports/last_day/2431.json',
               'diksha/stack_bar_reports/last_day/2432.json', 'diksha/stack_bar_reports/last_day/2433.json',
               'diksha/stack_bar_reports/last_day/All.json']
        return lst

    def get_table_report_all_files(self,all):
        lst=[]
        for x in range(2401,2434):
            if x != 2417:
                lst.append("diksha/table_reports/"+str(all)+"/{}.json".format(x))
        lst.append("diksha/table_reports/"+str(all)+"/All.json")
        return lst
    def get_table_report_files(self,all):
        lst=[]
        for x in range(2401,2434):
            if x != 2417:
                lst.append("diksha/table_reports/all/{}/{}.json".format(all,x))
        lst.append("diksha/table_reports/all/{}/All.json".format(all))
        return lst
    def get_pat_grades_files(self):
        self.pat_grades=['Grade 3.json','Grade 4.json','Grade 5.json','Grade 6.json','Grade 7.json','Grade 8.json']
        return self.pat_grades
