# Sorting-xml-with-xslt
Takes XML as the input and sorts filters it based on XSLT Template

**Prerequisites:**

* Python 2.7
* pip install cStringIO
* pip install lxml
* pip install json

**How it works:**

* Refer input.xml to form your xml file accordingly.
* Add sort, filter and headers in properties.ini file
    For example,
    * If you want to sort Title column in ascending and Status column in descending order, sort_rule property should have the following value.
        sort_rule = {"Title": "descending", "Status": "ascending"}

    * If you want to Filter rows with Passed Status and !Closed, filter_rule property should have the following value.
        filter_rule = {"Status": "!Closed || Passed"}

    * Header tag should have
        header = /Parent/Child....