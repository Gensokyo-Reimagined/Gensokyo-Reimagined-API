from stores.Database import Database

import datetime


async def get_player_clans(db: Database, player: str = None):
    select_query = """
        SELECT up.name, mp.uuid, mp.class, mp.level, mp.guild, mp.last_login
        FROM `mmocore_playerdata` mp
        JOIN `uclans-players` up ON mp.uuid = up.id
        WHERE up.name = %s
    """
    mmo_data = await db.execute(select_query, player)
    # timestamp conversion
    if mmo_data:
        # because return is an array of new assignment first
        mmo_data = mmo_data[0]
        timestamp = int(mmo_data['last_login']) // 1000  # ms to s
        last_login = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        mmo_data['last_login'] = last_login

    return mmo_data
