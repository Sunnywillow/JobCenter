from ronglian_sms_sdk import SmsSDK

import json

# accId = '容联云通讯分配的主账号ID'
# accToken = '容联云通讯分配的主账号TOKEN'
# appId = '容联云通讯分配的应用ID'
accId = '8aaf0708732220a60173fc86aa345d69'
accToken = 'cddfd02d8a95448da91924c53a1be2fc'
appId = '8aaf0708732220a60173fc86ab0b5d70'


# class CCP(object):
#     """自己封装的发送短信的辅助类"""
#
#
#
#     def send_mss(self, ):
#         def send_message():
#             sdk = SmsSDK(accId, accToken, appId)
#             tid = '容联云通讯创建的模板'
#             mobile = '手机号1,手机号2'
#             datas = ('变量1', '变量2')
#             resp = sdk.sendMessage(tid, mobile, datas)
#             print(resp)


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    # tid = '容联云通讯创建的模板'
    # mobile = '手机号1,手机号2'
    # datas = ('变量1', '变量2')
    tid = '1'
    mobile = '18506243060'
    datas = ('1234',)
    resp = sdk.sendMessage(tid, mobile, datas)

    print(resp)
    resp_dict = json.loads(resp)
    status_code = resp_dict.get("statusCode")
    # print(status_code)
    if status_code == 000000 :
        # 发送成功
        return 0
    else:
        # 发送失败
        return 1


if __name__ == '__main__':
    send_message()

