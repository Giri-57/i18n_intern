Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import json
data=json.load(open("C:/Users/Lenovo/Downloads/json.json",encoding="utf8"))
data

type(data)
<class 'dict'>
data.keys()
dict_keys(['type', 'features'])
data['type']
'FeatureCollection'
data['featurs']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data['featurs']
KeyError: 'featurs'
data['features']

type(data['features'])
<class 'list'>
data['features'][0]

type(data['features'][0])
<class 'dict'>
data['features'][0].keys()
dict_keys(['geometry', 'type', 'properties', 'id'])
data['features'][0]['geometry']

type(data['features'][0]['geometry'])
<class 'dict'>
data['features'][0]['geometry'].keys()
dict_keys(['type', 'coordinates'])
data['features'][0]['geometry']['type'])
SyntaxError: unmatched ')'
data['features'][0]['geometry'][type]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data['features'][0]['geometry'][type]
KeyError: <class 'type'>
data['features'][0]['geometry']['type']
'MultiPolygon'
data['features'][0]['geometry']['coordinates']

type(data['features'][0]['geometry']['coordinates'])
<class 'list'>
data['features'][0]['geometry']['coordinates'][0]
[[[93.84805297818306, 7.240280145604631], [93.84249877829927, 7.228610975131535], [93.85138702366079, 7.21389007108243], [93.8702774042622, 7.215834131699873], [93.88363647351434, 7.188451747905938], [93.87999725367499, 7.174723152826604], [93.8878936758917, 7.1511468735902985], [93.89138794259588, 7.1211109712483], [93.8877792385252, 7.086390065732503], [93.90166473542006, 7.077498939821743], [93.9166641267511, 7.048404273599602], [93.92205810300489, 7.009857134003413], [93.91390228193407, 6.9999999861240765], [93.92944335694526, 6.983888106019557], [93.93656921614681, 6.9623551775295915], [93.91722106724686, 6.944516144599245], [93.91027831921275, 6.923328856785091], [93.9164810142554, 6.912918022452581], [93.8972244242095, 6.902155839151327], [93.90159607274913, 6.881079258384722], [93.89360809633979, 6.866941030700211], [93.89360809477897, 6.846943882707896], [93.9087524429883, 6.838208227163111], [93.89623260732904, 6.804864926068334], [93.88513183817318, 6.795000116936779], [93.8682785043417, 6.815039174621699], [93.853202817781, 6.815390072935652], [93.8461074788681, 6.800555155714694], [93.84728241189066, 6.7798009323650215], [93.82831573670528, 6.754255805295052], [93.80665588130904, 6.76251979113323], [93.8133316058498, 6.807776961481051], [93.80110931471525, 6.813611997874592], [93.78571319680947, 6.8358488265651856], [93.79444122143222, 6.848899810327935], [93.77375030926072, 6.864097192163348], [93.77972412358268, 6.88152794556439], [93.76277923629166, 6.907779224884769], [93.75076293622884, 6.908124865726872], [93.74194335599924, 6.925000130143516], [93.75222015252122, 6.9388890035719], [93.74527740692571, 6.961945095178792], [93.73117065795007, 6.969559257913289], [93.72300720000683, 6.991942844371881], [93.7074661213691, 6.9897889356559695], [93.69930267299966, 7.011527055413396], [93.68583678985495, 7.018332920230984], [93.67028045257952, 7.013053823534785], [93.6652755720566, 7.041944950937884], [93.67028045441546, 7.0811118703933], [93.6602783229912, 7.086390065732503], [93.65583038271369, 7.126389016326523], [93.67582702498107, 7.139928793432795], [93.67490386887414, 7.176497923064195], [93.68611144671223, 7.189999996469531], [93.7130584707363, 7.192222101930918], [93.73361206054783, 7.187221050274635], [93.75499725081428, 7.211389019521805], [93.80770873928714, 7.214860899684803], [93.80831908756907, 7.228890822521257], [93.8261108422971, 7.23805098014438], [93.84805297818306, 7.240280145604631]]]
>>> data['features'][0]['geometry']['type']
'MultiPolygon'
>>> type(data['features'][0]['geometry']['type'])
<class 'str'>
>>> data['features'][0]['geometry']['properties']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data['features'][0]['geometry']['properties']
KeyError: 'properties'
>>> data['features'][0]['type']
'Feature'
>>> data['features'][0]['properties']
{'source': 'https://simplemaps.com', 'id': 'INAN', 'name': 'Andaman and Nicobar'}
>>> type(data['features'][0]['properties'])
<class 'dict'>
>>> data['features'][0]['properties'].keys()
dict_keys(['source', 'id', 'name'])
>>> data['features'][0]['properties']['source']
'https://simplemaps.com'
>>> data['features'][0]['properties']['id']
'INAN'
>>> data['features'][0]['properties']['name']
'Andaman and Nicobar'
>>> data['features'][0]['id']
1
>>> type(data['features'][0]['id'])
<class 'int'>
