# from __future__ import annotations
# import copy
# import random
# from typing import Callable, List

# import matplotlib.animation as animation
# import matplotlib.pyplot as plt


# __all__ = [
#     "record_states",
#     "animate_states"
# ]


# def record_states(
#     sort_fn: Callable[[List[int], Callable[[List[int]], None]], None],
#     arr: List[int],
# ) -> List[List[int]]:
#     """Run *sort_fn* on a **copy** of *arr* while collecting snapshots.

#     The *sort_fn* must accept the signature ``sort_fn(array, record_state)``
#     where *record_state* is a callback you invoke **every time** the array
#     changes (e.g. after each swap).

#     The returned value is the list of snapshots that can be fed to
#     :func:`animate_states`.
#     """

#     states: List[List[int]] = []

#     def _rec(state: List[int]) -> None:
#         # Copy so later mutations do not propagate back.
#         states.append(state.copy())

#     working = copy.copy(arr)  
#     sort_fn(working, _rec)
#     return states

# def animate_states(
#     states: List[List[int]], *, interval: int = 400, title: str = "Sorting animation"
# ):
#     """Turn *states* into a bar‑chart animation.

#     ``states`` is the list produced by :func:`record_states`.
#     In a regular Python session call ``plt.show()`` after this function returns;
#     in a Jupyter notebook do ``HTML(ani.to_jshtml())`` for inline playback.
#     """

#     if not states:
#         raise ValueError("No states to animate")

#     fig, ax = plt.subplots()
#     fig.set_tight_layout(True)

#     bars = ax.bar(range(len(states[0])), states[0], align="edge")
#     ax.set_xlabel("Index")
#     ax.set_ylabel("Value")
#     ax.set_title(title)
#     ax.set_xlim(0, len(states[0]) - 0.5)
#     ax.set_ylim(0, max(max(s) for s in states) * 1.1)

#     step_txt = ax.text(0.02, 0.95, "", transform=ax.transAxes)

#     def _update(frame: int):
#         for rect, height in zip(bars, states[frame]):
#             rect.set_height(height)
#         step_txt.set_text(f"Step: {frame}")
#         return (*bars, step_txt)

#     ani = animation.FuncAnimation(
#         fig,
#         _update,
#         frames=len(states),
#         interval=interval,
#         blit=True,
#         repeat=False,
#     )
#     return ani
