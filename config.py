from dataclasses import dataclass
from environs import Env


@dataclass
class BotConfig:
    TOKEN: str
    ADMIN_ID: list[int]


# @dataclass
# class DatabaseConfig:
#     USER: str
#     PASSWORD: str | None
#     HOST: str
#     PORT: str
#     DATABASE: str


@dataclass
class Config:
    BOT: BotConfig
    # DATABASE: DatabaseConfig


def load_config() -> Config:
    env = Env()
    env.read_env()

    config = Config(
        BOT=BotConfig(
            TOKEN=env('BOT_TOKEN'),
            ADMIN_ID=list(map(int, env.list('BOT_ADMIN_ID')))
        ),
        # DATABASE=DatabaseConfig(
        #     USER=env('DB_USER'),
        #     PASSWORD=env('DB_PASSWORD'),
        #     HOST=env('DB_HOST'),
        #     PORT=env('DB_PORT'),
        #     DATABASE=env('DB_NAME')
        # )
    )

    return config
