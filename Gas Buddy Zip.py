import asyncio

from py_gasbuddy import GasBuddy

zipcode = input('Type in a zipcode: ')
async def main():
    result = await GasBuddy().location_search(zipcode=zipcode)

    for s in result ["results"]:
        
       gasstation = s["station_id"]

       print(gasstation)

      # gb = GasBuddy(station_id=gasstation)
      # data = await gb.price_lookup()
      # print(data["name"])
     
       # print(s["station_id"])
       # print(s["address"])
asyncio.run(main())