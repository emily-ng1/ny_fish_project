import requests
import json

#NOTES: Ocean name and fishes for class

#https://www.fishwatch.gov/developers
def fish_data():
    fish_url="https://www.fishwatch.gov/api/species"
    response=requests.get(fish_url)
    fishes=response.json()
    return fishes

#https://amentum.io/ocean_docs#tag/rtofs
def location_infos(latitude, longitude, depth):
    url="https://ocean.amentum.io/rtofs"
    headers={"API-Key": "PBPVE02H65AKoc219baXIOr46K5c2QKT"}

    params={
      "latitude": latitude,
      "longitude": longitude,
      "depth": depth
    }

    # handle exceptions
    response=requests.get(url, headers=headers, params=params)
    json_payload=response.json()
    return json_payload

#https://globalfishingwatch.org/our-apis/
#https://globalfishingwatch.org/our-apis/documentation#quick-start
#https://globalfishingwatch.org/our-apis/documentation#basic-search
#https://globalfishingwatch.org/datasets-and-code-vessel-identity/
def all_fishing_vessesls():
    token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJmaXNoaW5nIiwidXNlcklkIjoyMzk5NCwiYXBwbGljYXRpb25OYW1lIjoiZmlzaGluZyIsImlkIjo0OTMsInR5cGUiOiJ1c2VyLWFwcGxpY2F0aW9uIn0sImlhdCI6MTY3Nzk4NzM0NCwiZXhwIjoxOTkzMzQ3MzQ0LCJhdWQiOiJnZnciLCJpc3MiOiJnZncifQ.oEftYjkxHguFbYM5_-5Rk3uH9gQ-xNixoYAejX68VNINi8pFxePxInWENLjOM239pSp7VPIxqM0QUuwTwNc978runRW8RL_8UMFHHZ-GFXRnIQRPRVVimKrmqrDpQJA0abLcGy9jDdChYR6lbhRx9W1cyCGI0E6wy8OFbjzuZ0WaKfxYY0g12Qk3pBgtRLOhjvX9un4Vv6TAXUPGUnVLUxl3l4fNZ7979QgkIj6Us03s-2rCgWpL4UdiHO1LSgq3lvC-vS-Q8PilxeZG6QIyU90qoBrCLXgpn54OHdjchJbKnqWV1pd5oMbaokVIhAo3wimE0x0KNx0lZMNEjVTEW5mVNuUE0_erGVbffLjgvX_skbhbgmcAOYTqcML9_BNOVzJzthaDtYtdVsHmPecEi1Pa9ZN4ALpY_SSfMXJ1lS-iMoH7EIN5MniW8OMmlLsY2h6SuVq6i_lMI4PrwlTsp5CsbIPwxchHh-MI-m7PEi75_t2ysc6sUzEwdRduDGiX"
    headers={"Authorization": f"Bearer {token}"}

    root_url='https://gateway.api.globalfishingwatch.org/v2/vessels/search'
    query='query=all&datasets=public-global-fishing-vessels:latest&limit=130&offset=0'
    response=requests.get(f"{root_url}?{query}", headers=headers)
    return response.json()

def vessel_ids():
    vessels_data=all_fishing_vessesls()
    vessels=vessels_data["entries"]
    return [vessel['id'] for vessel in vessels]

len(vessel_ids()) #130
", ".join(vessel_ids())

#Pull all fishing vessel activity for year 2022
def vessel_infos():
    token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJmaXNoaW5nIiwidXNlcklkIjoyMzk5NCwiYXBwbGljYXRpb25OYW1lIjoiZmlzaGluZyIsImlkIjo0OTMsInR5cGUiOiJ1c2VyLWFwcGxpY2F0aW9uIn0sImlhdCI6MTY3Nzk4NzM0NCwiZXhwIjoxOTkzMzQ3MzQ0LCJhdWQiOiJnZnciLCJpc3MiOiJnZncifQ.oEftYjkxHguFbYM5_-5Rk3uH9gQ-xNixoYAejX68VNINi8pFxePxInWENLjOM239pSp7VPIxqM0QUuwTwNc978runRW8RL_8UMFHHZ-GFXRnIQRPRVVimKrmqrDpQJA0abLcGy9jDdChYR6lbhRx9W1cyCGI0E6wy8OFbjzuZ0WaKfxYY0g12Qk3pBgtRLOhjvX9un4Vv6TAXUPGUnVLUxl3l4fNZ7979QgkIj6Us03s-2rCgWpL4UdiHO1LSgq3lvC-vS-Q8PilxeZG6QIyU90qoBrCLXgpn54OHdjchJbKnqWV1pd5oMbaokVIhAo3wimE0x0KNx0lZMNEjVTEW5mVNuUE0_erGVbffLjgvX_skbhbgmcAOYTqcML9_BNOVzJzthaDtYtdVsHmPecEi1Pa9ZN4ALpY_SSfMXJ1lS-iMoH7EIN5MniW8OMmlLsY2h6SuVq6i_lMI4PrwlTsp5CsbIPwxchHh-MI-m7PEi75_t2ysc6sUzEwdRduDGiX"
    headers = {"Authorization": f"Bearer {token}"}

    root_url='https://gateway.api.globalfishingwatch.org/v2/events'
    #query = 'vessels=a328cfcdf-f806-764b-10aa-d3f45d15ffd0&datasets=public-global-fishing-events:latest&start-date=2022-01-01&end-date=2022-12-31&limit=6940&offset=0'
    query='vessels=a328cfcdf-f806-764b-10aa-d3f45d15ffd0, ead3e56fb-bcaf-5561-174f-c54c81b88d75, bf8f7c3c0-0e87-f69b-b66a-88638ae8ec9e, c9ec15d23-3f8d-e9f8-9ad3-3711a83f189f, 0546918a5-55a8-736e-332f-9c275aab9a13, 58f19566c-c5ea-aa38-38cf-14d31b5fabbf, 1d13ff677-7ae5-e35c-24f8-576103981d13, 02b87f90e-e8e4-4730-6ba1-1175ac197845, 18836295d-de27-6dc7-1013-3dc1d13e4e1a, 6f783e530-06ff-a414-45fc-9c6218cf9f85, 5fba1c296-61ed-83b0-ebda-2dcfe54abd81, 622ee43b4-4ccd-065b-9015-a14f6da89468, 2229141e5-52f0-e620-7e10-2a3a51cb40ff, 99bf92433-3a53-1fd8-5924-f8b226b05647, d75c4182e-e279-46cc-922e-a1756ecf02d2, c4f8533e9-9e63-85b8-866e-6cf441604d72, fc5b26b9a-af27-54d8-f70f-512ae6da08f7, f5a7c9460-04dd-96f2-6e5e-1c123bec573f, 0dec8bf00-035c-78ee-a9d5-e6fce12fd506, 1b4e3d45b-bb82-45c6-6c48-a29a7757c2b5, 9b28be1bb-beba-8a0b-af0f-bfc7d9bb8657, e314379a5-5ace-4b43-7c83-9878d6808065, b76337c67-79b3-8e62-d6f6-9a3d4c30cca4, 575d5933d-d395-f8d5-09a4-bc782078000c, e4fafcfc9-9649-d2c9-b15c-19bbed709bbf, cda7510a7-7f2b-ec36-b9bb-6742e9a1dd65, aea74dc11-119e-24b4-1e0f-2113345b4dc8, f7f5c41ca-a5ad-18ac-9ab8-4a71c55c4fc4, 68c1dff81-106a-827a-bbf8-f3980c308c1c, 850ba79e5-58c8-c6d2-2daf-b7d67f8130c8, e9a24a2a9-9f25-6403-b772-a04303b2ac72, e87cb14b9-9001-3229-077f-841af68621f3, 901b60200-0661-bdff-d62d-131e5e3d6698, 134868c82-272d-5623-c576-13c20bf4126a, 7be6aa6ea-a08e-39db-7787-c693615863cf, 977f3e622-2e07-8402-7e2d-8f5dde25b2e7, b83ba05bb-bfb4-a833-4a6e-b5c1654206c8, fc000617a-a61e-7fb0-b84e-d81fb9b4a7fe, 6625e752d-d967-1281-002c-a71656152399, 5f68108fb-bc4a-3520-0da4-47372fa6c75e, 46369c258-8cc0-f063-88eb-8618c09d07e0, 81ef13eb8-80dc-e20d-4f54-2f20c08733cc, 46d54b28a-a0b2-ba37-a7d2-cdc4da6c9777, 388d11ce8-8d28-7134-5a0c-69f17f49a3ac, a313e5d7d-d337-8475-a547-a7ac9a54ff50, dbe400c0c-c7ac-f432-f41a-9b9166dcd11e, 1c685f383-31da-83aa-7428-4b4255cb7466, 3505e1a38-85aa-ada7-a7ef-a1c76035d1fd, 0af729c4c-c31f-0a2e-ee31-f10b10d6ce1a, b3f1b289d-ddb4-9906-06e5-5221431a00ac, 869518520-0c23-c8fa-d56c-685d7f558fe4, a0f4c410f-fc7d-564e-a776-fbff63795938, e1bae18c6-609f-c955-d39d-cb0c0b8f31f9, c851861ca-a8c1-8071-9a23-241d45b74e1e, 208937a2c-c032-d4d5-026b-ba76f25b7287, 598a9e10d-ddcf-b5a8-4b64-fcd9f840e2a1, 84213124d-df64-172b-0bdf-4d9d9e166440, 1c8f3a105-5eaf-e3c3-5dfd-de348aa32a00, fb6e99b98-84a7-4dd7-0e9b-238ed0a6e7aa, 220ec3126-6cd0-cbd7-fa07-a9004500c307, cb1896d57-70fe-6792-627a-778aa3871f52, 6e5a444f8-83e1-686a-4509-95751f0593e1, b0fc47fb1-17a7-888b-f40e-98e9e65a2d4f, 617f46300-0330-a144-5a1f-b824756b84f3, 9e5535e3e-e312-67d6-d217-ca13664be89d, 2d9096bbe-e38a-ae57-8d3c-753f38b36b38, 3c9a8e82d-d36c-9049-645b-6d9c7d4d878d, 598f9cad0-08b2-ea4c-3ccc-2df73b3bb539, aca8bfd90-0bb6-04f3-f5ce-517a3a25aa52, 684165050-0486-ec91-5a31-27b6f7a4ae29, 128981239-97f0-b6ae-cab9-e016bcc8248d, 800c0d4a7-73ca-2d92-cf7d-7d23ab455cd6, 2d2b10537-74da-cea1-0475-b5ce56a336a2, fba58f0cf-f3a8-0e12-f913-2f9cb6de11ee, d8edea176-6084-22b1-951d-d8895864b0c3, 7f8aa8176-652c-381c-0a10-a1f01f303d10, 3114876e2-25c9-c7f5-0db4-61f222fe7fd4, 4be4815a4-4aee-b228-05f5-947aa010dd9e, 6b07d4f28-81cb-76f3-b0cb-0f124e192417, b7e0f6d39-9a13-c0d6-1257-5a5c733b3994, 6bf312766-6714-d629-bb0b-7d3f91d7c30e, af5891aa9-965e-5529-e53b-4be52a194266, 4f4ecec15-52be-160f-8a87-febadb80371c, f2e0b0e66-6c93-bf86-8585-22cb72109ea1, 7a1dee94e-ec91-878f-86f5-c8d41246cdf3, ad81affda-a631-55e1-a8d7-6e6ebbc3f2b3, 2d9c1a530-01d2-3fc2-da01-10449241efb9, cfabc0090-00a5-d02b-2d1b-7dd65478274c, 58120bc52-283d-7667-67c6-3a15688b5ba1, 899b8bda0-031c-98e7-ba4b-18139d3968ef, c03f2f7d9-9f3e-70da-4af4-ec1997e6d83c, 1714ad136-695a-257b-9bce-9da220f3644e, eec162cc9-92e1-8a94-6fe8-eed4148baddd, d01d10580-0cf7-b9ce-7b91-1c4ae7a7c5da, f80991a3e-e178-be1f-513f-f0ab9e072df3, 7bce98b1e-e0e8-cef3-55a7-dc92390e2d8a, 0db0ca214-4b9d-d61a-e21f-f10def255993, 9b6e23707-72e6-87b3-bbb7-46d2017a1221, 916c66001-19b9-44e9-88b3-33851bcb9382, bc1263504-4591-baa9-e336-fd7d07f43e0e, 6113fb5a6-670c-e0fb-e2bd-8edf63b55797, 66c58ab24-47dd-e4bb-d061-5d83193c9289, cad6090e6-6c47-4dd9-c207-a7448f68bacc, 14a92347e-e25a-0479-8582-ae15c42a4a46, 1ed5f6940-078f-4847-a526-75b1fa57e846, abb1f8880-03ab-5bac-2444-9fbc61a6de68, 355f44f11-1748-52c7-3241-bd2abfe0a53b, 100ea0b39-9750-619e-bcf1-c1a1c873a9de, 091d7f390-0c28-7d65-27ac-3be7a2727c88, d75f47f24-454f-4f70-c6ea-46c202c34238, 8b519e7cb-b114-bb60-6269-3e9b82d5cbb7, a4faafe29-98c0-e474-6ff2-be283c3316ff, 2d2ee52c3-300a-3f9a-401c-a15444c04208, 858d63290-096f-00eb-43a1-78de7aee1e8c, 9ec39ceb0-0a3e-7910-87cc-c8db8e7b717e, a4e1a3e67-7bc3-4ec0-a003-d35e0ed5fdd2, 2c81e8b65-5ba4-1c42-3d1e-8e1e2b513821, c3086f24e-e3f8-4790-4cb5-42bc3011deef, f774a36a0-0ac2-8715-b6cd-702a6592b3df, 2b8946878-8b85-4fb6-1cf1-54b9720ae404, f69ca08f1-190c-1062-cf97-de7e5deb1765, c14c7586a-abf9-3c86-959b-b87a0dc45c8d, 33e6e6f31-1385-4518-ad92-a86a761663fc, 0f070e124-4456-16ea-a69c-16eb74798fc8, 7ed7c03ef-fcba-9f1a-d408-64ac6167ce43, faf5c906c-c035-798c-0478-3b6ea87c8bb6, fe7172b63-3a20-c73b-3cc0-abc32b972161, 70e75f9dd-d380-92a5-d4b3-0d2059d921b1, d2af693c4-45f0-2ca0-fbb9-de7eaeb3bf58, a0456bb8d-d536-8a22-9087-711e27791e48&datasets=public-global-fishing-events:latest&start-date=2022-01-01&end-date=2022-12-31&limit=6940&offset=0'
    response=requests.get(f"{root_url}?{query}", headers=headers)
    return response.json()

#Data sets:
fishes=fish_data()
fishing_vessels=vessel_infos()

def remove_fishes_without_location(fishes):
    return [fish for fish in fishes if fish["Location"]]

fishes_updated=remove_fishes_without_location(fishes)


#Extract location of each fish
water_source=["pacific", "arctic", "atlantic", "indian", "north atlantic", "south atlantic", "indo-pacific",
              "gulf of alaska"]
coordinates=[{"latitude":8.7832, "longitude":124.5085}, {"latitude":65.2482, "longitude":60.4621},
             {"latitude":14.5994, "longitude":28.6731}, {"latitude":33.1376, "longitude":81.8262},
             {"latitude":35.7465, "longitude":39.4629}, {"latitude":33.7243, "longitude":15.9961},
             {"latitude":9.79568, "longitude":118.82813}, {"latitude":57.0000, "longitude":144.0000}]


def fish_locations(fishes_updated):
    locations=[fish["Location"] for fish in fishes_updated]
    return locations





fishes[0]["Species Name"]
fishes[2]["Location"]
fishes[0]["Habitat"]

fishes[1]["Species Name"]
fishes[7]["Location"]
fishes[3]["Calories"]

test=fishes[5]["Location"].lower()
test_list=test.split(" ")
for i in test_list:
    if i in oceans:
        print(i)



new_loc=[]
fish_id=[]
updated_fish_locations=[location.lower() for location in fish_locations(fishes_updated)]
for location in updated_fish_locations:
    for word in location.split(" "):
        if word in water_source:
            new_loc.append((updated_fish_locations.index(location), word))
            fish_id.append(updated_fish_locations.index(location))
unique_list=sorted(list(set(new_loc)))
dict(unique_list)

unique_fish_id=sorted(list(set(fish_id)))


for i in range(len(updated_fish_locations)):
    if i not in unique_fish_id:
        print(i)

updated_fish_locations[8]
