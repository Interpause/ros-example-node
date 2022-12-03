"""
Simple example pub-sub to measure communication rate. Surprisingly, the RQT
topic monitor plugin chokes if the messages are:
- big (like images)
- rapid
- published using Best Effort (vs Reliable) QoS
Hence this example serves as a potential replacement for measuring bandwidth & latency.

NOTE: Shared memory only works if using C++.
See https://github.com/ros2/design/issues/251 for progress on bringing shared
memory to all language clients.

Max Rate:
@ 1 char: ~12500Hz
@ 1,000,000 chars: ~3000Hz
@ 10,000,000 chars: ~60Hz (sudden exponential drop?)
"""
__version__ = "0.1.0"
