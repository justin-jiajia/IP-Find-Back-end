from ip_from import CzIp
from apiflask import APIFlask, Schema
from apiflask.validators import Regexp
from apiflask.fields import String, List

api = APIFlask(__name__, 'IP查找', '0.2')
api.config['SWAGGER_UI_CSS'] = 'https://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/swagger-ui/4.5.2/swagger-ui.min.css'
api.config[
    'SWAGGER_UI_BUNDLE_JS'] = 'https://lf6-cdn-tos.bytecdntp.com/cdn/expire-1-M/swagger-ui/4.5.2/swagger-ui-bundle.min.js'
api.config[
    'SWAGGER_UI_STANDALONE_PRESET_JS'] = 'https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/swagger-ui/4.5.2/swagger-ui-standalone-preset.min.js'
ip_search = CzIp()
IP_RE = r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)\.)(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-4]|2[0-4][0-9]|1[0-9][0-9]|0?[0-9]?[1-9]|0?[1-9]0)$'


class GetIpIn(Schema):
    ip = String(required=True, validate=Regexp(regex=IP_RE, error='"{input}" is not a right IPV4 address'))


class GetIpOut(Schema):
    ip_from = String()


class GetIpsIn(Schema):
    ips = List(String(required=True, validate=Regexp(regex=IP_RE, error='"{input}" is not a right IPV4 address')))


class GetIpsOut(Schema):
    ip_from = List(String())


class GetAboutOut(Schema):
    about = String()


@api.post('/get_one_ip/')
@api.input(GetIpIn)
@api.output(GetIpOut)
def get_one_ip(d):
    ip_from = ip_search.get_addr_by_ip(d['ip'])
    return {'ip_from': ip_from}


@api.post('/get_ips/')
@api.input(GetIpsIn)
@api.output(GetIpsOut)
def get_ips(d):
    o = []
    for i in d['ips']:
        o.append(ip_search.get_addr_by_ip(i))
    return {'ip_from': o}


@api.get('/get_about/')
@api.output(GetAboutOut)
def get_about():
    return {'about': ip_search.get_version()}
