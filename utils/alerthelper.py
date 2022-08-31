import json
from WorkWeixinRobot.work_weixin_robot import WWXRobot

alert_msg = b'[{"scopeId":2,"scope":"SERVICE_INSTANCE","name":"bx_regservice_pro-pid:1@regsys-sftnet5g-gsregsyswinservice-deploy-79fc56cf96-lpqz2","id0":31976,"id1":0,"ruleName":"service_instance_resp_time_rule","alarmMessage":"Response time of service instance bx_regservice_pro-pid:1@regsys-sftnet5g-gsregsyswinservice-deploy-79fc56cf96-lpqz2 is more than 1000ms in 2 minutes of last 10 minutes","startTime":1661910198310},{"scopeId":2,"scope":"SERVICE_INSTANCE","name":"bx_studentapi_test-pid:1@studentapi-test-beixiao-private-dev-765fbb6d49-k5d54","id0":26287,"id1":0,"ruleName":"service_instance_resp_time_rule","alarmMessage":"Response time of service instance bx_studentapi_test-pid:1@studentapi-test-beixiao-private-dev-765fbb6d49-k5d54 is more than 1000ms in 2 minutes of last 10 minutes","startTime":1661910198310}]'

WX_ROBOT_KEY = "79041d52-5d1c-4415-89d6-4475fd7fe805"


def send_msg(_wx_robot_key, _msg, ):
    rbt = WWXRobot(key=_wx_robot_key)
    content = '\n'.join([
        '【SkyWalking告警通知】',
        '{}'.format('----------------------------------------------------------------'.join(_msg)),
    ])
    print(content)
    rbt.send_markdown(content=content)


def format_alert_msg(_alert_msg, _skywalking_url):
    send_info = []
    instance_list = json.loads(alert_msg.decode('utf-8'))
    for instance in instance_list:
        scope_id = instance.get('scopeId')
        scope = instance.get('scope')
        name = instance.get('name')
        id0 = instance.get('id0')
        id1 = instance.get('id1')
        rule_name = instance.get('ruleName')
        alarm_gessage = instance.get('alarmMessage')
        start_time = instance.get('startTime')

        info = """
告警级别: P1
告警类型: {}
故障主机: {}
告警主题: {}
告警详情: {}
触发时间: {}
告警阈值: {}
告警发送: [{}]({})
        """.format(
            scope, name, rule_name, alarm_gessage, start_time, id0, id1, _skywalking_url, _skywalking_url
        )
        # 判断环境，是有线上环境发布告警
        if "_pro-" in name:
            send_info.append(info)
            # print(info)
    return send_info

# if __name__ == '__main__':
#     msg = format_alert_msg(alert_msg)
#     send_msg(msg)
