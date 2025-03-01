# generated by DipDup 8.2.1

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ReactorClassHashUpdatedPayload(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    old_hash: int
    new_hash: int
    powerplant: int
    block_timestamp: int
