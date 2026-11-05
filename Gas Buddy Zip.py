import asyncio

from py_gasbuddy import GasBuddy


async def main():
    result = await GasBuddy().location_search(zipcode=zipcode)

    for s in result ["results"]:
        
        station = s["address"]
        
        print(station)
     #   print(s["address"])
      #  print(s["price_unit"])
asyncio.run(main())