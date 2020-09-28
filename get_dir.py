import os


class pwd():
    def get_config_ini_path(self):
        cwd = os.path.dirname(__file__)
        ini = os.path.join(cwd, 'config.ini')
        return ini

    def get_nifi_processor_group_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/cQubeConfiguration.html')
        return report_path
    def get_driver_path(self):
        cwd = os.path.dirname(__file__)
        driver_path = os.path.join(cwd, 'Driver/chromedriver')
        return driver_path

    def get_download_dir(self):
        cwd = os.path.dirname(__file__)
        download_path = os.path.join(cwd, 'Downloads')
        return download_path
    def get_s3_report_path(self):
        cwd = os.path.dirname(__file__)
        report_path = os.path.join(cwd, 'Reports/s3FilesCheck.html')
        return report_path