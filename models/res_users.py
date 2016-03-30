# coding=utf-8

from openerp import models, fields



class ResUsersAliIsv(models.Model):
    _inherit = 'res.users'

    openid = fields.Char(
        string= 'Wechat openId',
        required = False,
        index= False,
        size= 250,
        default= None,
    )
