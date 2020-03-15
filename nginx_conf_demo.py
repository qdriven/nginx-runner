from nginx.config.builder import NginxConfigBuilder

nginx = NginxConfigBuilder(daemon='on')
print(nginx)

with nginx.add_server() as server:
    server.add_route('/project1').end()

