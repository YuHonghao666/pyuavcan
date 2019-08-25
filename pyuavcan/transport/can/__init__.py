#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

"""
This module implements the CAN transport for UAVCAN: both CAN 2.0 and CAN FD.
UAVCAN does not distinguish between the two aside from the MTU difference; neither does this implementation.
CAN 2.0 is essentially treated as CAN FD with MTU of 8 bytes.

Virtual CAN bus interfaces
++++++++++++++++++++++++++

Some of the media sub-layer implementations support virtual CAN bus interfaces.
Those are useful for testing.
Please read their documentation for background.

Inheritance diagram
+++++++++++++++++++

.. inheritance-diagram:: pyuavcan.transport.can._session._input pyuavcan.transport.can._session._output
   :parts: 1
"""

# Please keep the elements well-ordered because the order is reflected in the docs.
# Core components first.
from ._can import CANTransport as CANTransport

from ._session import CANInputSession as CANInputSession
from ._session import CANOutputSession as CANOutputSession

# Statistics.
from ._can import CANTransportStatistics as CANTransportStatistics

from ._session import CANInputSessionStatistics as CANInputSessionStatistics
from ._session import TransferReassemblyErrorID as TransferReassemblyErrorID

# Media sub-layer.
from . import media as media