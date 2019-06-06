import requests

def run():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Cookie": "st_si=72747346219909; qgqp_b_id=96405d9f780665ad03d6328aed2f2b57; p_origin=https%3A%2F%2Fpassport2.eastmoney.com; ct=r-R8ChPJZmqF1WY8IFIigHY1y0Ii6aG7t81fUpRbYPTI7p4ST3qEeEZ-5zm7RkU8tctDvFuEguPZAuCwsxL-krS3IrmuOXf-Nf0ErcV9dPJv-iMKqrjXSH1aVQyULlHS12K008QorQQJjzf_8F-e7lYE8vhB2RZxeejVQMSYst4; ut=FobyicMgeV60R-wNFHdtrN17mhW5wDy4v9r6x1eY-wyk7BD3Q4qOgM5u27e--2Vz5DlQpGggkVwBNjS7W_QRxA8pE2WRgcRlN8g8sWEUcydlBcAo-fAhe6GdYEiUKU5cXaxmXK2-PdtHHbpdN-C_8naI7oopKJ4voq_MnOn5BPphm0WcCMVCF-4fhE-_81Q8Mh3kZQMaelEYkTD4K_gMOSoLu3VHmAkOFttp7mo6B7n9rcivNTTCVmOPZlumS1nO06LZC4rOFN3ARQ0pk-8czrDSXaInGiWE; pi=3564345589542852%3bm3564345589542852%3breboot1%3bUfUUbcfW0RZ6JgBqknIa7iXB6V0cK%2f7MSaPoGYn%2fcbebGw3tNd47%2fCmy6Hwq8U0KzZp50dXVCdGF82VMh8b7%2ffMqfvhlF3Hx8EZt18CiRG2A%2fvELeik%2bQm0iSvIueM2EGrpUoQKEq1paU%2bSwiXvijY5Ypucm0N02TahJFsmXSkmYV0nGFhhv4LxPvb2n5v3jwX6AR0v4%3b5BztCv8%2b5Rte5R%2fTSvHFFFYy2ifsGzgiw127Fx2bEKYxS5vnCEDeZJi4Cf6RUl%2fCEIytmrzw1DUuBNwPQUymUeDbS7I3oWW02QAfsKicZc%2bdHnL%2bMRehssQK2z67KBymOm%2fXXlLdAeygTa1Do%2f1YnEtPgssyZA%3d%3d; uidal=3564345589542852reboot1; sid=137744318; vtpst=|; st_asi=delete; st_pvi=06651445649880; st_sp=2019-06-06%2005%3A01%3A55; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=14; st_psi=20190606055018370-117005300001-8560595066",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }


    url_stock = "http://iguba.eastmoney.com/interf/stocklist.aspx"

    data = {
        "action":"gettastock",
        "type":"hs",
        "uid":"4162005331760506"
    }

    response1 = requests.post(url_stock, data=data, headers=headers)
    print(response1.text)


if __name__ == '__main__':
    run()