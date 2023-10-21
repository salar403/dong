from celery import shared_task
from django.core.cache import caches
from backend.customs.queryset import get_object_or_none
from backend.environments import NODE_IP

from dong.models import Node, RoutineTiming

cache = caches["routine_timing"]


def set_routine_time(routine_name: str, elapsed_time: float):
    routine_regexed_name = f"TroutineT_{routine_name}"
    in_cache_routine = cache.get(routine_regexed_name)
    if in_cache_routine:
        new_count = in_cache_routine[1] + 1
        new_avg_time = in_cache_routine[0] + elapsed_time
    else:
        new_count = 1
        new_avg_time = elapsed_time
    cache.set(routine_regexed_name, [new_avg_time, new_count])


@shared_task
def save_routine_times():
    node = get_object_or_none(Node, ip=NODE_IP)
    data = {}
    routines = cache.keys("TroutineT_*")
    for routine in routines:
        info = cache.get(routine)
        avg_time = str(round(info[0] / info[1], 4))
        data[routine.replace("TroutineT_", "")] = avg_time
        cache.delete(routine)
    RoutineTiming.objects.create(node=node, data=data)
