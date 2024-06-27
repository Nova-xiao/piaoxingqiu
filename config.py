
# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNp8kMFqwzAQRP9lzz5IsrRSfExJaSClEJpDT0Wy1sRgW0GWS9uQf6-CmtBTjzvM29nZMwS7pON26gI00zIMFSwzxTKfwfXfD8ETNPD4tHt_hgrmxa3vIgrU1jAiL7hRUmiDHZcrmX2Z3Ifhalof3jb7rIypPVxX-6wpx50lp0k65phXtbHWcMEKeLeh0l6T511Xc4WMMa4VoiC4VECfpz7Saz_S7fBMvpwo2hT-pX0OaSPZ9AtzzVdSYy0lq00u-DUnGkvBsnek2B7tlP4-KacXUqHQUlbwQXHuwwQNlg9O9nbY5QcAAP__.EHOhl3LVHJ6Lr9hw0ma4pu7lCk0X-NEYoz451t78J2ML1n8MBiPMIgw2De9psN1YErk7QOfezk8dPgV4uLC73ToOlX1bW-eS8opp0DyDVteDpE_IOszpsN6l3TJkqCc0ohtFvkmmhCusvLDobE1pvDnjjMRMoDr2-ZZtlF338K0'

# 项目id，必填
show_id = '66050ac51e59c10001881b4d'

# 指定场次id，不指定则默认从第一场开始遍历
session_id = ''

# 购票数量，一定要看购票须知，不要超过    上限
buy_count = 2

# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0, 1]

# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
# 新增,刷身份证: ID_CARD
deliver_method = ''

# Server酱SCKEY
sckey = ''