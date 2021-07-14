def sorter(all_read):
    ip=''
    all=[]
    for item in all_read:
        part=[]
        if item[0]!=ip:
            ip=item[0]
            host=item[1]
            os=item[2]
            cve=item[5]
            port=item[4]
            vuln=item[3]
            shedat=item[7]
            cvs=item[6]
            all.append(ip)
            all.append(host)
            all.append(os)
            part.append(cve)
            part.append(port)
            part.append(vuln)
            part.append(shedat)
            part.append(cvs)
        else:
            cve = item[5]
            port = item[4]
            vuln = item[3]
            shedat = item[7]
            cvs = item[6]
            part.append(cve)
            part.append(port)
            part.append(vuln)
            part.append(shedat)
            part.append(cvs)
        all.append(part)

    return all

def ye_cut(huge):
    new=[]
    new.append(huge[0])
    huge.remove(huge[0:1:][0])
    new.append(huge[0])
    huge.remove(huge[0:1:][0])
    new.append(huge[0])
    huge.remove(huge[0:1:][0])
    while type(huge[0])==type([]):
        new.append(huge[0])
        huge.remove(huge[0:1:][0])
        if huge==[]:
            break
    return new