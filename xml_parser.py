import xmltodict,sys
from docx import Document
import json,import_to_word
xml=sys.argv[1]
with open(xml) as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)
temp=json_data
list_nmap=temp.split('Nmap scan report for')
document = Document('nmap_table.docx')
def importer_to_docx(per):
    host=per[0]
    import_to_word.add_table(document)
    per.remove(per[0:1:][0])
    for item in per:
        import_to_word.row_count(document)
        data_dict=item
        p=data_dict['port']
        s=data_dict['service']
        v=data_dict['version']
        if s<1:
            s='None'
        elif p<1:
            p = 'None'
        elif v<1:
            v = 'None'
        import_to_word.insert_data(document,host,p,s,v)


for item in list_nmap:
    if "Host is up" in item  :
        try:
            out= item[:item.index('\\nHost'):]+ item[item.index('VERSION\\n')+7::]
            if list_nmap.index(item) == len(list_nmap) - 1:
                out = out[:out.index('Read data files'):]
            out=out.replace('\\n\\n','')
            out= out.split('\\n')
            first=out[0]
            ports=[]
            ports.append(first)
            for i in out:
                any_port_dict={}
                if 'open' in i :
                    port_number=i[:i.index('open'):].replace(' ','')
                    temp_service=i[i.index('open')+4::].lstrip()
                    service=temp_service[:temp_service.find(' '):].lstrip()
                    version=temp_service[temp_service.find(' ')+1::].lstrip()
                    any_port_dict.update({'port':port_number})
                    any_port_dict.update({'service':service})
                    any_port_dict.update({'version':version})
                    ports.append(any_port_dict)

            importer_to_docx(ports)
            print ports
        except Exception,e:
            print e

        print '----------------------------'

document.save(xml.replace('xml','docx'))