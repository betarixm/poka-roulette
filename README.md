# poka-roulette
2020 사이버이공계학생교류전 (aka 포카전)의 이벤트 페이지로 사용된 룰렛입니다.

# How to Use
1. [`app/utils/mail.py`](app/utils/mail.py)에 메일을 발송할 계정의 정보를 기입해주세요. 또는, [HEMOS](https://hemos.postech.ac.kr)에서 무인증 메일 발송을 신청하면 됩니다.
2. `docker-compose up`

# Notice
이 프로젝트는 django 컨테이너와 nginx 컨테이너로 구성되어 있으며, django는 gunicorn을 통해 배포되고, 이것을 nginx가 static 파일들과 함께 묶어서 배포합니다.
기본 노출 포트는 1337이며, 수정이 필요할 경우 [`docker-compose.yml`](docker-compose.yml)에서 `nginx`의 포트를 수정해주면 됩니다.
기본적으로 `get_random_secret_key()`를 이용하여 시크릿 키를 발급받지만, 적절한 고정 시크릿 키를 삽입하는 것을 추천드립니다.
