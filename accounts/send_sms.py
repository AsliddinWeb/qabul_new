import json
import requests

def send_sms(phone_number, code):
    url = "https://notify.eskiz.uz/api/message/sms/send/"

    payload = {'mobile_phone': str(phone_number)[1:],
               'message': f'Xalqaro Innovatsion Universiteti Qabul tizimiga kirish kodingiz: {code}',
               'from': '4546',
               'callback_url': 'http://qabul.xiu-edu.uz'
               }

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQwMjYsInJvbGUiOm51bGwsImRhdGEiOnsiaWQiOjQwMjYsIm5hbWUiOiJKdW1hbmF6YXJvdiBCYXhyYW0gTWVuZ3FvYmlsIG8nZydsaSIsImVtYWlsIjoianVtYW5hemFyb3YuYmFraHJhbUBtYWlsLnJ1Iiwicm9sZSI6bnVsbCwiYXBpX3Rva2VuIjpudWxsLCJzdGF0dXMiOiJhY3RpdmUiLCJzbXNfYXBpX2xvZ2luIjoiZXNraXoyIiwic21zX2FwaV9wYXNzd29yZCI6ImUkJGsheiIsInV6X3ByaWNlIjo1MCwidWNlbGxfcHJpY2UiOjExNSwidGVzdF91Y2VsbF9wcmljZSI6bnVsbCwiYmFsYW5jZSI6NDkwMCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOiIyMDIzLTA1LTE3VDEwOjI5OjE5LjAwMDAwMFoiLCJ1cGRhdGVkX2F0IjoiMjAyMy0wNS0xN1QxMDo1MzowMy4wMDAwMDBaIiwid2hpdGVsaXN0IjpudWxsfSwiaWF0IjoxNjg0MzIxMzYzLCJleHAiOjE2ODY5MTMzNjN9.YOLTsxGZieE5xQx8b_hcgjz89kpcd0_RrmrB9_zUgUo'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return {
        "json": json.loads(response.text),
        "status_code": response.status_code
    }

def send_sms_ariza_topshirilidi(phone_number, ariza_id):
    url = "https://notify.eskiz.uz/api/message/sms/send/"

    payload = {'mobile_phone': str(phone_number)[1:],
               'message': f"Hurmatli abituriyent. Xalqaro Innovatsion Universiteti qabul tizimiga yuborgan arizangiz muvaffaqqiyatli qabul qilindi!\n\n"
                          f"Arizangiz ID raqami: {ariza_id}",
               'from': '4546',
               'callback_url': 'http://qabul.xiu-edu.uz'
               }

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQwMjYsInJvbGUiOm51bGwsImRhdGEiOnsiaWQiOjQwMjYsIm5hbWUiOiJKdW1hbmF6YXJvdiBCYXhyYW0gTWVuZ3FvYmlsIG8nZydsaSIsImVtYWlsIjoianVtYW5hemFyb3YuYmFraHJhbUBtYWlsLnJ1Iiwicm9sZSI6bnVsbCwiYXBpX3Rva2VuIjpudWxsLCJzdGF0dXMiOiJhY3RpdmUiLCJzbXNfYXBpX2xvZ2luIjoiZXNraXoyIiwic21zX2FwaV9wYXNzd29yZCI6ImUkJGsheiIsInV6X3ByaWNlIjo1MCwidWNlbGxfcHJpY2UiOjExNSwidGVzdF91Y2VsbF9wcmljZSI6bnVsbCwiYmFsYW5jZSI6NDkwMCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOiIyMDIzLTA1LTE3VDEwOjI5OjE5LjAwMDAwMFoiLCJ1cGRhdGVkX2F0IjoiMjAyMy0wNS0xN1QxMDo1MzowMy4wMDAwMDBaIiwid2hpdGVsaXN0IjpudWxsfSwiaWF0IjoxNjg0MzIxMzYzLCJleHAiOjE2ODY5MTMzNjN9.YOLTsxGZieE5xQx8b_hcgjz89kpcd0_RrmrB9_zUgUo'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return {
        "json": json.loads(response.text),
        "status_code": response.status_code
    }