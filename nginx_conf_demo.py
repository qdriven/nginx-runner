from nginx.config.api import Section, Location
from nginx.config.builder import NginxConfigBuilder

# build nginx
nginx = NginxConfigBuilder(daemon='on')
print(nginx)

with nginx.add_server() as server:
    server.add_route('/project1').end()

print(nginx)

## build server section
# root % root_path;
# try_files $uri $uri / / index.html;
# index
# index.html;

server = Section('server',Location("/foo",root="/var/www/foo"
                                   ,try_files = "$uri $uri / / index.html",
                                   index ="index.html"))
print(server)

location = Location("/foo",root="/var/www/foo"
                                   ,try_files = "$uri $uri / / index.html",
                                   index ="index.html")
print(str(location))