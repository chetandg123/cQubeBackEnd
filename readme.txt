Execution of automation testscripts for both installation and upgradation of backend configuration

  python3 -m unittest TestSuites/run_configuration.py

Automation testscripts to check the json files in the s3 output bucket

   python3 -m unittest TestSuites/check_student_attendance_s3_files.py
   python3 -m unittest TestSuites/check_crc_s3_files.py
   python3 -m unittest TestSuites/check_semester_s3_files.py
   python3 -m unittest TestSuites/check_schoolinfra_s3_files.py
   python3 -m unittest TestSuites/check_diksha_s3_files.py
   python3 -m unittest TestSuites/check_udise_s3_files.py
   python3 -m unittest TestSuites/check_pat_s3_files.py
   python3 -m unittest TestSuites/check_composite_s3_files.py
   python3 -m unittest TestSuites/check_log_summary_s3_files.py
   
Mandatory fields for installation and upgradation of backend configuration and also to check the json files in the s3 output bucket
   
[config]
domain=
username=
password= 
basedirpath= # installation directory provided in the config.yml file ex:/opt
host=localhost
port=5432
database= # db name which is provided in the config.yml file
user= # db user which is provided in the config.yml file
db_password= # db user which is provided in the config.yml file
aws_default_region=ap-south-1
s3_bucket= # s3 output bucket name which is provided in the config.yml file
  

