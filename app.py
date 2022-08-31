from config import config

from flask import Flask, current_app, jsonify, request
from utils.alerthelper import format_alert_msg, send_msg

app = Flask(__name__)


@app.route('/web_hook_rec/', methods=['GET', 'POST'])
def web_hook_rec():
    """
    web hook 用于接收webhook请求并告警
    例如: Pinpoint、SkyWalking
    :return:
    """
    data = request.get_data()
    current_app.logger.info(data)
    send_info = format_alert_msg(data, config.skywalking_url)
    current_app.logger.info(send_info)
    if len(send_info) > 0:
        send_msg(config.wx_robot_key, send_info)
    return jsonify('200')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
