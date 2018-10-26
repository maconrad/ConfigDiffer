from ciscoconfparse import CiscoConfParse
import config
import json


def load_template(template):
    json1_file = open(template)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data

def main():
    confparse = CiscoConfParse(config.USER_CONFIG)
    cfgdiffs = CiscoConfParse([])

    for template in config.TEMPLATES:
        template_dict = load_template(template)

        regex_pattern = template_dict["SECTION_REGEX"]
        sub_regex_patterns = template_dict["LINES"]
        template_name = template_dict["TEMPLATE_NAME"]

        print("VERIFYING TEMPlATE: " + template_name)

        ## Find all matching sections
        for object in confparse.find_objects(regex_pattern):
            is_valid = True

            ## Mark that some lines are missing if we ever have to print that object
            cfgdiffs.append_line(" -> MISSING OR DIFFERENTLY CONFIGURED LINES")
            cfgdiffs.append_line("   " + object.text)

            ## Search children of the object
            for subregex in sub_regex_patterns:
                if not (object.re_search_children(subregex)):
                    cfgdiffs.append_line("    " + subregex)
                    is_valid = False

            if(is_valid==False):
                for line in cfgdiffs.ioscfg:
                    print(line)
            else:
                print(" -> SUCCESS - CONFIG SECTION: " + template_name + " FOR OBJECT: " + object.text)

            #Reset cfgdiffs for next object
            cfgdiffs = CiscoConfParse([])


if __name__ == "__main__":
    # create CiscoConfParse object using a configuration file that is stored in the
    # same directory as the script
    main()
