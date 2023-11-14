class Const():
    DOMAIN_REGEX = r'([|\/=\.~]?)(([\w-]{3,255})(\.[a-z]{2,3})?(\.[a-z]{2,7}))([#\/|\n\^\$,])'
    SUB_DOMAIN_REGEX = r'([|\/=\.~]?)(([\w-]+\.){1,3}(([\w-]{3,255})(\.[a-z]{2,3})?(\.[a-z]{2,7})))([#\/|\n\^\$,])'
    TLD_DOMAIN_REGEX = r'([\w-]+\.\w+)\/'
    REJECT_ENDINGS = [
        '.js', '.png', '.jpg', '.gif', '.aspx',
        '.widget', 'block.ad', '.mp4', '.mp3', '.m3u8',
        '.row', '.parse', '.round', 'abpvn.com',
        'abpvn.org', '.php', '.html', '.button', '.mrb10',
        '.modal', '.ico', '.error', '.write', '.webp', 'PanelScroller.Notices',
        'firstmessfloadright.samItem', 'banner-top-box.click',
        'clear.hd', 'info.card', 'left.box', 'right.box',
        'blqPr.nwsItHm', 'text-center.adsense', '.btn', '.show',
        'show.fade', 'parent.special', 'flex-1.table'
    ]
    SKIP_CHECK_REDIRECT = [
        'amazonaws.com', 'blogspot.com', 'blogtruyen.com', 'fptplay.net',
        'doubleclick.net', 'github.io', 'herokuapp.com', 'zing.vn', 'com.vn',
        'net.vn', 'edu.vn', 'googlesyndication.com', 'gov.vn', 'nct.vn', 'org.vn',
        'phukienthoitranggiare.com', 'cloudfront.net', 'admarketplace.net'
    ]
    REJECT_TARGET_DOMAIN = [
        'google.com', 'facebook.com', 'yahooinc.com'
    ]
    FILE_REGEX = r"\|\|([^*\n]+\.(js|png|webp|jpg|jpeg|mp4|gif))([\n\$])"
    ELEMENT_HIDE_REGEX = r"(^|,){domain}([,.\w]+)?#(@)?#([\.\w\-\=\"\'\>\ \+\+\#\[\]\:]+)$"
    MAX_CHROME_THREAD = 100
    NETWORK_RULE_REGEXS = {
        "TYPE1": r"\|\|({domain}([\w\*\^\.\/\^\-\?\=]+))(.+)?$",
        "TYPE2": r"\|\|([\.\-\w\^\*\/]+)([,$])?(.+)?domain=([.|\w]+)?{domain}"
    }
    NETWORK_RULE_SKIPS = {
        "TYPE1": [
            "{domain}^"
        ],
    }
    NETWORK_RULE_REPLACE = [
        ["^*", ".*"],
        ["^", ""]
    ]
