from pydantic import BaseModel


class CreateAttendance(BaseModel):
    client_id: int

