from ciscoconfparse import CiscoConfParse
from colorama import Fore, Style
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
        template_name = template_dict["TEMPLATE_NAME"]
        template_type = template_dict["TEMPLATE_TYPE"]
        print(f'{Fore.BLUE}VERIFYING TEMPlATE: ' + template_name)
        print(f'**************************************{Style.RESET_ALL}')

        for template_section in template_dict["SECTIONS"]:
            regex_pattern = template_section["SECTION_REGEX"]
            sub_regex_patterns = template_section["LINES"]
            section_name = template_section["NAME"]
        #regex_pattern = template_dict["SECTION_REGEX"]
        #sub_regex_patterns = template_dict["LINES"]

            print(f'{Fore.GREEN}-VERIFYING SECTION: {Fore.CYAN}' + section_name + f'{Style.RESET_ALL}')

            ## Find all matching sections (multi line objects)
            for object in confparse.find_objects(regex_pattern):
                is_valid = True

                ## Mark that some lines are missing if we ever have to print that object
                cfgdiffs.append_line(f'{Fore.RED} -> MISSING OR DIFFERENTLY CONFIGURED LINES')
                cfgdiffs.append_line(f'   ' + object.text + f'{Style.RESET_ALL}')

                ## Search children of the object
                for subregex in sub_regex_patterns:
                    if not (object.re_search_children(subregex)):
                        cfgdiffs.append_line("    " + subregex)
                        is_valid = False

                if(is_valid==False):
                    for line in cfgdiffs.ioscfg:
                        print(f'{Fore.RED}' + line + f'{Style.RESET_ALL}')
                else:
                    print(f'{Fore.GREEN} -> SUCCESS - CONFIG SECTION: ' + template_name + ' FOR OBJECT: ' + object.text + f'{Style.RESET_ALL}')

                #Reset cfgdiffs for next object
                cfgdiffs = CiscoConfParse([])

        ## Find all single line objects
        if(template_type=='SINGLE_LINE_AND_MULTI_SECTION'):
            is_valid = True
            print(f'{Fore.GREEN}-VERIFYING GENERAL LINES: {Style.RESET_ALL}')
            regex_patterns = template_dict["SINGLE_LINE_REGEXES"]
            for line in regex_patterns:
                if not confparse.has_line_with(line):
                    print(f'{Fore.RED} -> MISSING OR DIFFERENTLY CONFIGURED LINES: ' + line + f'{Style.RESET_ALL}')
                    is_valid = False
            if (is_valid==True):
                print(f'{Fore.GREEN} -> SUCCESS - GENERAL CONFIG PARTS: ' + template_name + f'{Style.RESET_ALL}')

        print(f'{Fore.BLUE}*****************END*********************{Style.RESET_ALL}\n')


if __name__ == "__main__":
    main()

