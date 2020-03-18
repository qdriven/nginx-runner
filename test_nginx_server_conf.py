# encoding: utf-8
from unittest import TestCase

from nginx_server_conf import update_nginx_setting, load_nginx_configuration, nginx_settings, append_location_to_nginx


class TestNginxConfig(TestCase):
    def test_update_nginx_setting(self):
        update_nginx_setting("project1")

    def test_load_nginx_setting(self):
        load_nginx_configuration()
        print(nginx_settings)

    def test_generate_server_conf(self):
        append_location_to_nginx("project2")