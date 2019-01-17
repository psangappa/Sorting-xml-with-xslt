def form_filter_rules(fkey, fval, widget):
    """ This method forms the filtering rules"""
    equal = """!='{}'"""
    not_equal = """='{}'"""
    contains = """[not(contains(., '{}'))]"""
    not_contains = """[contains(., '{}')]"""
    xslt_filter = """<xsl:template match="{}{}"/>"""
    rule = """{}/text()""".format(fkey)
    filter_rule = """["""
    if "||" in fval:
        for value in fval.split("||"):
            value = value.strip(" ")
            if value.startswith('!') and value.find('*') > -1:
                filter_rule += rule + not_contains.format(value.strip("*! ")) + """ or """
            elif value.startswith('!'):
                filter_rule += rule + not_equal.format(value.strip("! ")) + """ or """
            elif value.find("*") > -1:
                filter_rule += rule + contains.format(value.strip("* ")) + """ and """
            else:
                filter_rule += rule + equal.format(value.strip(" ")) + """ and """
    else:
        if fval.startswith('!') and fval.find('*') > -1:
            filter_rule += rule + not_contains.format(fval.strip("*! ")) + """ and """
        elif fval.startswith('!'):
            filter_rule += rule + not_equal.format(fval.strip("! ")) + """ and """
        elif fval.find("*") > -1:
            filter_rule += rule + contains.format(fval.strip("* ")) + """ and """
        else:
            filter_rule += rule + equal.format(fval.strip(" ")) + """ and """
    if filter_rule.endswith(" or "):
        filter_rule = filter_rule[:-4] + """]"""
    else:
        filter_rule = filter_rule[:-5] + """]"""
    return xslt_filter.format(widget, filter_rule)