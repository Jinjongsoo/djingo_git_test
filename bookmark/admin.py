from django.contrib import admin

# Register your models here.

# 관리자 페이지에서 관리할 모델을 등록
# 관리자 페이지를 커스터마이징
# 옵션 클래스를 만들어서 추가
from .models import Bookmark

class BookmarkOptions(admin.ModelAdmin):
    list_display = ['id','site_name', 'url']
    # list_editable = ['site_name', 'url'] # 활성화 시 수정창에 안들어가도 바로 수정 가능하다
    # list_filter = ['url'] # 대부분 DateTime필드가 있을 경우 많이 사용
    search_fields = ['site_name', 'url'] # ForeignKey 필드같은 다른 테이블을 참조하는 항목은 사용하지 않는다.
    # raw_id_fields : 선택값 -> 입력값으로 바꾸는
    # 관리자 페이지에 커스텀 페이지 추가
    # 관리자 페이지에 action 추가

admin.site.register(Bookmark, BookmarkOptions)
