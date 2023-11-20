from dataclasses import dataclass, make_dataclass, asdict
from typing import Tuple


@dataclass
class BusinessInfo:
    """
    location: (longitude, latitude); e.g., 北纬为正，东经为正
    """
    identifier: str = 'store-231118-01' # identifier for album name and raw data
    name: str = '地坛客栈'
    location: Tuple[float, float] = (39.95297, 116.41609)
    address: str = '北京市东城区安定门外大街 地坛公园附近 地坛客栈'
    supplement: str = '地坛公园附近最新客栈（2023冬开张）'
    phone: str = '010-84257666'
    num_photos: int = 0
