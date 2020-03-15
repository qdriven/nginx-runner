import shutil
import subprocess

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from nginx_server_conf import generate_server_config

app = FastAPI()

NGINX_CONF_PATH = "/etc/nginx/sites-enabled/"


class NginxConf(BaseModel):
    project_name: str
    port: int
    root_path: str


@app.post("/nginx")
def set_up_conf(conf: NginxConf):
    file_name = generate_server_config(conf.project_name, conf.port, conf.root_path)
    shutil.copy(file_name, NGINX_CONF_PATH)
    subprocess.run("sudo nginx -t", shell=True)
    cp = subprocess.run("sudo nginx -s reload", shell=True)
    return {"status": cp.stdout}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000,
                log_level="info", reload=True)
