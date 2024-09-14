from dataclasses import dataclass
from environs import Env


@dataclass
class BotConfig:
    TOKEN: str
    ADMIN_ID: list[int]


@dataclass
class Config:
    BOT: BotConfig


def load_config() -> Config:
    env = Env()
    env.read_env()

    config = Config(
        BOT=BotConfig(
            TOKEN=env('BOT_TOKEN'),
            ADMIN_ID=list(map(int, env.list('BOT_ADMIN_ID')))
        )
    )

    return config
