import shutil
import subprocess

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from nginx_server_conf import *

app = FastAPI()

NGINX_CONF_PATH = "/etc/nginx/sites-enabled/"


class NginxConf(BaseModel):
    project_name: str
    # port: int
    # root_path: str


@app.post("/nginx")
def set_up_conf(conf: NginxConf):
    file_name = append_location_to_nginx(conf.project_name)
    shutil.copy(file_name, NGINX_CONF_PATH)
    subprocess.run("nginx -t", shell=True)
    cp = subprocess.run("nginx -s reload", shell=True)
    return {"status": cp.stdout}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000,
                log_level="info", reload=True)
