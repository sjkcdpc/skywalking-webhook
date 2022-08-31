# 概述

Skywalking通过配置webhook来定制化实现钉钉、企微、邮件告警

# 安装
```
git clone https://github.com/sjkcdpc/skywalking-webhook.git webhook
cd webhook
python3 -m venv venv
source venv/bin/active
pip install -r requirements/requirement.txt
export FLASK_ENV=development
python app.py
nohup python main.py &

```

# 参考资料
- https://www.itmuch.com/skywalking/alert/

# to-do-list
- ~~企微机器人报警~~
- 邮件告警
- 钉钉报警
- 飞书报警
