import boto.s3

conn = boto.s3.connect_to_region('ap-south-1')
bucket = conn.get_bucket('cqube-qa5-output')

folders = bucket.list("","/")

for key in bucket.list(prefix="diksha/table_reports/", delimiter='*.json'):
        print(str(key.name))
# lst2=[]
# lst=['diksha/stack_bar_reports/2401', 'diksha/stack_bar_reports/2402', 'diksha/stack_bar_reports/2403', 'diksha/stack_bar_reports/2404', 'diksha/stack_bar_reports/2405', 'diksha/stack_bar_reports/2406', 'diksha/stack_bar_reports/2407', 'diksha/stack_bar_reports/2408', 'diksha/stack_bar_reports/2409', 'diksha/stack_bar_reports/2410', 'diksha/stack_bar_reports/2411', 'diksha/stack_bar_reports/2412', 'diksha/stack_bar_reports/2413', 'diksha/stack_bar_reports/2414', 'diksha/stack_bar_reports/2415', 'diksha/stack_bar_reports/2416', 'diksha/stack_bar_reports/2417', 'diksha/stack_bar_reports/2418', 'diksha/stack_bar_reports/2419', 'diksha/stack_bar_reports/2420', 'diksha/stack_bar_reports/2421', 'diksha/stack_bar_reports/2422', 'diksha/stack_bar_reports/2423', 'diksha/stack_bar_reports/2424', 'diksha/stack_bar_reports/2425', 'diksha/stack_bar_reports/2426', 'diksha/stack_bar_reports/2427', 'diksha/stack_bar_reports/2428', 'diksha/stack_bar_reports/2429', 'diksha/stack_bar_reports/2430', 'diksha/stack_bar_reports/2431', 'diksha/stack_bar_reports/2432', 'diksha/stack_bar_reports/2433','diksha/stack_bar_reports/All.json','diksha/stack_bar_reports/diksha_metadata.json']
# for x in lst:
#         for key in bucket.list(prefix=x, delimiter='*.json'):
#                 lst2.append(x)
# print(lst2)

# import unittest
# from reuse_func import GetData
# class student(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         self.cal = GetData()
#         self.student_files=[['attendance', 'cluster_attendance_opt_json_2018_9.json'], ['attendance', 'district_attendance_opt_json_2018_9.json'], ['attendance', 'school_attendance_opt_json_2018_9.json'], ['attendance', 'student_attendance_meta.json']]
#
#     def test_student_files(self):
#         print(self.student_files)
#         # for x in self.student_files:
#         #     if x[len(x) - 1].__contains__("district"):
#         #         print("student attendance district file generated successfully")
#         #     elif  x[len(x) - 1].__contains__("block"):
#         #         print("student attendance block file generated successfully")
#         #     elif x[len(x) - 1].__contains__("cluster"):
#         #         print("student attendance cluster file generated successfully")
#         #     elif x[len(x) - 1].__contains__("school"):
#         #         print("student attendance school file generated successfully")
#         #     elif x[len(x) - 1].__contains__("student_attendance_meta"):
#         #         print("student attendance meta file generated successfully")
#         #     else:
#         #         raise self.failureException('data not found')
#
#     @classmethod
#     def tearDownClass(self):
#         print("")
#
#
