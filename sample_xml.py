import xmltodict

filename = ("sample.xml");

file1 = open(filename, 'r');

dict_resp = xmltodict(xml,file);

print(dict_resp);
