import json
from string import Template

from nginx.config.api import Location


class NginxTemplate(Template):
    delimiter = "%"

# todo: add if there is no configuration file
def load_nginx_configuration():
    with open("nginx_setting.json", "r") as setting:
        locations_setting = json.load(setting)
    return locations_setting


nginx_settings = load_nginx_configuration()
default_root_path = "/var/www"
NGINX_CONF_FILE = "nginx.conf"


def update_nginx_setting(project_name):
    nginx_setting = {
        "root": default_root_path + "/" + project_name,
        "try_files": "$uri $uri / / index.html",
        "index": "index.html"
    }
    nginx_settings["locations"][project_name] = nginx_setting
    write_to_nginx_setting(nginx_settings)


def write_to_nginx_setting(nginx_json_setting):
    with open('nginx_setting.json', 'w', encoding='utf8') as setting:
        json.dump(nginx_json_setting, setting)


def append_location_to_nginx(project_name):
    update_nginx_setting(project_name=project_name)
    location_str = []
    for project_name, setting in nginx_settings["locations"].items():
        location = Location("/" + project_name, root=setting["root"]
                            , try_files=setting["try_files"],
                            index=setting["index"])
        location_str.append(str(location))

    generate_server_by_locations("".join(location_str))
    return NGINX_CONF_FILE

def generate_server_by_locations(locations):
    with open('server.conf', 'r', encoding='utf-8') as conf:
        lines = conf.readlines()
        conf_temp = NginxTemplate("".join(lines))
        conf_content = conf_temp.substitute(locations=locations)

    with open(NGINX_CONF_FILE, 'w', encoding="utf-8") as new_conf:
        new_conf.write(conf_content)
    return True


def generate_server_config(server_name="default_server", port=8080, root_path="/var/www"):
    with open('server.conf', 'r', encoding='utf-8') as conf:
        lines = conf.readlines()
        conf_temp = NginxTemplate("".join(lines))
        conf_content = conf_temp.substitute(project_name=server_name, port=port, root_path=root_path)

    with open(server_name, 'w', encoding="utf-8") as new_conf:
        new_conf.write(conf_content)
    return server_name

# if __name__ == '__main__':
#     server_name = sys.argv[1]
#     # server_name = "project1"
#     port = sys.argv[2]
#     port = 8081
#     root_path = sys.argv[3]
#     # root_path = "/var/www/project1"
#     generate_server_config(server_name, port, root_path)
