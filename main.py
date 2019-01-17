import ConfigParser
import json

from sorting import sort_xml

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read('properties.ini')

    sort_by_col = config.get("SORTING", "sort_rule")
    sort_by_col = json.loads(sort_by_col)

    filter_rule = config.get("FILTER", "filter_rule")
    filter_rule = json.loads(filter_rule)

    xml_file = "input.xml"
    xslt_template = "template.xsl"

    header_tag = config.get("HEADER", "header")

    sort_xml(sort_by_col, xml_file, xslt_template, filter_rule, header_tag)