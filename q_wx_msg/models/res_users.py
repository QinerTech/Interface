# coding=utf-8

from openerp import models, fields
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

import base64#file encode
import urllib2 #file download from url

conf = WechatConf(
    token='your_token',
    appid='your_appid',
    appsecret='your_appsecret',
    encrypt_mode='safe',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='your_encoding_aes_key'  # 如果传入此值则必须保证同时传入 token, appid
)

wechat = WechatBasic(conf=conf)

class ResUsersWechatMsg(models.Model):
    _inherit = 'res.users'

    openid = fields.Char(
        string='Wechat openId',
        required=False,
        index=False,
        size=250,
        default=None,
    )

    image = fields.binary(
        string='Image',
        frequired=True
    )

    web = fields.char(
        string='image url',
        help='Automatically sanitized HTML contents'
    )

    def onchange_image(self, cr, uid, ids, web, context=None):
        link = web
        photo = base64.encodestring(urllib2.urlopen(link).read())
        val = {
            'image': photo,
        }
        return {'value': val}