############
How to use
############

This document quickly describes how to use the Script.

Under the Files folder, you will find separate folders:

*   SampleCfgs
*   Templates

SampleCfgs folder usually stores the IOS configs. But these could be located
anywhere.

Templates follow a regex pattern and allow to verify the existence/absence of
config according to the template. Lets take a IOS config snipp to understand
the templates:

.. literalinclude:: config_sample.txt
    :linenos:

To verify that this config or part of it exists, a json file in the following
format is used:

.. literalinclude:: template_sample.json
    :linenos:


The following important points should be noted::

    Line 3: Defines the Type of the Template, currenntly MULTI_SECTION
            and SINGLE_LINE_AND_MULTI_SECTION exist. The SINGLE_LINE type
            allows additionally for top level commands to be verified, that
            are not part of a Section.
    Line 7: Defines the regex to search for the section.
            It could bei router, router eigrp, router eigrp 1 and allows
            for more specific matches to validate existence of lines
            or exact matching of lines
    Line 8: Defines the lines that need to exist within a certain section.
            Again: Lines can be exact matches (Line 9) or only match
            partly (Line 10).

Under mainapp/config.py one can configure which templates
the config should be verified against and which config to run
the script against. The file should be self explanatory.

.. literalinclude:: ../../mainapp/config.py
    :linenos:

