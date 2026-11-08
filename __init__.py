"""Listing AutomatEr Hermes plugin: registers one read only skill. No tools, hooks, network or env."""
from pathlib import Path

_SKILL = Path(__file__).parent / "skills" / "listing-automater" / "SKILL.md"


def register(ctx):
    ctx.register_skill(
        "listing-automater",
        _SKILL,
        description="Listing AutomatEr: Facebook Marketplace posting for real estate agents with permission to market listings, plus listing post writing guidance.",
    )
