'''
ospf_regex_pattern = r"^router ospf \d+$"

# in this case, we will simply check that the ospf router command is part of the config
is_ospf_in_use = confparse.has_line_with(ospf_regex_pattern)

if is_ospf_in_use:
    print("==> OSPF is used in this configuration")
    result["features"].append("ospf")
else:
    print("==> OSPF is not used in this configuration")


            #if (section.re_search_children(subregex)):
            #    print("Found matching subsection" +

        if (object.re_search_children(r"ip\saddress\s1\.1\.1")):
            cfgdiffs.append_line("!")
            cfgdiffs.append_line(object.text)  # Add the interface text
            cfgdiffs.append_line(" mpls ip")


JSON
{
  "TEMPLATE_NAME" : "EIGRP ROUTER",
  "SECTION_REGEX" : "router eigrp",
  "LINES" : [
    "network 10.0.0.0",
    "passive-interface default",
    "eigrp router-id",
    "eigrp stub connected"
  ],
  "test" : [20,30,40]
}


class Config(object):
    def __init__(self):
        self.verbose = False
        self.homedir = ""
        self.restclient = ""
        self.logfile = ""



'''