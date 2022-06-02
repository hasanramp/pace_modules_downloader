import requests
from PIL import Image
import os
# from scraper import save_pdf, decode_base64

import base64
import requests
import re

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    try:
        return base64.b64decode(data, altchars)
    except base64.binascii.Error:
        print(data)

def download_pdf(arr, dir):
    x = 0
    for link in arr:
        xstr = str(x)
        content = requests.get(link).content
        decoded_content = decode_base64(content[150:-8])
        with open(f'{dir}/page{xstr}.jpg', 'wb') as f:
            f.write(decoded_content)

        x += 1
def save_pdf(dir_, pages):
    img_list = []
    im1 = Image.open(f'{dir_}/page0.jpg').convert('RGB')

    # parses images one by one and appends to img_list list
    for x in range(1, pages):
        xstr = str(x)
        img = Image.open(f'{dir_}/page{xstr}.jpg').convert('RGB')
        img_list.append(img)

    # saves all images as one pdf file
    im1.save(f'{dir_}.pdf', save_all=True, append_images=img_list)

    # moves pdf to modules folder
    try:
        os.rename(f'{dir_}.pdf', f'modules/{dir_}.pdf')
    except FileNotFoundError:
        os.mkdir('modules')
arr = ["https://videos.online.digitalpace.in/697509/page_1638453319-1.page?Expires=1654148324&Signature=Ta1M2hVPmObHSj3g6KlWHcHysW3Y2Rh9rzJ8SVoB2x9jkwzyXBcmCqXM1xs~g7~GNSoZKJJL4hxjBHfh8-TMGgoUNb9TkRVNjkQxgYfDWrRoPdVzuFSICvr9mswr5hXAzIYhMah8WbnmAORJyT0nhujr-6607shfAHTfV7geTxI_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-2.page?Expires=1654148350&Signature=XU9ZW5zZlSIhQrcD-4UUNB1VlAGAiJO9fPoTQujHaY2GKdz9lEF8-bbRsEu1HUhOo750kgq~N7OdM4nlzz-GkTAeuDIr96uupzc6SzVlmxMOilLg1jrCsVJJGujVOFnIBL8zztmBDDO8-0ZqjmzeoNXlq4TwOW1ClJOKEijHizw_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-3.page?Expires=1654148353&Signature=AN8QVSn-dX2nrldTyySOpYvLvT53hpuNkEXwZ6DBjiExWGwPBV0t2vbpEsyru-z3ohrh~0ubVwHN1fWOeB1DzPeXy3VK-johgTW5sivOPFvg0ackBDJekYLNMvoezuxeT6sC5l6DyIHrAp82gXJ1ZZTbWWeGa2C0j-f6PvcmuxE_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-4.page?Expires=1654148357&Signature=AXCM8p7IXng3NI10yeTarsk5OUnQtgf14d-xwTBHr9BfBpZ1bfFRmiI0PIlTJcChMa7dsFIMC8t4MlSXIHQbEQbESyQjXDM0FdIYkjfzJ4zTl4Xd1IVNrLfuNgU-9prz7jo2T7-oNM3qFw86AjKMvxgO~i-iRUeLvmPFuJtGL10_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-5.page?Expires=1654148360&Signature=j6QTxRYT6OwyUNJOIMB6NQ7wiDVwyz7UnKQMGlrhmqLwTzCOTMDvz6mv5Udwi-qSuXsufS4Fxn7Luiwja78BR3OHlaWZ~3wAw~sv9yAv36yfL2oOPbQJhg2Q9kfryhN1F5Yd1BjvOxWEonakGuxFfXMOtjIcczkpCYGLHOR5v6s_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-6.page?Expires=1654148363&Signature=V-zPYqlwCovA7uZLKK5K7jYuJbUJ381poYSMXeBtbYG7CChn6Pp46SjS-de9KiTOr8W5TWxMEp2LyoksrvnaZMIEFF6Gu~2yTC51Sv7NRarHGWRTeHi6tsY71XDCNN-kdb68Zf-VZfyxlj4i~qi4-uvGZvb5pj-3Fe5~l7YNzXw_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-7.page?Expires=1654148366&Signature=JYOvI9ujwWH9K68KW0fXFBXS54dGmQTNX3xsl0MKoi9~6E8Jft89WnKTE8551eMyojTqi2GA2munvsRyVLYDfT6hhGbmbN3wPUchfwqRL4jrrUkSR0Eqe16~d~c8DHAMihYRnEhrF5t6pNvY148rWwZTd5uB2UVx5FDNFes1YME_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-8.page?Expires=1654148369&Signature=lcSQIggziTlmVVBBUvYDUl06HIz9vsCYmBw1TRzu8YGomEDk66u4WXXG4XBVvwv2RmOdDqZmqN8xZ~J8s8L1NjWQJNI8TwFlA-GGiIwvEPLkSvf5UxCHG9mEuFslXKErB4hkgfMvTw~Ap3cZhpM1cW4OfAFQ6X3sEdcVbeQpge4_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-9.page?Expires=1654148372&Signature=QuTxFRKYh0Rc0oRJzBqBoY8aRbe0aBQqvRvWMKzu8Zw5JgcmoPK0yBXXtvGNxw3ePGbiBXhthb4-PXE5OJHGPNfCMOwgRLqxifc-~zyrOE8WWGwBMxBbgPkzwtxmExusFKdHzbZ8LXqVNa8l0td9rEXekSvPP~6WoHi6mQ~TfGc_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-10.page?Expires=1654148375&Signature=aT-v3N6-N8Z81Pm7boc8MYrEvsUk5-y3Q7-XrBNOzj0eSEvb86tEHq6raGckprnMvrIFRuZysS4JPu~ToQXkCe46W2F7wrj2uZwLj8THPstXPz7XSVYZsTQh6D1hw3wwJnVC2DHlIrNJApABDKkdnzr9pvQOis01ZnutMDhn6N8_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-11.page?Expires=1654148378&Signature=Ytrllgx6yQFvnGS-4Z1RFRoPFATJYL6lXU9RBEldN22THtet9x18MiTa5~bFmyC77xOZdV5VtffZ7dKPKYpsE84H22yQtaKxu9Zlec1~7RgiuJ3B~lU8PRM~tX3F213eX6peLcB~fJfM1xWfe27-rax0DoKRh8NwG1p5JnrRfOU_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-12.page?Expires=1654148381&Signature=Ivv53-9WN4xaqRx0Ckbyd~99-SKPKyP~vRRVgBLa2rmOsupgiETzZWk8MVICs3LNNTWNOr9TYM1z-Z2jWC5YmgtKlHZJkkuxaW~xUKsrtWAsFEi8ZXzcAKNMRbFYc3BvAlNyMs8hOzWC1M1XUrg~zq-387dLEnnAuXbTvDeRnOg_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-13.page?Expires=1654148384&Signature=htLa5Ro30oWipRhbNFlWFDKCYEj7HEK7HGjZQ0JD5wyDB8nR-155KV8hSDdZC89Bwqmt6eGVSOn8WfoPY5gwXSFZ6m8UfZNFVFj9Qatti6PE0fEMWvlAxGDyRWddLOhj4luxPsQyRvBmV05mapfoOcWNRMr4FQ3S3LqGWpzhW98_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-14.page?Expires=1654148387&Signature=c7oOGuL71HE7zvx1-7-hHceZYlkBMtTIXMxdD3sGetQaen0NRG5~fnJrm5l1uB60PSG33M06dFFeWVtz3A6~ZQpK~CRVhselHrbuXNccIos1FeC9M3g2OMAOhd7aGvfktiVzbgu3pd0CW6UXL7IsBPQw5cZW5SkLKn2CXLE2KiE_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-15.page?Expires=1654148390&Signature=jScZ8ECDBdTuISmE~JGXBAI1Dhi017hgFB6EoBrPRrmHqymby~cXJQV3-9mGIWvAENATu5-jB-L0x84Wxc4ZFUVSS2VsjqsRgPOEbb5gVJ1NuZfG6nOau0rrqYM-G6lUd6P~tVgBnOTqbX3C6FPzYiFKnuv5ovndJ3jggUD0k6g_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-16.page?Expires=1654148393&Signature=eQIX-8iPo29bbYdVx-dTHeRfTHENfFrY6EhXBhon5P1Y2ruiB6kVWwqs80VoC0uMQbIk-yQrxrhzvsDLGqG58Fla5TGbyxH-4nTrmEKnRcKZzuq4GPjzLq7lrHdkp0t9sTyLVPFSiSEg~jG7LMfx0eA64ECtzN9FmO8eQOfWa6g_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-17.page?Expires=1654148397&Signature=E26YsZGGXYKkmApuxs1MseaLII-EvVU3Ya7B9fTshm8VLjoJcEsELFKYA0QkLpoerr2PT9EsSaydfigTaAa1JTTDjtx-qts2qRcWMH-nwrMJGBO~cF0f7QqvokoLO6SUSaKajqXzCDPWXORLlzA-osKx5mS3kea5mBve75yzmBI_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-18.page?Expires=1654148400&Signature=N1cN-Hk53avvqvpi09NMiNBSMLv5Sp1sL6v84v8ZXiYq9c587cJdebl5LEadJjrTuPaQO2AaZbdgetKh8t8SaAkplsofQoS21H7h1tSKBCQ3QS8G-UUBdSPF7oLb6EDSqSeYionLZO50iXWzKGw~XQseI6q-g5QNjtOLSVMOup0_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-19.page?Expires=1654148403&Signature=dqED2V2mBvh8pELHN38SPa2nb4tuqdYmPLaRrgy2IyHN29P6RvgYH-w~g~aYZvDoPKTxTDRgt6XvHy6vuJKvReZPStktrms1Tj3WvShRGInFRnS9-L4MyL0Dcm9iqEQYEmHLhxvPDCd7ixW~6m~XRdFOdWkvleCkqrvlyVuG9jQ_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-20.page?Expires=1654148406&Signature=B6vW8xM8MWIcsmCA1JEvj79Rw5Rjf1~DPfNBk2rz4coWztDcJelDs0TsPoMalFEdDgB1C~j1LuE8i0Lb4yLYhv2wsZjvQh3zg09LLJ6uqVtoLHNiORIUGZvuLtN3XfUFGV1OrGojgJ65pdXhsB5uZEHvgfdXpKK~8xzym8W-tYE_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-21.page?Expires=1654148409&Signature=YfY59j9-0LfT5ScsbBKe1B8wU8OSDetZvEFqZcPzRuWhzdVd6I1T-Ly8BiZEUmcNGbNaSp5JhgBWcQCvQx7Z1v6f6tlw4E849E4ZnRVexTFHkI1sgifstYNYivRjzsxSb1If22DbQFccWZQtCZQ~MOfyq44hITk5hyi1q9kUPxg_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-22.page?Expires=1654148412&Signature=Sp1b7EkwSVtIWikBNeTud5~QQf~1vo-jdAWdICTn9Zwv-wo9aOO0B02dPomvdR8gMFOZ88TrRBoa6VMaiZIgEoNMfkiNS6y0uXDBEnbj7~2XK2fGEnFK27Kbvpp6tj8FeuCzOjwtrTw3yo0t-6jHZ~UC58F4uskPxMGy3y1cVQc_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-23.page?Expires=1654148415&Signature=Wwh4c-GeszkwEwkZPsFEsExmxj2DT6ZGIOPznr6JNHSlXrItlgoKM~jsCFkjnFfjAKY7Eb8Ejn3W9fWAXtlF09HW1WmJedQDTamwYMiV~fmRG0I4nNp1SZrCGyaxNq6l87webs8zrKdi86QCMRkOKvWZNPIGU-w~VlM5d1Pi790_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-24.page?Expires=1654148418&Signature=ee8Be-w~MO~Bn30YqJQraJu4grIFEV0QtsFJm9l3k~-Jz4nn4Lj9skOKN3FHl8zMEYqfJNqE7BYEv3aHFKl5207qtXzB6J0RtiazZScVv0fSy2MnkpsvwT0eRN45jvq9X~XPKv5oznTuid-Nl-Q36lCQYfdmms0~hFh9C9lkb5U_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-25.page?Expires=1654148421&Signature=N6X-UzdDXfFiBMVqMwpnQW6hpqlIHyqCvhNELCm9AknXEccld2Rmm7rgbIE4ui67HUOanDGGWOKoKaQQmFXieW2wnMpLGfR~YtW4GDXELuoJ6BsSn8TNOoWrHi9MEAkpzQhhHgaHIMmBFqQD5DEajQ71dielHLEQnjOOp~RAjb8_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-26.page?Expires=1654148424&Signature=mADJvyZG7up5F6OeG5Xf6vxnQJlBLXYECf3IIzBPoO~gUjxUhFs0UDhu4YElgtsTkawMfUoN2FTeQzOZVSdrfuMFwxU-JSukJp6fSdD92hfTwCxXGzgkrjJWgt-OLvhsZDV-QfiVcgc~HVbSrUodT4dFOSfTCrrTm0kx0jiNimI_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-27.page?Expires=1654148427&Signature=RS3fRXmWb3S~LWBnjyu6dsI~dEhJsxlpNybzBNn0UppWcWBALcYWD-OVq1gOvAsDSRSTVz0m6EfRgwKPyJ1s0uKTxczu5U5SW7hoM3W6P3CFd5JHiwGl8GEJeMcHV7X4S-tdmKY4yd8O-ajbpRNvWPq-rxSE9gbHFedFfW-~nNw_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-28.page?Expires=1654148430&Signature=AFDk9N3ouj~Ex-XXeDlu8dNKGYxrRuP6XNnbrYBhi6cpVQFLXSo8Pzr8UHSMnSOWlZx3vyl7TvqKq1SKxv7W9vJIZrxGYYWXpzXWF9vmMDAxO4a0BanzsoJ9Cjr1KdgQYbu~kJmYRrrTGVUQggWEg3cGJiVt0J9Vlh8eNMXRhnA_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-29.page?Expires=1654148433&Signature=US3dwdq3EvrVS3WXekuZgzejxbKB720PlOoHL7lNFRQfA8XZb4sDEe1JjNXkM8wLxsW4xDqnju31E~~PmJZglAZnpA1iriqnYWB-qeKfV8P75QthX6B94JN2mwQbnMHJHNsVsI~JKpCo-gsp~xLxVy-yw4OoezNPSPiX7uAK5UU_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-30.page?Expires=1654148436&Signature=NvYD3Pi7Ma7R05WU6DlLKn0aZ-DmK1O40ktadLKBYy8KmQq7~IerN4Zpb704AKq4WFQuaVGKoFYssbpYj5V8kprU~A2F-PXI2RgQ0tZI-hEb~G40DLF6l0NwBC6uqkEec6co4BD7liOyPLo8hyAq2vP1f5g80eRG-3m2VaNtURk_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-31.page?Expires=1654148439&Signature=Tr5Rmuv0HoQzPQCQp8Ru6E2cEPLS8rvhqUnUvLf8TTZCjlj7GVzl9SbNqxEvCgWw76pEIVZmF-rhFyPB-XWixJnIEfk35Id6Rdm7O4ZMtdKnjNWA~tqW1aArj82So2zCBzv0g0S4U57u-hk2fV5aBdX1Ydf9D29W~i4P7c1~bUE_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-32.page?Expires=1654148443&Signature=CNM36uAontvHGuD8x-RscLqf~e4J~HfkbwoGG1~5q7RAIYlgLG6KxJnLCi4UzoUFwJxUCnaX9vvdgR59-1ZO9vzyvZLJ3pEm0bf2a9lkN3fvUaUkFLARfxZR7OwJQcIQ2c-0-FyOuaC~ioUuxEfdCcJylVjKQvo14rINmRcnzlk_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-33.page?Expires=1654148446&Signature=ATLawCc8n~oSfuPgt3BsUqNNrU2Cb6RAiX~saVAUJRE8rFVbezR7nicyPAGM9B6rle4h0DDvdQd-hLqnY8Nuc6iq2VKZrADADLHLmIM427LlLqW2dz9ykYhUkD2SqRw8M0W67pz-de31GDnOI0Cl7TBNRRirB5aIOSyMe1Xn9vA_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-34.page?Expires=1654148449&Signature=FBa9qe33DsguDZngCVd0MYc10npKMkjOCpacZmZuZZVISvmID8-iwuhzpjXFgY1ZpgPPP4cVTIRQVp0vySDykV1ucgpAjj7rN22n1gPmsEeo1ksxxwq0FLtLduowQEW3d~KSZhGIcLdtB-gTR041Bxh4hGNowx1kC~dHxqowawg_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-35.page?Expires=1654148452&Signature=Lz5CEosXP4VkNe5ugVnaIXGKC70KDnsNeh93O3iRCu8ba2VGcTKa4YXRj5spgxkmleJrF1D-42scJQwAWeZyruTipMMfFnymZoKXT0zOOTo-Nh59xGMIdC8glMczWVjqE3eBvGjB-spb2G5HuAYBclubZMTx~8wTUmHvKz5OvvU_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-36.page?Expires=1654148455&Signature=gbx-~uSyOlwHj13GxSdZ8HGxTEVAMLcUkIByBlO64EHVWhmz1uH8L69ZWacLCZ5ob7NkiYiNB3fQn86uftua8vb8WJBtdL3yNvSB1R6lgwJtN4kg3HlWmv1sVd1jHVfRlSvBHzKWtM7FER3N4m-vcf3mvUeBD~NEAAvSa1TOvnc_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-37.page?Expires=1654148458&Signature=kb-lAcNj0WXzSoKKxw3jikut3AiaSEQbPMpOcjy-cMs7-Z419-e2infpYE109y8GeAdSY6eXDmNOgwJtMhy3CK5m9Nw0rK6MeGLBG-w1bZj2B4iq5eXNoIxo7Uyv4jjejJmJdFZ5a1-zF30YnAsyU0GoX5~w75XYq4WQ0rfjmRk_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-38.page?Expires=1654148461&Signature=oQfTnKVSoMgSb34LLmMSzXHAQmfySY4ctZANvy22pnwlkCoI-6EGG6kbkHLHn2IS0g5tqJuZWSRvqgxGJCsjY5jHVB2X5VUfXvX8lx0bsru1bSbiiFZJcMX8hmgyRR6dzeCS1foe26eglr3rrj9y5YLTtgk1lUTF2lKjmBOfoKg_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-39.page?Expires=1654148464&Signature=mrFw-4faHVUKFSVyez778Vm0XLdMHLgQ~yOv7dVBz1dKbu6o2SLb0awp00xjeYytfcw30~z-jrl1qwtD9xlor6pT5tQb~MBsWNDyz3K4kXAxqe29oIDatOT3FmCZUWS-N3pgqO02350MSTcVDN~ES5IM-z~8R00naTh8ZFJI6Co_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-40.page?Expires=1654148467&Signature=hNnghAjTvHA9kXGXG7u3YAqKLKp7p9fZmc~ohzCgGteC8tCcaRwZy3w4XfK39cUSndX4FBo51TL-BT-ub-IYCFgYAo6JKUIZUFiPG6wS7cs6bdv5gD3PZWCbE4zJViFnbQBTszG2YmBzo0zewLoZMGNkTNDJraUoeV3SIRt8qjo_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-41.page?Expires=1654148470&Signature=QKrTbf6bvcDaEh3Qh30T5SBM0QISitAsMS8dBScIGm7a3VUb0s0KjUT8VCsmvmpfNyfoy9Ye3vNiOLjnTxh7aoQda~PNDqTvXfHSYkOvKygkiW4ljay4kldBTvHCYMSt4iKauqej9R5dT6X49NEEgbnbcSzuEeg-CWw4dBgKnIU_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-42.page?Expires=1654148473&Signature=pJY9fe0YqiBjGVrNpIMDhGoYVjFqGtXjCEmFMLzlC8mjCLjYD6Iyu6rGXmBzo9C0XBvbp4pZkXYB0KhkHmyxAvlXTvvZGxKR~S0178yhhYmOA8omRwYL2AvOyCX5jn5HkkmX~IuSuIMv8CU9mWDosTKSub04aidL26R0o6H4qzM_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-43.page?Expires=1654148477&Signature=P5GJeRb3We8YEzt9-hNF1F-XTeiVK-QAU0couog78N5TvPejREntZuJbHS8UcXMdCoRiC5WdznOZO7ZV3ktCkeb0djyB4wobIo5hQYIRTE9z3HCAbOK5gWZYMkVt6hlecuLgQ3WcRZ5nhLB5HLBzQTm5UZxVuNCBZpkhkXY4uTs_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-44.page?Expires=1654148480&Signature=WODtdaxq736FV0gnL1b2stXLZp8P2DA9619w1fiQiKrSy7vrM2519~zxotNBknVvc1umOxwC7F~Ur70JhfLZ8AY1mEh6cfRcO-~KBb5zyCtf4mENwWTF7Njk3g7vpd8s1LbVyI3q1wIM2z6lNZn-14694KwPfoKGnbD~7OgTppw_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-45.page?Expires=1654148483&Signature=Krm4aUzbC-VPiX5d4k25iFtAKfvB-G~DBgygWebLNVeeimUa50iZ1ruLN4pk6LIEjxmO~IJbLioi77AjqhsbIH1P4K5vn5AHXnOTVERaRSews06gAVTt35I4fBh5K7sSI4eNp4lVQRisEgd3NzLK~jT8UuYlR-e0KVrWG~1sZIY_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-46.page?Expires=1654148486&Signature=TZXrSouoEFHVUgEbj-tWM4HwKCwlJpGeDd7YlELSZB3NIQSWMM8wRLFWQ-XJQQpR2AFUXtQEma9EXzL7rFkSQCePnO1qRV3bkloevOf-oh-b6rsxyhIouIzrb7zzpheeibJBGneCiTMAdaVcda3ZFLS7UX3J-bMIkVh3QSkDXJU_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-47.page?Expires=1654148489&Signature=ibD2DU8ipy56TruRPprjb627mgSxkADvgvZmuj9mYiNrKb6m7mqOAuXt3uHFWmictL~t33i5tFrUFgzIKn3Z0v4-ANI~XBEZhLi7cKE8hm-FUlL9ov4~03scf7TSeb-moICEpv50kv0I~SM-h9ugLPBOq01TUNV2FQUcjRh6L9s_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-48.page?Expires=1654148492&Signature=WnqTIflWTcZt2oPQTW1PhtQYXzx2F~zrgppI8mCvf8TM9wajQvy-5LRy9Yq40suVQuZT6DTc68bEDpcJz~IujaCPphwsJJeWpvebt9gwGIfO4xFNYlLxJSCAahQQfBZud2mVLaKsm49DmstGGxsyC45XqMAnzemPnwYtgGiRoug_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-49.page?Expires=1654148495&Signature=Dvu8Og3HjWCUiRnUFjUqQTIM-AtyEEcB3hI-jdfTcpMDps~P8QPWwSKOU4lset2YGGF2oGIOpuedYbJXEKOP5Ysd0M4QboAgvms0APYlD7GKF2AZ7WzBfnNb9Ub2LXSoH0GBsseso68LzHbTFlC5-hERYMkDDEs18xOELlO6nKw_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-50.page?Expires=1654148498&Signature=lOG-VwOHtNhNRWoGgrjz74QKRrtjZwdBQvjE2eI~2yDQsHFqYP5q2kYJCujzYmqbX4fFCX8nzP0ovrvEnA3RiFgkD-1h8G4LQM5kWikhwPB8BwCXX7PIvLLLIi-ROy7ntc31Q7IcNK1Io5pXtlMIlp~O8khsMOkqnp7y6CUUnZ4_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-51.page?Expires=1654148501&Signature=UbmkUO5ywzFgnplHHwPzYVAnwm1rDvoBrQCjMNq~86-zC6bLJSHXi6GorWkSj9rjmaiWota7~Aj4XJWvNKHOskzGPNvcx3WZ4pO~bl19qdmUZR3QH8VhFJUFvvvs0tTqvrkFNyRyoHyhlciBPxpzUYPVSzejqpZm4EBG2qxZyPM_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-52.page?Expires=1654148504&Signature=S3QyCg02TnK2jtRkOlzRseGtN25aj7GpVq5p-SJi390vZgktyBpd9UtjSLNtN6rfbBsx~FW794CWHitmB6PEW9ktJdNPqO0x3b5VqweghricJsI2ES2rgsTHtNUOXksDPGTp1XTGvVMUSUKZblxQMRl4Qs3T5v-v3HRpJNqCQwk_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-53.page?Expires=1654148507&Signature=YGawQ9jsbQWxlYv5G6lsA3PBM7I4fQKHZL28rIawL2Ey7c6G2i6cbMM-dSqPH4MOEy~UUk-rqvHLI3M7qDG0uUKcHuz5AG8--CwH0EjoEQnWHtS5oO2JqzKlLUlT5lJr7gpuIiiYeoAJ~XxyvObvrJEReBOtBQzgDiC68vZRCQE_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-54.page?Expires=1654148510&Signature=np8QwKBliwzcMzkW4V-3BI-XZx0HE0QJe7JZLkiUSGa4YffnB7fVVE~LXptNauE7JXcFP-0~NUnZdKZFVZKBimM4QFlsslOjqFIVVC8nkec7HCEzolWuQCa49rHUXFKYVmn-gWB8jxNhbWuNJoPMLWExNQvZ-xRimAzrmBbbX1s_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-55.page?Expires=1654148514&Signature=QeIUpTZL-jPMaltRwWmN1b3JS-4iV8no2Iy4KCHEyGiTyFby46P~t8JWKF8lfgjVUHPRC65BnypFOONBE~ws9EpS3-azgAzLCaEBfNI67XHZp1iYHHVFg09P8y6raG~I0kBNywyZfBpz6DFsq3-QAQtQvQMjIPAaq2fcdriTaZA_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-56.page?Expires=1654148517&Signature=h-PfJVm2-UalbRvBByca8blnDKxXwwCL-mgcWtcdS9IpaGCesUuTNTNkagoX4pAtZHtFuSE~7b8fhQ3pI8E3t9oAYXDSo8z7I1H1O00IdbBUjNiO6-23ly0-9wWaeRDvoQlKWvx2EUHDFoqODpbtzceWbb7D5w6dvgURIllumAA_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-57.page?Expires=1654148520&Signature=odN58di6aR~lriNmpKt-n7HiiRVEKXsIGuGy05K1gbOXZzqVeHdPgxT8ZWkVXDD2iqLEpxRtyiQy3XWpCOGaa0jKur5l0MeG8fjGUFbd8cvUoyaobm686QMyvodU4mH1Mkx5XyGgVFfwhIBqNKdEOWQkKGX-voYZcmtFn0FSvTQ_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-58.page?Expires=1654148523&Signature=fEHb3B415y41a7RUp1eoE6A6GYHZbMV~E2ZJEVsPkhiloj5yti2vU~mpaHWUIEdJd08Qj1Kyt-iHW8zciPcAqjiofYxQUvEF8zTgnVJySJyN3Pcm4whzVJmGtRqkS6V-WOyMhynozSS6LkF5wovT4OzqVejmPTBoSIsurW-2Gx4_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-59.page?Expires=1654148526&Signature=fdummOpAWZrwWbTmINRLPfg~Un0iZTG45EntrJnhu2TisvihuJxdBugE6W~0DZuofrE9ij-D6aQAiy93lRcfAy38jgb1WnO93ztyS3dMhz6zSXrhcYkWcy3jt5aT6uQR9ZJiq~3Dc4DdEWH56WPLwbBh~LdPcIUs4grLVPlhvks_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"
,"https://videos.online.digitalpace.in/697509/page_1638453319-60.page?Expires=1654148529&Signature=PvkbUFtSrKao6~GeJtD21okrJr-px0~TV0dvV-FvAv8f5hlKKT1POX-jnpqhmvcPGeomLuaVPM0XudivNLnKE2qUOypInvr6ckthLuYRv-3frk9MnCZoxTwCBlqfBrpTQn~bUPaAAVOEkilYdfe5~fIcSZQkNqmnbN~Njy7QMRg_&Key-Pair-Id=APKAID56YXJX6U7XGA5A"]



download_pdf(arr, 'qualitative analysis')
# save_pdf('goc', 91)