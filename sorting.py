from cStringIO import StringIO
import lxml.etree as ET

from filter_rule import form_filter_rules


def sort_xml(sort_by_col, xml_file, xslt_template, filter, header_tag):
    sort_rules = StringIO()
    filter_col_rules = StringIO()
    with open(xml_file) as xml:
        xml_str = xml.read()
    dom = ET.fromstring(xml_str)
    with open(xslt_template) as xslt_file:
        xslt_str = xslt_file.read()

    for key in sort_by_col:
        sort_rules.write("""\n\t\t\t\t<xsl:sort select="%s" order="%s"/>""" % (key, sort_by_col[key]))

    for key in filter:
        rules = form_filter_rules(key, filter[key], header_tag)
        filter_col_rules.write("""\n\t%s""" % rules)

    if len(filter_col_rules.getvalue()) > 0:
        xslt_str = xslt_str.replace(
            """<!-- hide rules -->""", filter_col_rules.getvalue())

    if len(sort_rules.getvalue()) > 0:
        xslt_str = xslt_str.replace(
            """<!-- this is to sort -->""", sort_rules.getvalue())

    xslt = ET.fromstring(xslt_str)
    transform = ET.XSLT(xslt)
    new_dom = transform(dom)
    new_xml = ET.tostring(new_dom)
    print(new_xml)

