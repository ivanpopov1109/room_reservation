from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, between, or_, select


class CRUDReseration(CRUDBase):
    # свободен ли запрошенный интервал времени; если это время полностью или частично зарезервировано в каких-то объектах бронирования
    async def get_reservations_at_the_same_time(self, *,
                                                from_reserve: datetime,
                                                to_reserve: datetime,
                                                meetingroom_id: int,
                                                reservation_id: int = None,
                                                session: AsyncSession) -> list[Reservation]:

        select_stmt = select(Reservation).where(Reservation.meetingroom_id == meetingroom_id,
                                                and_(from_reserve <= Reservation.to_reserve,
                                                     to_reserve >= Reservation.from_reserve))
        if reservation_id is not None:
            select_stmt = select_stmt.where(Reservation.id != reservation_id)
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    async  def get_future_reservations_for_room(self, room_id: int, session: AsyncSession):
        reservations = await session.execute(select(Reservation).
                                                      where(Reservation.meetingroom_id == room_id,
                                                            Reservation.to_reserve > datetime.now()))
        reservations = reservations.scalars().all()
        print(type(reservations))
        return reservations

reservation_crud = CRUDReseration(Reservation)
