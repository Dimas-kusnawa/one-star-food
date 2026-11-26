"""One Star, Five Stars for the Food — make.fun entry.

One sentence (183 chars, inside the 1-200 gate) in the voice of an alien
tourist giving planet Earth a one-star review while still complimenting
the food. Writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Three candidates, judged the way the house judge would (deadpan travel
critic from another planet; criteria in order: on-brief alien one-star
review with a food compliment, convincing alien voice, joke lands with a
funny turn, one sentence in the limit, fresh angle):

A (168 chars) — queuing + chicken satay:
  "One star: your species queues for hours to buy tiny paper rectangles,
  then calls it a holiday, but the chicken satay with peanut sauce almost
  made me forgive the queue."
  Weakest: "tiny paper rectangles" is muddled (tickets? money?), the food
  compliment sits mid-sentence, and the twist is about the queue, not
  the food.

B (182 chars) — tipping + nasi goreng:
  "One star: on Earth you must tip the human who carried your plate, as
  if carrying were not already the job, but the nasi goreng was so good
  I tipped twice and apologized to the plate."
  Strong alien bafflement and a good last-words twist, but "as if
  carrying were not already the job" is wordy and tipping is a
  well-worn alien joke.

C (183 chars) — small talk + tonkotsu ramen — CHOSEN:
  "One star: every human here asks 'how are you' and then walks away
  before the answer, which is rude in twelve galaxies, but the tonkotsu
  ramen was worth the entire interstellar flight."
  Freshest habit (small talk nobody answers), most distinct alien voice
  ("rude in twelve galaxies"), and the food compliment IS the punchline
  in the last words — the ramen outranks the whole interstellar trip.
"""

ENTRY = (
    "One star: every human here asks 'how are you' and then walks away "
    "before the answer, which is rude in twelve galaxies, but the "
    "tonkotsu ramen was worth the entire interstellar flight."
)


def write_entry() -> str:
    """Write the entry sentence to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    import os
    from pathlib import Path

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    return str(target)


if __name__ == "__main__":
    print(write_entry())
