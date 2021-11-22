# Django로 배우는 파이썬 웹 프로그래밍

## models.py
- DB 구조 결정
- 클래스의 이름이 테이블 이름, 클래스 속성이 컬럼이 됨

## admin.py
- 장고의 기본 관리자 페이지
  
## views.py
- 페이지 만드는 곳

## urls.py
- 어떤 url을 통해 view를 동작시킬 지 결정

## templates
- HTML이 들어있는 파일(템플릿 코드 포함)

## 디자인 패턴
- MVT : Model(DB), Template(화면-프론트), View(계산,처리-백엔드)

#

# 장고 프로젝트 만드는 순서  

1. 파이참 프로젝트 만들기

2. 장고 설치

3. 장고 프로젝트 만들기 
   
    ``` $ django-admin startproject config . ```

4. 설정하기(DB, S3) // 생략

5. DB 초기화

    ``` $ python manage.py migrate ```

6. 관리자 계정 만들기

    ``` $ python manage.py createsuperuser ```

7. 앱만들기

    ``` $ python manage.py startapp polls ```
    - polls는 앱이름

8. 모델 설계(DB))
    - models.py 설계
    - settings.py INSTALLED_APPS 추가

    ``` $ python manage.py makemigrations polls ``` 
    - polls(앱) DB 적용

    ``` $ python manage.py sqlmigrate polls 0001 ```
    - sql 구문 및 테이블 확인
  
    ``` $ python manage.py migrate polls 0001 ```
    - 실제 DB에 테이블 생성 및 초기화
  
9.  뷰 만들기(기능,계산)
    - views.py : 함수 추가
    - urls.py : urlpattern 추가
    - setting.py : TEMPLATES 'DIRS' templates 폴더 추가

10. 템플릿 만들기(화면에 표시될 내용, 양식)

11. URL 만들기

  -  대표적인 기능(화면) : CRUD → Create, Read, Update, Delete

12. 사이트 확인하기

    ``` $ python manage.py runserver ```

#

# 뷰 : 기능을 담당(페이지 단위)
- 화면이 나타나는 뷰, 화면이 없는 뷰(URL는 둘 다 있어야 함)
- 뷰 내용(함수, 클래스), URL이 있으면 동작
- 뷰의 코드 형식 : 함수형, 클래스형
- 함수형 : Request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수, 내가 원하는대로 동작들을 설계하고 만들고 싶을 때 사용(노가다성)
- 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아서 사용한다.
  - 장고의 제네릭 뷰를 많이 사용


