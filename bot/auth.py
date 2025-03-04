import aiohttp


async def register(data: dict):
    async with aiohttp.ClientSession() as session:
        payload = {
            "username": data["name"],
            "password": data["password"]
        }
        async with session.post("http://api:8000/register", json=payload) as response:
            if response.status == 200:
                return True
            else:
                return False
