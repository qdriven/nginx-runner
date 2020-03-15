import sys
from string import Template


class NginxTemplate(Template):
    delimiter = "%"


def generate_server_config(server_name, port, root_path):
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
