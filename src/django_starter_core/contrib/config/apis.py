from typing import List, Dict

from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from .models import ConfigItem
from .schemas import ConfigItemOut

router = Router(tags=['djs-config'])

class OkListOut(Schema):
    detail: str
    data: List[ConfigItemOut]


class OkDictOut(Schema):
    detail: str
    data: Dict[str, str]


@router.get('/dict', response=OkDictOut, summary='获取配置字典')
def to_dict(request):
    data = {}
    for item in ConfigItem.objects.all():
        data[item.key] = item.value

    return {"detail": "ok", "data": data}


@router.get('/{item_id}', response=ConfigItemOut)
def get_item(request, item_id: int):
    item = get_object_or_404(ConfigItem, id=item_id)
    return item


@router.get('/', response=OkListOut)
def get_list(request):
    qs = ConfigItem.objects.all()
    return {"detail": "ok", "data": qs}
