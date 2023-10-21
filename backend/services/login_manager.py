import base64, binascii, json, hmac, time
from hashlib import sha3_512

from adminstration.models import AdminSession


def calculate_signature(payload: str, key: str):
    return hmac.new(key.encode(), payload.encode(), sha3_512).hexdigest()


def login(admin: object):
    session = AdminSession.objects.create(admin=admin)
    login_data = {"session_id": session.id, "timevalid": session.valid_time}
    payload = base64.b64encode(json.dumps(login_data).encode()).decode()
    signature = calculate_signature(payload=payload, key=session.key)
    return f"{payload}.{signature}"


def validate_token(token: str):
    try:
        payload, signature = token.split(".")
        json_payload = base64.b64decode(payload).decode()
        login_data = json.loads(json_payload)
    except ValueError or binascii.Error or json.JSONDecodeError:
        return False
    session_id = login_data.get("session_id", None)
    if not session_id:
        return False
    timevalid = login_data.get("timevalid", None)
    current_time = int(time.time())
    if (
        not session_id
        or not isinstance(timevalid, int)
        or int(timevalid) < current_time
    ):
        return False
    session = AdminSession.objects.filter(
        is_active=True, id=session_id, valid_time__gte=current_time
    )
    if not session.exists():
        return False
    session = session.last()
    sign = calculate_signature(payload=payload, key=session.key)
    if sign != signature:
        return False
    return session
