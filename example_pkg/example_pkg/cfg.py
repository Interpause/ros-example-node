from __future__ import annotations

from dataclasses import dataclass

from example_pkg.utils import JobCfg


@dataclass
class SubscriberCfg(JobCfg):
    topic: str = "topic"
    """Topic to publish to."""
    buf_size: int = 1000
    """Maximum size of rate timings buffer."""
    buf_duration: int = 2
    """Maximum duration in seconds of rate timings buffer."""
    max_rate: int = 0.5


@dataclass
class PublisherCfg(JobCfg):
    topic: str = "topic"
    """Topic to publish to."""
    pub_size: int = 10
    """Size of msg to publish."""
