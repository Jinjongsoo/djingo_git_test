
from django.db import models

# Create your models here.
# 모델의 형태 - 클래스

# models.Model을 상속받는 이유
# 상속 : 어떤 클래스가 부모 클래스를 상속 받는다.
# ---> 부모

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField()
    contents = models.TextField(blank=True)
    # 작성자 -> 로그인한 유저 정보를 찾아서 추가
        # 작성자 != 로그인한 유저다(장고에서 알수없음)
            # 모델 저장 직전에 직접 코드로 처리
    # 작성일 -> 서버 시간을 읽어서 timestamp 값을 만들어 추가
        # 자동 옵션 auto_now, auto_now_add
    created = models.DateTimeField(auto_now_add=True)# 갱신 할때마다 업데이트됨

    # DB에 적용 : makemigrations, migrate
    # python manage.py makemigrations bookmark
    # python manage.py migrate bookmark 0001

    # 관리자 페이지 목록에 표시될 내용
    # 확인 메세지에 출력되는 내용을 만들기 위해

    def __str__(self):
        return "Site name : "+self.site_name+", URL : "+self.url

    # 메타 클래스는 옵션 클래스
    class Meta:
        # 정렬 : 필드 이름 -> 필드값 오름차순, -필드이름 -> 필드값 내림차순
        ordering = ["site_name"]

    # 모델 클래스가 수정됬다고 해서 항상 migrate 해야 하는 것은 아니다.
    # DB에 변경 사항이 반영되야할 항목들만 migrate를 한다.

