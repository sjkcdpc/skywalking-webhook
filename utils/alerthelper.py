import json
import time
from WorkWeixinRobot.work_weixin_robot import WWXRobot

alert_msg = b'[{"scopeId":2,"scope":"SERVICE_INSTANCE","name":"bx_regservice_pro-pid:1@regsys-sftnet5g-gsregsyswinservice-deploy-79fc56cf96-lpqz2","id0":31976,"id1":0,"ruleName":"service_instance_resp_time_rule","alarmMessage":"Response time of service instance bx_regservice_pro-pid:1@regsys-sftnet5g-gsregsyswinservice-deploy-79fc56cf96-lpqz2 is more than 1000ms in 2 minutes of last 10 minutes","startTime":1661910198310},{"scopeId":2,"scope":"SERVICE_INSTANCE","name":"bx_studentapi_test-pid:1@studentapi-test-beixiao-private-dev-765fbb6d49-k5d54","id0":26287,"id1":0,"ruleName":"service_instance_resp_time_rule","alarmMessage":"Response time of service instance bx_studentapi_test-pid:1@studentapi-test-beixiao-private-dev-765fbb6d49-k5d54 is more than 1000ms in 2 minutes of last 10 minutes","startTime":1661910198310}]'

alert_msg = b'[{"scopeId":1,"scope":"SERVICE","name":"bx_studentapi_pro","id0":12340,"id1":0,"ruleName":"service_resp_time_percentile_rule","alarmMessage":"Percentile response time of service bx_studentapi_pro alarm in 3 minutes of last 10 minutes, due to more than one condition of p50 \\u003e 1000, p75 \\u003e 1000, p90 \\u003e 1000, p95 \\u003e 1000, p99 \\u003e 1000","startTime":1661922196853},{"scopeId":1,"scope":"SERVICE","name":"bx_gateway_test","id0":42,"id1":0,"ruleName":"service_resp_time_percentile_rule","alarmMessage":"Percentile response time of service bx_gateway_test alarm in 3 minutes of last 10 minutes, due to more than one condition of p50 \\u003e 1000, p75 \\u003e 1000, p90 \\u003e 1000, p95 \\u003e 1000, p99 \\u003e 1000","startTime":1661922196853},{"scopeId":1,"scope":"SERVICE","name":"bx_crm_test","id0":38,"id1":0,"ruleName":"service_resp_time_percentile_rule","alarmMessage":"Percentile response time of service bx_crm_test alarm in 3 minutes of last 10 minutes, due to more than one condition of p50 \\u003e 1000, p75 \\u003e 1000, p90 \\u003e 1000, p95 \\u003e 1000, p99 \\u003e 1000","startTime":1661922196853},{"scopeId":1,"scope":"SERVICE","name":"bx_crm_pro","id0":423,"id1":0,"ruleName":"service_resp_time_percentile_rule","alarmMessage":"Percentile response time of service bx_crm_pro alarm in 3 minutes of last 10 minutes, due to more than one condition of p50 \\u003e 1000, p75 \\u003e 1000, p90 \\u003e 1000, p95 \\u003e 1000, p99 \\u003e 1000","startTime":1661922196853},{"scopeId":1,"scope":"SERVICE","name":"bx_regapi_test","id0":37,"id1":0,"ruleName":"service_resp_time_percentile_rule","alarmMessage":"Percentile response time of service bx_regapi_test alarm in 3 minutes of last 10 minutes, due to more than one condition of p50 \\u003e 1000, p75 \\u003e 1000, p90 \\u003e 1000, p95 \\u003e 1000, p99 \\u003e 1000","startTime":1661922196853}]'
WX_ROBOT_KEY = "79041d52-5d1c-4415-89d6-4475fd7fe805"


def send_msg(_wx_robot_key, _msg, ):
    rbt = WWXRobot(key=_wx_robot_key)
    content = '\n'.join([
        '【SkyWalking告警通知】',
        '{}'.format('----------------------------------------------------------------'.join(_msg)),
    ])
    print(content)
    rbt.send_markdown(content=content)


alert_type_dict = {
    'SERVICE_INSTANCE': '服务实例',
    'SERVICE': '服务',
}


def format_alert_msg(_alert_msg, _skywalking_url):
    send_info = []
    instance_list = json.loads(_alert_msg.decode('utf-8'))
    for instance in instance_list:
        scope_id = instance.get('scopeId')
        scope = alert_type_dict.get(instance.get('scope'), )
        name = instance.get('name')
        id0 = instance.get('id0')
        id1 = instance.get('id1')
        rule_name = instance.get('ruleName')
        alarm_gessage = instance.get('alarmMessage')
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(str(instance.get('startTime'))[:10])))

        info = """
告警级别: P{}
告警类型: {}
故障主机: {}
告警主题: {}
告警详情: {}
触发时间: {}
告警发送: [{}]({})
        """.format(
            id1, scope, name, rule_name, alarm_gessage, start_time, _skywalking_url, _skywalking_url
        )
        # 判断环境，是有线上环境发布告警
        if "_dev" not in name and "_test" not in name:
            send_info.append(info)
            # print(info)
    return send_info

# if __name__ == '__main__':
#     msg = format_alert_msg(alert_msg)
#     send_msg(msg)
