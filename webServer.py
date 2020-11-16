import os

import flask
import json
import configparser
from flask import request

server = flask.Flask(__name__)


class MyConfig:
    server_port = ''
    server_ip = ''
    nginx_config_path = ''
    nginx_path = ''


config = []

# init config
def init_config():
    root_dir = os.path.dirname(os.path.abspath('.'))
    cf = configparser.ConfigParser()
    cf.read(root_dir + "/nginx-ip-fusing/config.ini")

    config = MyConfig()

    config.server_port = cf.get("WebServer", "web-server-port")
    config.server_ip = cf.get("WebServer", "web-server-ip")
    config.nginx_config_path = cf.get("Nginx", "nginx-config-path")
    config.nginx_path = cf.get("Nginx", "nginx-path")

    return config


@server.route('/auto_nginx', methods=['get'])
def auto_nginx():
    p_type = request.args.get('type')
    ip = request.args.get('id')
    port = request.args.get('port')
    if p_type == '':
        p_type = 1

    resu = {'code': 100, 'result': 'success!'}


    try:
        if p_type == '1':
            result_number = os.system("./shell/openServer.sh '" + ip + "' '" + port + "' 0 '" + config.nginx_config_path + "' '" + config.nginx_path + "'")
            resu['result'] = result_number
        else:
            result_number = os.system("./shell/closeServer.sh '" + ip + "' '" + port + "' 0 '" + config.nginx_config_path + "' '" + config.nginx_path + "'")
            resu['result'] = result_number

    except Exception as e:
        print(e)

        resu = {'code': 109, 'result': 'fail!'}

    return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    config = init_config()
    server.run(debug=False, port=config.server_port, host=config.server_ip)
