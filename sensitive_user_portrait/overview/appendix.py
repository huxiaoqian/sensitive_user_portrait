# -*- coding:utf-8 -*-

import sys
import json
from sensitive_user_portrait.global_utils import es_user_profile

# domain
writer = ['1311967407', '1195347197', '1142648704', '1889213710', '1706987705']
expert = ['1827652007', '1265965213', '1596329427', '1908195982', '2248789552']
grassroot = ['1220291284', '1635764393', '2682546440', '3188186580', '1665808371']
religion = ['1218353337', '1761179351', '3482911112', '1220291284', '2504433601']
attorney = ['1215031834', '1701401324', '1935084477', '1840604224', '2752172261']
public_intellectual = ['1182389073', '1989660417', '1494720324', '1189591617', '1971861621']
non_public_owner = ['1182391231', '1640571365', '1197161814', '1191220232', '1749127163']
independent_media = ['1189729754', '1497882593', '1742566624', '1661598840', '2283406765']
public_media = ['2803301701', '1974576991', '1639498782', '2105426467', '1644648333']
civil_officer = ['1419517335', '1098736570', '1729736051', '2419062270', '1369714780']
star = ['1687429295', '1195300800', '1997641692', '1746274673', '1223178222']
commonweal = ['3299094722', '1342829361', '1946798710', '1894477791', '1958321657']

domain_dict = {'作家写手': writer, '专家学者': expert, '草根红人': grassroot, '宗教人士': religion, \
        '维权律师': attorney, '公知分子': public_intellectual, '非公企业主': non_public_owner, \
        '独立媒体人': independent_media, '官方媒体': public_media, '公职人员': civil_officer, \
        '文体明星': star, '社会公益': commonweal}
index_name = 'weibo_user'
index_type = 'user'

def get_top_user():
    results = dict()
    for domain in domain_dict:
        results[domain] = []
        user_list = domain_dict[domain]
        profile_result = es_user_profile.mget(index=index_name, doc_type=index_type, body={'ids':user_list})['docs']
        for profile in profile_result:
            uid = profile['_id']
            try:
                uname = profile['_source']['nick_name']
                photo_url = profile['_source']['photo_url']
            except:
                uname = 'unknown'
                photo_url = 'unknown'
            results[domain].append([uid, uname, photo_url])
    return results

# topic
zongjiao = ['1218353337', '1761179351', '3482911112', '1220291284', '2504433601']
yishi = ['1214219230', '1195818302', '1567762360', '1654592030', '2280198017']
kongbu = ['1497418902', '2548067870', '2752172261', '3049817110', '1960785875']
wending = ['1661598840', '1644489953', '1840604224', '1701401324', '1215031834']
minyun = ['1311967407', '3200285974', '2803301701', '3270699555', '1644307977']
gangaotai = ['1771665174', '2504433601', '2632236847', '1843749702', '1971861621']
shewai = ['2181597154', '1649159940', '2263972354', '1743951792', '2647349703']
xiejiao = ['3902988319', '1644489953', '2283710290', '5305757517', '1974576991']

search_dict = {'宗教': zongjiao, '意识形态': yishi, '民族及恐怖主义': kongbu, '民生稳定': wending, '民运': minyun, \
        '港澳台': gangaotai, '涉外': shewai, '邪教': xiejiao}

# topic
def get_topic_user():
    result = {}
    index_name = 'weibo_user'
    index_type = 'user'
    '''
    test_user_list = [['1499104401', '1265965213', '3270699555', '2073915493', '1686474312'],\
            ['2803301701', '2105426467', '1665372775', '3716504593', '2892376557'],\
            ['1457530250', '1698513182', '2793591492', '2218894100', '1737961042'],\
            ['1656818110', '1660127070', '1890124610', '1182391230', '1243861100'],\
            ['1680430844', '2998045524', '2202896360', '1639498782', '3494698730'],\
            ['2587093162', '1677675054', '1871767009', '1193111400', '1672418622'],\
            ['1730726640', '1752502540', '1868725480', '1262486750', '1235733080'],\
            ['1250041100', '2275231150', '1268642530', '1658606270', '1857599860'],\
            ['1929496477', '2167425990', '1164667670', '2417139911', '1708853044'],\
            ['1993292930', '1645823930', '1890926610', '1641561810', '2023833990'],\
            ['2005471590', '1233628160', '2074684140', '1396715380', '1236762250'],\
            ['1423592890', '2612799560', '1926127090', '2684951180', '1760607220']]
    '''
    for topic in search_dict:
        result[topic] = []
        user_list = search_dict[topic]
        profile_result = es_user_profile.mget(index=index_name, doc_type=index_type, body={'ids':user_list})['docs']
        for profile in profile_result:
            uid = profile['_id']
            try:
                uname = profile['_source']['nick_name']
                photo_url = profile['_source']['photo_url']
            except:
                uname = 'unknown'
                photo_url = 'unknown'
            result[topic].append([uid, uname, photo_url])
    return result





