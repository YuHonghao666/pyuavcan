#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

from .. import _media, _frame


class SocketCAN(_media.Media):
    def __init__(self, mtu=_media.Media.MAX_MTU):
        mtu = int(mtu)
        if not (self.MIN_MTU <= mtu <= self.MAX_MTU):
            raise ValueError(f'Invalid MTU: {self.MIN_MTU} <= {mtu} <= {self.MAX_MTU}')

        self._mtu = mtu
        super(SocketCAN, self).__init__()

    @property
    def mtu(self) -> int:
        return self._mtu

    async def send(self, frame: _frame.Frame) -> None:
        raise NotImplementedError

    async def receive(self, monotonic_deadline: float) -> _frame.ReceivedFrame:
        raise NotImplementedError

    async def close(self) -> None:
        raise NotImplementedError
