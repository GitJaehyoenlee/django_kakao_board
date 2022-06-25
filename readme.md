<img src='http://kakaocloudschool.rapa.or.kr/publish/images/img_top.png' />

# Kakao School - Django Board Project

-----
**Kakao - django board** 은 Kakao cloud School 에서 진행된 장고 학습 프로젝트 중에 1개로, 장고를 활용하여, 
게시판을 생성하는 프로젝트 입니다.  


## 사용 Tool List  

--------------
**Requirements.txt** 에 서술 되어 있으며, 운영 된 상세 버전을 아래와 같습니다.

* django = 4.0.5
* Pillow
* django-allauth
* 


## 주요 기능  

-----

 - 로그인
   - 기본 로그인 기능 
   - 카카오 소셜 로그인 기능
   - 이메일 인증
 

 - 글쓰기
   - 글 작성 / 수정 기능
   - 글 읽기 기능
   - 글 리스트 View 기능


## GIT 에 포함되지 않은 필요 사항 

---

### secret.json 파일

```sh
# secret.json 파일
{
  "SECRET_KEY": "[Django KEY]"
  "DB_ENGINE": "[DB ENGINE]",
  "DB_NAME": "[DB_NAME]",
  "DB_USER": "[DB_USER]",
  "DB_PASSWORD": "[DB_PASSWORD]",
  "DB_HOST": "[DB_HOST]",
  "DB_PORT": "[DB_PORT]"
}
```

```sql
# DataBase Creation Query
create database web_board;
```

## 개발시, 고려되지 않은 사항.

----
- 학습 용도로 개발된 코드 임으로, Web 공격에 대한 대비 코드는 없습니다.
- 





