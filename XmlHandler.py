import xml.dom.minidom


def process(file_path):
    doc = xml.dom.minidom.parse(file_path)

    lines = []
    
    
    firstLine = []
    dt_created = doc.getElementsByTagName("dhEmi")[0].firstChild.nodeValue
    nfe_id = doc.getElementsByTagName("nNF")[0].firstChild.nodeValue
    
    try:
        name = doc.getElementsByTagName("xFant")[0].firstChild.nodeValue
    except:
        name  = doc.getElementsByTagName("xNome")[0].firstChild.nodeValue
    
    firstLine.append(dt_created)
    firstLine.append(name)
    firstLine.append(nfe_id)
    
    sups = doc.getElementsByTagName("dup")
    first = True
    for sup in sups:
        dt_sup = sup.getElementsByTagName("dVenc")[0].firstChild.nodeValue
        value_sup = sup.getElementsByTagName("vDup")[0].firstChild.nodeValue
        if(first):
            first = False
            firstLine.append(dt_sup)
            firstLine.append(value_sup)
            xml_number = doc.getElementsByTagName("chNFe")[0].firstChild.nodeValue
            firstLine.append(xml_number)
            lines.append(firstLine)
        else:
            line = []
            line.append("")
            line.append("")
            line.append("")
            line.append(dt_sup)
            line.append(value_sup)
            lines.append(line)

    # case no sup
    if(first):
        firstLine.append("")
        firstLine.append("")
        xml_number = doc.getElementsByTagName("chNFe")[0].firstChild.nodeValue
        firstLine.append(xml_number)
        lines.append(firstLine)

    return lines
    