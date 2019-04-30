'''
1. 파이썬 프로젝트 만들기
2. 장고 설치 : pip install django
3. 장고 프로젝트 만들기 : django-admin startproject config .
4. DB 초기화 : python manage.py migrate
5. 관리자 계정 생성 : python manage.py createsuperuser
6. 기본 앱 만들기 : python manage.py startapp bookmark
7. INSTALLED_APPS 에 추가 : bookmark (템플릿 폴더 검색, DB 변경사항 추적 가능)

---
앱
(custom field)
1. models.py 작성
    - 필드 => DB에 컬럼 -> 컬럼의 데이터 타입, 제약조건
    forms.py 작성
2. views.py 작성
    context_processor 작성
    custom template tag
3. urls.py 작성
4. template 만들기
'''
#_--------------------------------------------------------------------------
'''
SEO - Search Engine Optimization

HTML 표준에 맞춰
Meta Tag => 무슨 검색을 해도 내용이 다르지만 검색되게 하는 기능?
Open Graph
위 항목 3가지는 프론트 엔드에서 하는 일
'''

# ------------------------------------------

'''
localhost/bookmark/1 : 글보기, 수정, 삭제
localhost/bookmark/create : 글쓰기

'bookmark/<int:value>/'
int : 정수
str : 문자(default
uuid : application 호출
slug : why-so-serius => seo때문에 많이 사용
path : 'bookmark/<path:value>/' => bookmark/19/04/29/
위의 기본 converter를 제외한 형태가 필요하다면  custom converter를 만든다.
'''

'''
추가, 수정, 삭제의 경우 해당 기능을 완료한 후에 
이동할 페이지가 필요하다.
1. success_url 이라는 속성값을 지정
2. model 에 get_absolute_url 이라는 메서드를 만든다.
'''

'''
배포 Deploy : 서버에 올린다.
    Pythonanywhere /w Github
        github에 소스코드 업로드, requirements도 같이
        pythonanywhere.com에 가입
    Heroku
    AWS Linux FTP
    AWS EB
    Docker
'''