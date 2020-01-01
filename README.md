

# ZatoBot

## Cài đặt Redis và Zato theo hướng dẫn
  - [Zato](https://zato.io/docs/admin/guide/install/py3/ubuntu.html)
  - [Redis](https://redis.io/)
  - Upload các service trong thư mục `/zato-service`
## Cài thư viện (Python>=3):
`pip3 install rasa`

`pip install rasa[spacy]`

`python -m spacy download en_core_web_md`

`python -m spacy link en_core_web_md en`

## Tích hợp Bot với slack
http://api.slack.com/

gán token vào slack_token trong `credentials.yml`
![slack](https://scontent.fhan2-1.fna.fbcdn.net/v/t1.15752-9/81623467_2589680334586246_7658323569515954176_n.png?_nc_cat=101&_nc_ohc=VVBatWQ3YqcAQlBTnjoXBmH5gCkZNsd6z-r6FhSbc_DojYe00ClzLrF-w&_nc_ht=scontent.fhan2-1.fna&oh=6f6d1584a4c2d22d5e35cb8d62f833f8&oe=5E9C1055)

Cài đặt và sử dụng [ngork](https://ngrok.com/) làm public domain với câu lệnh:
`ngrok http 5005`

Khai báo domain trong Event Subcriptions với đường dẫn https://ngork-domain/webhooks/slack/webhook
  
![slack2](https://scontent.fhan2-2.fna.fbcdn.net/v/t1.15752-9/81329187_602320470519942_5316245853961191424_n.png?_nc_cat=111&_nc_ohc=lZVjl7E9NhoAQlsXZFjyiy5NKsKBTSh3TgELQre4Z8B6WM_OjH5mniswQ&_nc_ht=scontent.fhan2-2.fna&oh=956068c6d045b5f8111529eec4f8cda5&oe=5E9873F7)

## chạy chương trình
Terminal 1 chạy bot ở cổng 5005 với câu lệnh:  `rasa run`
Terminal 1 chạy bot actions ở cổng 5055 với câu lệnh:  `rasa run actions`
