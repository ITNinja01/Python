import asyncio

from py_gasbuddy import GasBuddy

zipcode = input('Type in a zipcode: ')

async def main():
    result = await GasBuddy().price_lookup_service(zipcode=zipcode,limit=10)

    for station in result["results"]:
        print(station["name"])
        if "regular_gas" in station:
               print(station["regular_gas"]["formatted_price"])
               print(station["address"]["line1"])   
               print()
asyncio.run(main())